import cv2
import os
from natsort import natsorted  # Ensure proper sorting of filenames with numbers


def create_video_from_images(image_folder, output_video_path, fps=24):
    # Check if the image folder exists
    if not os.path.exists(image_folder):
        print(f"Error: Folder '{image_folder}' does not exist.")
        return

    # Get the list of image files in the folder
    images = [img for img in os.listdir(image_folder) if img.endswith((".jpg", ".png"))]
    if not images:
        print(f"No valid image files (.jpg, .png) found in '{image_folder}'.")
        return

    # Sort the images naturally (handles filenames with numbers correctly)
    images = natsorted(images)

    # Read the first image to determine video dimensions
    first_image_path = os.path.join(image_folder, images[0])
    first_frame = cv2.imread(first_image_path)
    if first_frame is None:
        print(f"Error reading the first image: {first_image_path}")
        return
    height, width, _ = first_frame.shape

    # Create the VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Use 'XVID' for .avi files
    out = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))
    print(f"Video will be saved to: {output_video_path}")
    print(f"Video resolution: {width}x{height}, FPS: {fps}")

    # Write images to the video
    for image in images:
        img_path = os.path.join(image_folder, image)
        frame = cv2.imread(img_path)
        if frame is None:
            print(f"Error reading image: {img_path}. Skipping.")
            continue
        if frame.shape[:2] != (height, width):
            print(f"Resizing image: {img_path} to match video dimensions.")
            frame = cv2.resize(frame, (width, height))
        out.write(frame)
        print(f"Added image to video: {img_path}")

    # Release the VideoWriter object
    out.release()
    print("Video created successfully!")


# Example usage:
if __name__ == "__main__":
    # Set the folder containing images and the output video path
    script_dir = os.path.dirname(__file__)
    image_folder = os.path.join(script_dir, 'vid2')  # Update 'vid2' with your folder name
    output_video_path = os.path.join(script_dir, "output_video_tracker.mp4")

    # Create video from images
    create_video_from_images(image_folder, output_video_path)
