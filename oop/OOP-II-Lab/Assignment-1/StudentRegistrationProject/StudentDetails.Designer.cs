using System.Windows.Forms;

namespace StudentRegistrationProject
{
    partial class StudentDetails
    {
        private System.ComponentModel.IContainer components = null;

        private Label labelName;
        private Label lblName;

        private Label labelRoll;
        private Label lblRoll;

        private Label labelRegID;
        private Label lblRegID;

        private Label labelSemester;
        private Label lblSemester;

        private Label labelBloodGroup;
        private Label lblBloodGroup;

        private Label labelGender;
        private Label lblGender;

        private PictureBox pictureBoxPhoto;

        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        private void InitializeComponent()
        {
            this.labelName = new Label();
            this.lblName = new Label();
            this.labelRoll = new Label();
            this.lblRoll = new Label();
            this.labelRegID = new Label();
            this.lblRegID = new Label();
            this.labelSemester = new Label();
            this.lblSemester = new Label();
            this.labelBloodGroup = new Label();
            this.lblBloodGroup = new Label();
            this.labelGender = new Label();
            this.lblGender = new Label();
            this.pictureBoxPhoto = new PictureBox();

            ((System.ComponentModel.ISupportInitialize)(this.pictureBoxPhoto)).BeginInit();
            this.SuspendLayout();

            // StudentDetails properties
            this.ClientSize = new System.Drawing.Size(600, 300);
            this.Name = "StudentDetails";
            this.Text = "Student Details";

            // labelName
            this.labelName.AutoSize = true;
            this.labelName.Location = new System.Drawing.Point(30, 30);
            this.labelName.Name = "labelName";
            this.labelName.Text = "Name:";

            // lblName
            this.lblName.AutoSize = true;
            this.lblName.Location = new System.Drawing.Point(100, 30);
            this.lblName.Name = "lblName";
            this.lblName.Text = "-";

            // labelRoll
            this.labelRoll.AutoSize = true;
            this.labelRoll.Location = new System.Drawing.Point(30, 60);
            this.labelRoll.Name = "labelRoll";
            this.labelRoll.Text = "Roll:";

            // lblRoll
            this.lblRoll.AutoSize = true;
            this.lblRoll.Location = new System.Drawing.Point(100, 60);
            this.lblRoll.Name = "lblRoll";
            this.lblRoll.Text = "-";

            // labelRegID
            this.labelRegID.AutoSize = true;
            this.labelRegID.Location = new System.Drawing.Point(30, 90);
            this.labelRegID.Name = "labelRegID";
            this.labelRegID.Text = "Reg. ID:";

            // lblRegID
            this.lblRegID.AutoSize = true;
            this.lblRegID.Location = new System.Drawing.Point(100, 90);
            this.lblRegID.Name = "lblRegID";
            this.lblRegID.Text = "-";

            // labelSemester
            this.labelSemester.AutoSize = true;
            this.labelSemester.Location = new System.Drawing.Point(30, 120);
            this.labelSemester.Name = "labelSemester";
            this.labelSemester.Text = "Semester:";

            // lblSemester
            this.lblSemester.AutoSize = true;
            this.lblSemester.Location = new System.Drawing.Point(100, 120);
            this.lblSemester.Name = "lblSemester";
            this.lblSemester.Text = "-";

            // labelBloodGroup
            this.labelBloodGroup.AutoSize = true;
            this.labelBloodGroup.Location = new System.Drawing.Point(30, 150);
            this.labelBloodGroup.Name = "labelBloodGroup";
            this.labelBloodGroup.Text = "Blood Group:";

            // lblBloodGroup
            this.lblBloodGroup.AutoSize = true;
            this.lblBloodGroup.Location = new System.Drawing.Point(100, 150);
            this.lblBloodGroup.Name = "lblBloodGroup";
            this.lblBloodGroup.Text = "-";

            // labelGender
            this.labelGender.AutoSize = true;
            this.labelGender.Location = new System.Drawing.Point(30, 180);
            this.labelGender.Name = "labelGender";
            this.labelGender.Text = "Gender:";

            // lblGender
            this.lblGender.AutoSize = true;
            this.lblGender.Location = new System.Drawing.Point(100, 180);
            this.lblGender.Name = "lblGender";
            this.lblGender.Text = "-";

            // pictureBoxPhoto
            this.pictureBoxPhoto.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.pictureBoxPhoto.Location = new System.Drawing.Point(300, 30);
            this.pictureBoxPhoto.Name = "pictureBoxPhoto";
            this.pictureBoxPhoto.Size = new System.Drawing.Size(150, 150);
            this.pictureBoxPhoto.SizeMode = PictureBoxSizeMode.Zoom;

            // Add controls to StudentDetails
            this.Controls.Add(this.labelName);
            this.Controls.Add(this.lblName);
            this.Controls.Add(this.labelRoll);
            this.Controls.Add(this.lblRoll);
            this.Controls.Add(this.labelRegID);
            this.Controls.Add(this.lblRegID);
            this.Controls.Add(this.labelSemester);
            this.Controls.Add(this.lblSemester);
            this.Controls.Add(this.labelBloodGroup);
            this.Controls.Add(this.lblBloodGroup);
            this.Controls.Add(this.labelGender);
            this.Controls.Add(this.lblGender);
            this.Controls.Add(this.pictureBoxPhoto);

            ((System.ComponentModel.ISupportInitialize)(this.pictureBoxPhoto)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();
        }
    }
}