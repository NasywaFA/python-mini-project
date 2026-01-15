import pyautogui
import time
import threading
import keyboard

# Global variable to control the clicking
clicking = False

def click_mouse():
    while clicking:
        pyautogui.click()  # Perform the click
        time.sleep(interval)  # Wait for the specified interval

# Set the interval between clicks (in seconds)
interval = 0  # Adjust this value as needed

# Start the auto clicker
def start_clicking():
    global clicking
    clicking = True
    click_mouse()

# Stop the auto clicker
def stop_clicking():
    global clicking
    clicking = False

# Main function
if __name__ == "__main__":
    print("Auto clicker will start in 5 seconds. Move your mouse to the desired location.")
    time.sleep(5)  # Delay to allow you to position the mouse

    # Start the clicking in a separate thread
    click_thread = threading.Thread(target=start_clicking)
    click_thread.start()

    # Wait for the Caps Lock key to be pressed to stop clicking
    print("Press Caps Lock to stop clicking...")
    keyboard.wait('caps lock')  # Wait for the Caps Lock key to be pressed
    stop_clicking()
    click_thread.join()  # Wait for the thread to finish

    print("Auto clicking stopped.")