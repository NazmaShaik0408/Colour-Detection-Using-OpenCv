import cv2
import numpy as np

# Open webcam
cap = cv2.VideoCapture(0)

while True:

    # Capture frame
    ret, frame = cap.read()

    if not ret:
        print("Could not access webcam")
        break

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # --------------------------------------------------
    # Define HSV ranges for different colors
    # --------------------------------------------------

    colors = {

        "Red": [
            (np.array([0, 100, 100]), np.array([10, 255, 255])),
            (np.array([170, 100, 100]), np.array([180, 255, 255]))
        ],

        "Green": [
            (np.array([35, 50, 50]), np.array([85, 255, 255]))
        ],

        "Blue": [
            (np.array([90, 50, 50]), np.array([130, 255, 255]))
        ],

        "Sky Blue": [
            (np.array([80, 50, 50]), np.array([100, 255, 255]))
        ],

        "Pink": [
            (np.array([140, 50, 50]), np.array([175, 255, 255]))
        ],

        "White": [
            (np.array([0, 0, 180]), np.array([180, 60, 255]))
        ]
    }

    # --------------------------------------------------
    # Detect each color
    # --------------------------------------------------

    for color_name, ranges in colors.items():

        # Create empty mask
        mask = np.zeros(hsv.shape[:2], dtype=np.uint8)

        # Create mask for each HSV range
        for lower, upper in ranges:
            color_mask = cv2.inRange(hsv, lower, upper)
            mask = cv2.bitwise_or(mask, color_mask)

        # Remove small noise
        kernel = np.ones((5, 5), np.uint8)

        mask = cv2.morphologyEx(
            mask,
            cv2.MORPH_OPEN,
            kernel
        )

        mask = cv2.morphologyEx(
            mask,
            cv2.MORPH_CLOSE,
            kernel
        )

        # Find contours
        contours, _ = cv2.findContours(
            mask,
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE
        )

        # Process detected objects
        for contour in contours:

            # Calculate contour area
            area = cv2.contourArea(contour)

            # Ignore very small objects/noise
            if area < 500:
                continue

            # Get bounding rectangle
            x, y, w, h = cv2.boundingRect(contour)

            # Draw bounding box
            cv2.rectangle(
                frame,
                (x, y),
                (x + w, y + h),
                (0, 255, 0),
                2
            )

            # Display color name
            cv2.putText(
                frame,
                color_name,
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 255, 0),
                2
            )

    # Display webcam frame
    cv2.imshow("Real-Time Color Detection", frame)

    # Press Q to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# Release webcam
cap.release()

# Close all OpenCV windows
cv2.destroyAllWindows()
