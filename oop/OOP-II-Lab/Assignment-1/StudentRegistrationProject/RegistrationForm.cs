using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace StudentRegistrationProject
{
    public partial class RegistrationForm : Form
    {
        // A variable to store the selected photo
        private Image selectedPhoto;

        public RegistrationForm()
        {
            InitializeComponent();
        }

        private void RegistrationForm_Load(object sender, EventArgs e)
        {
            // Optional: Pre-populate the Blood Group ComboBox
            comboBloodGroup.Items.Add("A(+ve)");
            comboBloodGroup.Items.Add("A(-ve)");
            comboBloodGroup.Items.Add("B(+ve)");
            comboBloodGroup.Items.Add("B(-ve)");
            comboBloodGroup.Items.Add("AB(+ve)");
            comboBloodGroup.Items.Add("AB(-ve)");
            comboBloodGroup.Items.Add("O(+ve)");
            comboBloodGroup.Items.Add("O(-ve)");

            // Set default selections, etc.
            radioMale.Checked = true;  // default gender
        }

        private void btnUpload_Click(object sender, EventArgs e)
        {
            // Use OpenFileDialog to choose an image
            OpenFileDialog ofd = new OpenFileDialog();
            ofd.Filter = "Image Files|*.jpg;*.jpeg;*.png;*.bmp";
            if (ofd.ShowDialog() == DialogResult.OK)
            {
                selectedPhoto = Image.FromFile(ofd.FileName);
                pictureBox1.Image = selectedPhoto;
            }
        }

        private void btnReset_Click(object sender, EventArgs e)
        {
            // Clear all fields
            txtName.Clear();
            txtRoll.Clear();
            txtRegID.Clear();
            txtSemester.Clear();
            comboBloodGroup.SelectedIndex = -1;
            radioMale.Checked = true;
            pictureBox1.Image = null;
            selectedPhoto = null;
        }

        private void btnSubmit_Click(object sender, EventArgs e)
        {
            // Gather data from fields
            string name = txtName.Text;
            string roll = txtRoll.Text;
            string regID = txtRegID.Text;
            string semester = txtSemester.Text;
            string bloodGroup = comboBloodGroup.SelectedIndex >= 0
                ? comboBloodGroup.SelectedItem.ToString()
                : "";
            string gender = radioMale.Checked ? "Male" : "Female";

            // Create StudentDetails and pass data
            StudentDetails StudentDetails = new StudentDetails(name, roll, regID, semester, bloodGroup, gender, selectedPhoto);
            StudentDetails.Show();
        }
    }
}