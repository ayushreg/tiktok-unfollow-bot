# TikTok Unfollow Bot

A Python automation bot that helps you unfollow users on TikTok who don't follow you back. On TikTok, when someone you follow also follows you, you are considered "friends." This bot will automatically unfollow anyone who is not a friend, helping you clean up your following list.

## Features

- Automatically detects and clicks unfollow buttons on TikTok
- Scrolls through your following list automatically
- Can be easily modified to unfollow everyone in your following list
- Uses image recognition to find unfollow buttons

## Requirements

- Python 3.x
- `pyautogui` library
- A screenshot of the "Follow" button saved as `follow.png` in the same directory

## Installation

1. Clone or download this repository
2. Install the required dependencies:
   ```bash
   pip install pyautogui 
   ```

## Setup Instructions

### Step 1: Get the Follow Button Image

1. Open TikTok and navigate to your Following list
2. Find a user who doesn't follow you back (they will have a "following" button instead of "Friends")
3. Take a screenshot of the "Following" button
4. Crop the image to show only the button (make it as small as possible while still being recognizable)
5. Save it as `follow.png` in the same directory as `unfollowBot.py`

### Step 2: Get the Correct Region Coordinates

**Important:** The region coordinates in the code are specific to screen resolution and window size. You need to customize them for your setup.

The region is defined as: `(left, top, width, height)`

To get the correct coordinates using PyAutoGUI:

1. Open TikTok and navigate to your Following list
2. Use PyAutoGUI's `position()` function to get the coordinates:
   - Move your mouse to the **top-left corner** of the area where the user list appears
   - Use `pyautogui.position()` to get the coordinates (you can add a `time.sleep()` to give yourself time to position the mouse)
   - Print or note down these coordinates as `top_left = (x1, y1)`
   - Move your mouse to the **bottom-right corner** of the same area
   - Use `pyautogui.position()` again to get the coordinates
   - Print or note down these coordinates as `bottom_right = (x2, y2)`

3. Convert these coordinates to the region format:

   **Step 1: Get top-left and bottom-right points**
   
   Suppose you used the mouse to find the points:
   - `top_left = (x1, y1)`       # e.g., (1095, 585)
   - `bottom_right = (x2, y2)`   # e.g., (1500, 960)
   
   `top_left` → the starting corner of the region
   
   `bottom_right` → the opposite corner

   **Step 2: Compute width and height**
   
   The region tuple in PyAutoGUI is `(left, top, width, height)`.
   
   If your coordinates are:
   - `top_left = (x1, y1)`       # e.g., (1095, 585)
   - `bottom_right = (x2, y2)`   # e.g., (1500, 960)
   
   Then calculate:
   - `left = x1` (the first number from top_left)
   - `top = y1` (the second number from top_left)
   - `width = x2 - x1` (the first number from bottom_right minus the first number from top_left)
   - `height = y2 - y1` (the second number from bottom_right minus the second number from top_left)
   
   `width` = horizontal size of the box
   
   `height` = vertical size of the box

   **Step 3: Create the region tuple**
   - `region = (left, top, width, height)`

4. Update line 5 in `unfollowBot.py` with your calculated coordinates:
   ```python
   region = (left, top, width, height)
   ```

### Step 3: Adjust Scroll Amount (Optional)

The scroll amount on line 29 (`pyautogui.scroll(-565)`) may need adjustment based on your screen size:
- Smaller screens: Use a smaller negative number (e.g., `-400`)
- Larger screens: You might need a larger number (e.g., `-700`)
- Test and adjust until it scrolls the right amount to show the next batch of users

## Usage

1. **Important:** Before running the bot:
   - Open TikTok in your browser
   - Navigate to your Following list
   - Make sure the window is positioned where you set the region coordinates
   - **Do not move your mouse or interact with the computer while the bot is running**

2. Run the bot:
   ```bash
   python unfollowBot.py
   ```

3. The bot will:
   - Search for "Following" button in the specified region
   - Click each button to unfollow users who don't follow you back
   - Scroll down to find more users
   - Continue until you stop it (Ctrl+C)

4. To stop the bot, press `Ctrl+C` in the terminal

## Modifying the Bot

### To Unfollow Everyone

If you want to unfollow everyone (not just those who don't follow you back), you need to:

1. Take a screenshot of the "Following" and "Friends" button 
2. Save it as `following.png` and `Friends.png`
3. NEED TO FINISH

### Adjusting Confidence Level

If the bot is missing buttons or clicking wrong elements, adjust the confidence level on line 16:
- Lower confidence (e.g., `0.85`): More matches, but might click wrong elements
- Higher confidence (e.g., `0.98`): More precise, but might miss some buttons

### Adjusting Timing

You can modify the sleep durations:
- Line 25: Time between clicks (currently 0.2 seconds)
- Line 28: Time before scrolling (currently 1 second)
- Line 30: Time after scrolling (currently 1.5 seconds)

Increase these values if the bot is too fast and missing buttons.


## Disclaimer

This bot is for educational purposes. Use at your own risk. Make sure you comply with TikTok's Terms of Service. Automating interactions may violate TikTok's policies, so use responsibly.

## License

This project is provided as-is for educational purposes.

