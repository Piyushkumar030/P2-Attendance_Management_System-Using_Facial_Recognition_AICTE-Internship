import cv2
import numpy as np
from PIL import Image
import os

# Paths
dataset_path = "dataset"
trainer_path = "trainer"
trainer_file = os.path.join(trainer_path, "trainer.yml")

# Create `trainer` folder if not exists
if not os.path.exists(trainer_path):
    os.makedirs(trainer_path)

# Initialize recognizer
recognizer = cv2.face.LBPHFaceRecognizer_create()
detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

def get_images_and_labels(path):
    image_paths = [os.path.join(path, f) for f in os.listdir(path) if f.endswith(".jpg") or f.endswith(".png")]
    face_samples = []
    ids = []

    for image_path in image_paths:
        img = Image.open(image_path).convert('L')  # Convert to grayscale
        img_numpy = np.array(img, 'uint8')
        id = int(os.path.split(image_path)[-1].split(".")[1])  # Extract ID from filename
        faces = detector.detectMultiScale(img_numpy)

        for (x, y, w, h) in faces:
            face_samples.append(img_numpy[y:y + h, x:x + w])
            ids.append(id)

    return face_samples, ids

print("\n[INFO] Training faces. This may take a few seconds...")
faces, ids = get_images_and_labels(dataset_path)
recognizer.train(faces, np.array(ids))

# Save the trained model
recognizer.write(trainer_file)
print(f"[INFO] {len(np.unique(ids))} faces trained. Model saved at '{trainer_file}'.")
