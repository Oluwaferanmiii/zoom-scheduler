# Zoom Scheduler Script

This Python script automates the process of starting a Zoom meeting by opening the Zoom application, locating the "Join" button, entering the meeting ID, and submitting the passcode. It utilizes `pyautogui` for mouse and keyboard automation, and `subprocess` for launching Zoom.

## Features

- Automatically opens Zoom and joins a scheduled meeting.
- Locates the "Join" button using a screenshot template.
- Inputs the meeting ID and passcode automatically.

## Prerequisites

1. Python 3.x installed on your system.
2. Required Python packages:
   - `pyautogui`
   - `pillow`
3. An image file (`join_button.png`) to locate the "Join" button on the Zoom interface.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Oluwaferanmiii/zoom-scheduler.git
   cd zoom-scheduler

2. **Install the necessary Python packages**: 
You can install the required Python packages using pip:

'''bash
pip install pyautogui pillow

3. **Save the "Join" Button Image**: 
Place an image of the Zoom "Join" button (join_button.png) in the appropriate folder path specified in the script.

## How to Run the Script
1. **Edit the Script**:
.Ensure that the zoom_path variable points to the correct location of the Zoom executable on your machine.
.Adjust the coordinates for the mouse movement or any timings as necessary based on your system's speed.

2. **Run the Script: Open the command prompt or terminal and run the Python script**:
'''bash
python zoom_scheduler.py

The script will:
.Open Zoom.
.Look for the "Join" button on the screen.
.Automatically click the "Join" button, input the meeting ID, and passcode.