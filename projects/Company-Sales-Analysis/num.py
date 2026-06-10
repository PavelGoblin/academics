import numpy as np

months = np.array(["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"])
sales = []

print("Enter sales (in $1000s) for each month:")

for month in months:
    value = float(input(f"{month}: "))
    sales.append(value)

sales = np.array(sales)

print("\n---Company Sales Analysis---")
print("Total Sales of the Year:", np.sum(sales), "$")
print("Average Monthly Sales:", np.mean(sales), "$")
print("Highest Sales:", np.max(sales), "$")
print("Lowest Sales:", np.min(sales), "$")

best_month = months[np.argmax(sales)]
worst_month = months[np.argmin(sales)]

print("Best Month:", best_month)
print("Worst Month:", worst_month)

above_avg = months[sales > np.mean(sales)]
below_avg = months[sales < np.mean(sales)]

print("Above Average Months:", above_avg)
print("Below Average Months:", below_avg)