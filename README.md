# Video Tracking and Cropping Script
![Tracking Video Demo](https://res.cloudinary.com/dwfdyavop/video/upload/v1737125905/marvel_asemble_xrdwgy.mp4)
This project is a Python script that uses OpenCV to track a region of interest (ROI) in a video, crop the tracked region frame-by-frame, and save both the cropped images and the annotated video output. It also supports selecting the initial ROI interactively.

## Features

- Select and track a region of interest (ROI) in a video.
- Save cropped frames of the tracked ROI as images.
- Save the annotated video with tracking information.
- Real-time display of tracking and FPS information.

## Prerequisites

- Python 3.x
- OpenCV (Ensure the `opencv-contrib-python` package is installed for legacy tracker support)
- A valid video file (`mp4` format recommended).

## Installation

1. Clone this repository:
   ```bash
   git clone <repository_url>
   cd <repository_name>
   ```

2. Install the required dependencies:
   ```bash
   pip install opencv-contrib-python
   ```

3. Place the input video file in the `vid1` folder. Ensure the file is named `avng.mp4` or update the script with your video filename.

## Usage

1. Run the script:
   ```bash
   python script.py
   ```

2. Select the ROI by dragging a rectangle over the desired region in the displayed frame. Press `Enter` or `Space` to confirm your selection.

3. The script will:
   - Track the selected ROI throughout the video.
   - Save cropped frames of the tracked region to the `vid2` folder.
   - Save the annotated video output as `output.mp4` in the root directory.

4. Press `q` during playback to exit the tracking loop early.

## File Structure

```
project/
|
|-- script.py        # Main Python script
|-- vid1/            # Input video folder
|   |-- avng.mp4     # Input video file
|
|-- vid2/            # Folder for cropped frames
|
|-- output.mp4       # Annotated output video
|
|-- README.md        # Project documentation
```

## Notes

- Ensure the input video is placed in the correct directory (`vid1`) before running the script.
- The `TrackerMOSSE` tracker is used for lightweight tracking. For more robust tracking, consider using other trackers like `TrackerCSRT`.

## Troubleshooting

1. **Error: Cannot open video file**
   - Ensure the input video file exists and the path is correct.

2. **Error: Cannot read video**
   - Check the video format and compatibility with OpenCV.

3. **Tracking issues**
   - If the tracker loses track frequently, try selecting a clearer ROI or use a more robust tracker.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contribution

Contributions, issues, and feature requests are welcome! Feel free to fork the repository and submit pull requests.
