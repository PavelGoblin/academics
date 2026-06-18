"""
Dogs vs Cats Image Classification
====================================
Goal: Classify images as dog or cat
ML Task: Binary Image Classification (CNN)
Algorithm: Convolutional Neural Network (TensorFlow/Keras)
"""

import kagglehub
import os
import zipfile
import numpy as np
import matplotlib.pyplot as plt

# 1. Load & Extract Data
print("[1] Downloading dataset...")
path = kagglehub.competition_download("dogs-vs-cats")
print(f"Downloaded to: {path}")

# Extract if needed
if not os.path.exists("dogs_vs_cats_data"):
    os.makedirs("dogs_vs_cats_data", exist_ok=True)
    with zipfile.ZipFile(f"{path}/train.zip", 'r') as z:
        z.extractall("dogs_vs_cats_data")
    print("  Extracted to 'dogs_vs_cats_data/'")

# 2. Check data
train_dir = "dogs_vs_cats_data/train"
files = os.listdir(train_dir)
dogs = sum(1 for f in files if f.startswith('dog'))
cats = sum(1 for f in files if f.startswith('cat'))
print(f"\n[2] Data: {dogs} dogs, {cats} cats")

# 3. Prepare data using Keras image_dataset_from_directory
import tensorflow as tf
from tensorflow import keras
from keras import layers

print("\n[3] Loading images (use only 2000 for speed)...")

def create_df(start_dir):
    import pandas as pd
    files = os.listdir(start_dir)
    filepaths, labels = [], []
    for f in files:
        if f.startswith('dog'):
            filepaths.append(os.path.join(start_dir, f))
            labels.append(1)  # dog=1
        elif f.startswith('cat'):
            filepaths.append(os.path.join(start_dir, f))
            labels.append(0)  # cat=0
    return pd.DataFrame({'filepath': filepaths[:2000], 'label': labels[:1000]+labels[:1000]})

df = create_df(train_dir)
print(f"Using {len(df)} images ({df['label'].sum()} dogs, {len(df)-df['label'].sum()} cats)")

# 4. Create data generators (with augmentation)
print("\n[4] Creating data generators...")
datagen = keras.preprocessing.image.ImageDataGenerator(
    rescale=1./255,
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    horizontal_flip=True,
    validation_split=0.2
)

train_gen = datagen.flow_from_dataframe(
    df, x_col='filepath', y_col='label',
    target_size=(150, 150), batch_size=32,
    subset='training', class_mode='raw'
)
val_gen = datagen.flow_from_dataframe(
    df, x_col='filepath', y_col='label',
    target_size=(150, 150), batch_size=32,
    subset='validation', class_mode='raw'
)

# 5. Build CNN Model
print("\n[5] Building CNN...")
model = keras.Sequential([
    layers.Conv2D(32, (3,3), activation='relu', input_shape=(150,150,3)),
    layers.MaxPooling2D(2,2),
    layers.Conv2D(64, (3,3), activation='relu'),
    layers.MaxPooling2D(2,2),
    layers.Conv2D(128, (3,3), activation='relu'),
    layers.MaxPooling2D(2,2),
    layers.Flatten(),
    layers.Dropout(0.5),
    layers.Dense(512, activation='relu'),
    layers.Dense(1, activation='sigmoid')  # binary output
])

model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)
print(model.summary())

# 6. Train
print("\n[6] Training (5 epochs for speed)...")
history = model.fit(
    train_gen,
    validation_data=val_gen,
    epochs=5,
    verbose=1
)

# 7. Evaluate
print(f"\n[7] Results:")
final_acc = history.history['val_accuracy'][-1]
print(f"Validation Accuracy: {final_acc:.4f} ({final_acc*100:.1f}%)")
print(f"Training Accuracy:   {history.history['accuracy'][-1]:.4f}")

# 8. Plot training history
plt.figure(figsize=(12, 4))
plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'], label='Train')
plt.plot(history.history['val_accuracy'], label='Val')
plt.title('Accuracy')
plt.legend()
plt.subplot(1, 2, 2)
plt.plot(history.history['loss'], label='Train')
plt.plot(history.history['val_loss'], label='Val')
plt.title('Loss')
plt.legend()
plt.tight_layout()
plt.savefig('08_training_history.png')
print("\n[8] Training plot saved to '08_training_history.png'")

# 9. Test with a custom image
print("\n[9] Quick prediction test:")
sample_dog = df[df['label'] == 1].iloc[0]['filepath']
sample_cat = df[df['label'] == 0].iloc[0]['filepath']

for img_path, expected in [(sample_dog, 'Dog'), (sample_cat, 'Cat')]:
    img = keras.preprocessing.image.load_img(img_path, target_size=(150, 150))
    img_arr = keras.preprocessing.image.img_to_array(img) / 255.0
    img_arr = np.expand_dims(img_arr, axis=0)
    pred = model.predict(img_arr, verbose=0)[0][0]
    result = 'Dog' if pred > 0.5 else 'Cat'
    print(f"  Expected: {expected}, Predicted: {result} (conf: {max(pred, 1-pred):.2%})")
