#train model .py

import cv2
import os
import numpy as np
from PIL import Image
import sqlite3

# Initialize the face recognizer
recognizer = cv2.face.LBPHFaceRecognizer_create()

# Directory containing the dataset (images)
dataset_dir = 'faces/'

def train_face_recognizer():
    # Create lists to hold the image data and labels
    images = []
    labels = []

    # Fetch user data from the database
    conn = sqlite3.connect('user.db')
    cursor = conn.cursor()
    cursor.execute("SELECT user_id FROM users")
    users = cursor.fetchall()
    conn.close()

    for user in users:
        user_id = user[0]
        user_images_path = os.path.join(dataset_dir, str(user_id))

        # Check if the user's folder exists
        if not os.path.exists(user_images_path):
            continue  # Skip if the folder for the user doesn't exist

        # Collect images for the given user
        for filename in os.listdir(user_images_path):
            file_path = os.path.join(user_images_path, filename)

            # Check if the file is an image (e.g., ends with .jpg, .png)
            if filename.endswith('.jpg') or filename.endswith('.png'):
                img = Image.open(file_path).convert('L')  # Convert to grayscale
                img_np = np.array(img, 'uint8')  # Convert to numpy array

                images.append(img_np)  # Add image to the list
                labels.append(user_id)  # Add the corresponding user ID to the list

    # Train the recognizer
    recognizer.train(images, np.array(labels))
    recognizer.save('trainer/trainer.yml')  # Save the trained model

if __name__ == "__main__":
    train_face_recognizer()
    print("Training complete and model saved.")
