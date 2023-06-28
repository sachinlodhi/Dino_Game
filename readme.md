
# Automated Dino Game in Chrome using OpenCV

This project utilizes OpenCV, a popular computer vision library, to automate the Dino game in Chrome. The script captures screenshots of the game window, processes the images using computer vision techniques, and simulates keypresses to control the Dino character.

## Prerequisites

Before running the script, ensure you have the following dependencies installed:

- Python 3.x
- OpenCV
- NumPy
- PIL (Python Imaging Library)
- PyAutoGUI

You can install these dependencies using pip, the Python package manager. Run the following command to install them:

```
pip install opencv-python numpy pillow pyautogui
```

## Getting Started

1. Clone the repository or download the script file to your local machine.

2. Adjust the parameters in the script according to your screen dimension and the position of the browser window. Look for the line that captures the screenshot and modify the `bbox` values to match your game window position and size:

   ```python
   pic = ImageGrab.grab(bbox=(182, 332, 280, 490))  # Adjust the values according to your screen dimension and game window position
   ```

3. Update the `temp_dir` variable to specify the directory where you want to save the screenshots:

   ```python
   temp_dir = "/path/to/screenshots/directory/"
   ```

4. Run the script using the following command:

   ```
   python dino_game.py
   ```

5. Switch to the Chrome browser with the Dino game and let the script automatically play the game for you.

## How It Works

1. The script captures screenshots of the game window using the `ImageGrab.grab()` function from the PIL library.

2. It converts the RGB image into the BGR color space required by OpenCV.

3. The captured image is then thresholded using the `cv2.threshold()` function to create a binary image, isolating the Dino character from the background.

4. The binary image is split into upper and lower sections to detect obstacles and empty spaces.

5. Based on the presence of obstacles, the script simulates keypresses using `pyautogui.press()` to make the Dino jump or crouch.

6. The processed images of the upper and lower sections are displayed in separate OpenCV windows for visual debugging.

7. The script runs in an infinite loop until you press the 'q' key to quit.

## Customization

You can customize the script further to enhance its performance or add additional features. Some possible improvements include:

- Adjusting the threshold values (`127` and `255`) to optimize obstacle detection based on your specific game environment.
- Implementing more sophisticated image processing techniques, such as edge detection or contour analysis, to improve obstacle detection accuracy.
- Implementing a scoring mechanism to keep track of the Dino's performance and display it on the screen or save it to a file.
- Implementing a machine learning algorithm to train a model that can predict the optimal timing for jumps and crouches.

## Limitations

It's important to note that automating browser games using screen capture and image processing techniques might not be as reliable or efficient as other methods, such as using browser automation tools or game-specific APIs. The accuracy and responsiveness of the script may vary depending on factors like screen resolution, game speed, and system performance.

## Disclaimer

Automating browser games using scripts or bots may violate the terms of service of the game or website. Ensure you have the necessary permissions or use the script responsibly for personal use only.

## License

This project is licensed under the [MIT License](LICENSE)