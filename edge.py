import cv2
# Open the video file
video_path = "/home/cyberdynamo/Downloads/curveVid.mp4"
cap = cv2.VideoCapture(video_path)

# Check if the video file is opened successfully
if not cap.isOpened():
    print("Error: Unable to open video file.")
    exit()

# Loop through each frame in the video
while True:
    # Read a frame from the video
    ret, frame = cap.read()

    # Check if the frame is successfully read
    if not ret:
        break

    # Apply Canny edge detection to the frame
    frame_canny = cv2.Canny(frame, 150, 200)

    # Display the edge-detected frame
    cv2.imshow("Canny Edge Detection", frame_canny)

    # Check for key press to exit (press 'q' to quit)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()
