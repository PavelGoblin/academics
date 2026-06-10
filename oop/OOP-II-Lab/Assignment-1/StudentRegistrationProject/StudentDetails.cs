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
    public partial class StudentDetails : Form
    {
        public StudentDetails(string name, string roll, string regID, string semester,
                     string bloodGroup, string gender, Image photo)
        {
            InitializeComponent();

            // Display data on StudentDetails’s controls
            lblName.Text = name;
            lblRoll.Text = roll;
            lblRegID.Text = regID;
            lblSemester.Text = semester;
            lblBloodGroup.Text = bloodGroup;
            lblGender.Text = gender;

            if (photo != null)
                pictureBoxPhoto.Image = photo;
        }
    }
}