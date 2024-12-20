import cv2
import sqlite3
from datetime import datetime

# Initialize face detector and recognizer
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()

def capture_attendance(user_id):
    # Start video capture
    cap = cv2.VideoCapture(0)
    attendance_shown = False  # Flag to ensure the message is shown only once
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            

            # Mark attendance if face detected
            if len(faces) > 0:
                if not attendance_shown:  # Show the message only once
                    mark_attendance(user_id)
                    attendance_shown = True  # Set the flag to True to stop showing the message
                break

        cv2.imshow('Capturing Attendance', frame)

        # Exit on pressing 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

def mark_attendance(user_id):
    # Get the current date and time
    now = datetime.now()
    date_time = now.strftime("%Y-%m-%d %H:%M:%S")
    date = now.strftime("%Y-%m-%d")
    
    # Connect to the database and insert attendance
    conn = sqlite3.connect('user.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM attendance WHERE user_id = ? AND date = ?", (user_id, date))
    attendance = cursor.fetchone()

    if attendance:
        print("Attendance already marked for today.")
    else:
        cursor.execute("INSERT INTO attendance (user_id, date, time) VALUES (?, ?, ?)", (user_id, date, date_time))
        conn.commit()
        print("Attendance marked successfully!")

    conn.close()
