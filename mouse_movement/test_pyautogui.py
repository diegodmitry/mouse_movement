import pyautogui
import time

def test_basic_movement():
    print("Current mouse position:", pyautogui.position())
    print("Screen size:", pyautogui.size())
    print("Moving mouse to (100, 100)...")
    pyautogui.moveTo(100, 100, duration=1)
    time.sleep(1)
    print("Moving mouse to (500, 500)...")
    pyautogui.moveTo(500, 500, duration=1)
    print("Test completed!")

if __name__ == "__main__":
    print("Starting basic PyAutoGUI test...")
    print("Move mouse to corner to abort!")
    time.sleep(2)
    test_basic_movement() 