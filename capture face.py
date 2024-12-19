import cv2

def capture_image(window_name, image_name):
    # Open a connection to the webcam
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    print(f"Press 's' to capture {image_name}, or 'q' to quit.")

pture_face.py = import cv2 

def capture_image(window_name, image_name):
    # Open a connection to the webcam
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    print(f"Press 's' to capture {image_name}, or 'q' to quit.")

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        if not ret:
            print("Error: Failed to capture image.")
            break

        # Display the resulting frame
        cv2.imshow(window_name, frame)

        # Wait for the user to press 's' to save the image or 'q' to quit
        key = cv2.waitKey(1) & 0xFF

        if key == ord('s'):
            # Save the captured image
            cv2.imwrite(f"{image_name}.jpg", frame)
            print(f"{image_name} captured and saved as {image_name}.jpg")
            break
        elif key == ord('q'):
            print("Quitting without saving.")
            break

    # Release the webcam and close windows
    cap.release()
    cv2.destroyAllWindows()

# Capture face image
capture_image("Face Capture", "face_image")

# Capture ID proof image
capture_image("ID Proof Capture", "id_image")