# Face-ID-verification-System
A Face ID Verification System is a biometric authentication method that uses facial recognition technology to verify a person's identity. It works by capturing, analyzing, and comparing the facial features of an individual with a stored reference image (such as a photo from an ID proof) to determine if there is a match. This type of system provides an added layer of security, ensuring that the person attempting to access a system or perform a sensitive action is the legitimate user.

## Features

- **Capture Face from Webcam**: Captures a user's face using a webcam.
- **Upload ID Proof**: Allows the user to upload an image of their ID proof.
- **Face Comparison**: Compares the captured face with the uploaded ID proof to validate identity.
- **Result Display**: Shows whether the ID proof is valid or invalid, with styling to indicate success or failure.

## Tech Stack

- **Python**: Programming language used for backend logic.
- **Flask**: Web framework for handling HTTP requests and rendering HTML templates.
- **OpenCV**: Used for webcam access and capturing face images.
- **face_recognition**: Python library to perform face detection and comparison.
- **HTML/CSS**: For the frontend layout and styling.
