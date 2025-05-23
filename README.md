# Virtual Mouse using Hand Gestures

Control your computer mouse using hand gestures via your webcam — no physical mouse needed!

![screenshot](screenshot.png)

---

## Features

- Real-time hand detection with MediaPipe
- Move mouse with index finger
- Left-click gesture (index + thumb)
- Take screenshot gesture (middle + thumb)
- Works on any screen resolution
- Fast, lightweight & easy to use

---

## Project Structure

Virtual-Mouse

- main.py # Main file to run the app
- hand_tracking.py # Hand detection module
- gesture_control.py # Gesture recognition & mouse control
- screenshot.png # Saved screenshot
- README.md # Project documentation


---

## Tech Stack

- **Python**
- **OpenCV** – for video capture and image processing  
- **MediaPipe** – for hand tracking  
- **PyAutoGUI** – to control mouse & take screenshots  
- **NumPy** – for distance calculation

---

## Installation

```bash
# Clone the repository
git clone https://github.com/vikas-tikapur/Virtual-Mouse.git
cd Virtual-Mouse

# (Optional) create virtual environment
python -m venv .venv
.venv\Scripts\activate    # On Windows

# Install required packages
pip install opencv-python mediapipe pyautogui numpy
``` 
---
## Run the Project
- python main.py

- Press q to quit the program.

---
## How It Works 
| Gesture           | Action          |
| ----------------- | --------------- |
|  Index Finger   | Move the mouse  |
|  Index + Thumb  | Left Click      |
|  Middle + Thumb | Take Screenshot |

---
## Notes
- Ensure good lighting for accurate hand detection.

- Screenshot will be saved as screenshot.png in the project folder.

- You can adjust click/screenshot sensitivity in gesture_control.py

---
## Author
- Vikas Mishra
- 🔗 GitHub: vikas-tikapur

---
