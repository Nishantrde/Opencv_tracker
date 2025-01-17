import os
import cv2 as cv

# Get paths
script_dir = os.path.dirname(__file__)
video_path = os.path.join(script_dir, 'vid1/avng.mp4')
output_dir = os.path.join(script_dir, 'vid2')
os.makedirs(output_dir, exist_ok=True)

# Initialize video capture
cap = cv.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Cannot open video file.")
    exit()

# Select the tracking region
success, img = cap.read()
if not success:
    print("Error: Cannot read video.")
    exit()

bbox = cv.selectROI("Select ROI", img, False)
cv.destroyWindow("Select ROI")

# Initialize tracker
tracker = cv.legacy.TrackerMOSSE_create()
tracker.init(img, bbox)

# Define the codec and create VideoWriter object
fourcc = cv.VideoWriter_fourcc(*'mp4v')
output_path = os.path.join(script_dir, 'output.mp4')
out = cv.VideoWriter(output_path, fourcc, 20.0, (img.shape[1], img.shape[0]))

frame_count = 0
while True:
    success, img = cap.read()
    if not success:
        break

    # Update the tracker
    tracking_success, bbox = tracker.update(img)

    if tracking_success:
        # Extract bounding box coordinates
        x, y, w, h = [int(v) for v in bbox]

        # Crop the image to the bounding box
        cropped_frame = img[y:y + h, x:x + w]

        # Save cropped region
        cv.imwrite(os.path.join(output_dir, f"frame_{frame_count}.jpg"), cropped_frame)

        # Display the cropped frame
        cv.imshow("Tracking", cropped_frame)

    else:
        cv.putText(img, "Lost Track", (75, 50), cv.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        cv.imshow("Tracking", img)

    # Show FPS on original frame
    fps = cap.get(cv.CAP_PROP_FPS)
    cv.putText(img, f"FPS: {int(fps)}", (75, 20), cv.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

    # Write original frame to video
    out.write(img)

    frame_count += 1
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
out.release()
cv.destroyAllWindows()
