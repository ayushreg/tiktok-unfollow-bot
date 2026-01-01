import time
import pyautogui

# The region of the follow list page
region = (1095,585,405,375)
left, top, width , height = region

# Get center of the window and use it to scroll
centerX, centerY = left+width//2, top+height//2
pyautogui.moveTo(centerX, centerY)

while True:
    try:
        # LocateAllOnScreen returns a box object with cords, so <box> <box> so we need to convert to list
        # So if we want to move our mouse to it, we have to conver it to just x and y axis
        matches = list(pyautogui.locateAllOnScreen("follow.png", region=region, confidence=.95))
    except Exception as e:
        matches = []

    if (matches):
        # Click each unfollow if we found the button
        for match in matches:
            x, y = pyautogui.center(match)
            pyautogui.click(x, y)
            time.sleep(0.2)

    # Scroll to next batch
    time.sleep(1)
    pyautogui.scroll(-565)
    time.sleep(1.5)


