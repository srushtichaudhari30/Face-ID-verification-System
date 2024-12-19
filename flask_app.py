from flask import Flask, render_template, request, redirect, url_for
import cv2
import os
import face_recognition
import numpy as np

app = Flask(__name__)

# Create a folder for uploads
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Function to capture image from webcam
def capture_image(window_name, image_name):
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return
    print(f"Press 's' to capture {image_name}, or 'q' to quit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to capture image.")
            break
        cv2.imshow(window_name, frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('s'):
            cv2.imwrite(f"{image_name}.jpg", frame)
            print(f"{image_name} captured and saved as {image_name}.jpg")
            break
        elif key == ord('q'):
            print("Quitting without saving.")
            break
    cap.release()
    cv2.destroyAllWindows()

# Route for capturing the face using the webcam
@app.route('/capture_face')
def capture_face():
    capture_image("Face Capture", "uploads/face_image")
    return redirect(url_for('compare'))

# Home route: Form to upload ID proof
@app.route('/')
def upload_id():
    return render_template('index.html')

# Function to compare face images
def compare_faces(known_image_path, unknown_image_path):
    # Load the images
    known_image = face_recognition.load_image_file(known_image_path)
    unknown_image = face_recognition.load_image_file(unknown_image_path)

    # Get the face encodings
    known_encodings = face_recognition.face_encodings(known_image)
    unknown_encodings = face_recognition.face_encodings(unknown_image)

    # Error handling if no face is detected
    if len(known_encodings) == 0 or len(unknown_encodings) == 0:
        return 'No face detected in one or both images.'

    # Compare the faces
    results = face_recognition.compare_faces([known_encodings[0]], unknown_encodings[0])

    return results[0]  # True if the faces match, False otherwise

# Route to handle file upload and face comparison
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    if file:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], "id_image.jpg")
        file.save(file_path)
        return redirect(url_for('capture_face'))  # Redirect to capture face

# Route for comparing the captured face and uploaded ID proof
@app.route('/compare', methods=['GET', 'POST'])
def compare():
    if request.method == 'GET':
        # Render the comparison page
        return render_template('compare.html')

    elif request.method == 'POST':
        # Perform the comparison logic here
        captured_face_path = "uploads/face_image.jpg"  # Path where the captured face is saved
        id_proof_path = "uploads/id_image.jpg"  # Path where the uploaded ID proof is saved

        match = compare_faces(id_proof_path, captured_face_path)

        if isinstance(match, str):
            # Return error message if face detection failed with error styling
            return render_template('compare.html', result_message=match, result_class="error")

        if match:
            # Return success message if faces match with success styling
            return render_template('compare.html', result_message="ID proof is valid: Face matches!", result_class="success")
        else:
            # Return failure message if faces do not match with error styling
            return render_template('compare.html', result_message="ID proof is invalid: Face does not match!", result_class="error")

if __name__ == '__main__':
    app.run(debug=True)
