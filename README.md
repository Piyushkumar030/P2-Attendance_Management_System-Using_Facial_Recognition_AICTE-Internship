# Attendance_Management_System-Using_Facial_Recognition_AICTE-Internship

## Overview of the project
The "Attendance Management System" is a Python-driven application that automates attendance tracking using facial recognition. With OpenCV-python powering face detection and recognition, and SQLite managing the database for user and attendance records, the system ensures reliability and hold good functionality. A user-friendly interface built with Tkinter enhances accessibility.Its  features include capturing training images, real-time recognition, and streamlined attendance management.

---


* Problem
Taking attendance manually can be slow, full of mistakes, and not always reliable. In schools, offices, or events, it often causes delays and can be easily misused.

* Challenges
Sometimes people forget to mark attendance, or someone might mark it for someone else. This leads to incomplete or incorrect records, causing confusion and problems later.

* Solution
The Attendance Management System uses face recognition technology to take attendance quickly and accurately. It scans faces through a camera, identifies the person, and securely saves the attendance in an SQLite database. This saves time, avoids errors, and makes the process smooth and trustworthy.

---

## Features

- **User Registration & Login**: Secure registration and login with username and password.
- **Face Recognition for Attendance**: Automatic attendance marking through facial recognition, reducing human intervention.
- **Attendance History**: Allows users to check their previous attendance logs with date and time.
- **Database Integration**: All user data and attendance logs are stored in an SQLite database for easy management and retrieval at anytime.

---

## Technologies Used

- **OpenCV**: A computer vision library used to detect and recognize faces in real-time.
  - Install with: `pip install opencv-python`
- **SQLite**: A lightweight, self-contained database used to store user details and attendance records.
- **Tkinter**: Used for creating a simple and interactive graphical user interface (GUI).
  - Install with: `pip install tk`
- **Pillow**: A Python Imaging Library (PIL) fork used for processing and handling images (e.g., resizing).
  - Install with: `pip install pillow`
- **NumPy**: Provides support for large multi-dimensional arrays and matrices, used with OpenCV for face recognition.
  - Install with:
    `pip install numpy`

---


## Installation Guide

Follow the steps below to run the project on your local machine:

### 1. Clone the Repository
```bash
git clone P2-Attendance_Management_System-Using_Facial_Recognition_AICTE-Internship.git
cd P2-Attendance_Management_System-Using_Facial_Recognition_AICTE-Internship
```

### 2. Install Required Packages
Ensure Python is installed on your system, then install the necessary dependencies using the command:
```bash
pip install -r requirements.txt
```

### 3. Set Up SQLite Database
- Create a SQLite database(here, user.db) to store attendance records.
- Update the database connection details in the code as needed.

### 4. Download Haarcascade
Download the Haarcascade XML file for face detection from the [OpenCV GitHub repository](https://github.com/opencv/opencv) and place it in the project directory.

---


## Working

### 1. Capture Images
- Run `main_gui.py` to open the GUI and it is the main file of the project.
- Enter the Username and Password for registration.
- Then Click on Login Button.
- After that , window for marking attendance using facial identification opens.
- Camera opens, and images are captured.
- Click 'ctrl+q' to finish capturing images.

### 2. Train the Model
- After capturing images, run `train_model.py` in cmd to train the face recognition model.

### 3. Automatic Attendance
- Select `Mark Today's Attendance` to automatically mark attendance for the day, a message can be seen in cmd(terminal).

### 5. View History
- Access the `Attendance History` button to view the details of attendance.

---


## Directory Structure
```plaintext

AttendanceManagementSystem/
├── faces/                          # Folder where user images for training are stored
├── trainer.yml                     # Trained face recognition model file
├── user.db                         # SQLite database for user data and attendance logs
├── haarcascade_frontalface_default.xml  # Haarcascade file for face detection
├── main_gui.py                     # Main application file that runs the GUI
├── attendance_capture.py           # The script that handles capturing attendance using the webcam and the facial recognition model.
├── attendance_create.py            # Used for creating new user entries in the system (such as username, password, and storing their face images).
├── train_model.py                  # Script to train the face recognition model
├── delete_faces.py                 # Script to delete a user's face data
└── README.md                       # This guidance file

```


---

## Contributing
This version still maintains the friendly and encouraging tone while providing the same clear steps for contributing, feel free to fork the repository and submit a pull request.

---


---

## Acknowledgments
Special thanks to the following:
- **OpenCV** for face detection and recognition functionalities.
- **Tkinter** for GUI development.
- **NumPy** and **Pandas** for data manipulation and analysis.
- **MySQL** for database management.

---


### Step-by-Step Usage in the README:

1. **Introduction of the Problem**: Describes the problem of manual attendance systems and how it can lead to inefficiency and errors.
2. **Solution**: Shows how the facial recognition system solves this problem with automated attendance marking.
3. **Technologies and Libraries**: Explains the libraries and technologies used, including installation steps.
4. **Setup Instructions**: Guides the user through each step of the installation process.
5. **Project Structure**: Displays the organization of the project files to help the user navigate through them.
6. **Detailed Working Explanation**: Describes how the system functions, from registration to face recognition and attendance logging.
7. **Contact Information**: Provides a way for users to contact you for help.

This **README.md** follows a clear, detailed, and structured approach, allowing someone unfamiliar with your project to set it up and run it without any problems.


For any questions or issues, feel free to contact **[deypiyushkumar2004@gmail.com]**.

HAPPY CODING 🎉
