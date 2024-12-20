import cv2
import os
import numpy as np

def train_face_recognizer():
    faces = []
    labels = []
    label_map = {}

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    # Load the images
    image_paths = [os.path.join('faces', f) for f in os.listdir('faces') if f.endswith('.jpg') or f.endswith('.png')]
    
    for image_path in image_paths:
        img = cv2.imread(image_path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces_detected = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
        
        for (x, y, w, h) in faces_detected:
            face = gray[y:y+h, x:x+w]
            label = int(image_path.split('_')[0])  # Extract label from filename
            faces.append(face)
            labels.append(label)
            label_map[label] = image_path.split('_')[0]

    face_recognizer = cv2.face.LBPHFaceRecognizer_create()
    face_recognizer.train(faces, np.array(labels))
    face_recognizer.save('trainer.yml')

    print(f"Training complete! Model saved as 'trainer.yml'")
    return label_map

if __name__ == "__main__":
    label_map = train_face_recognizer()
    print("Label Map:", label_map)
