from mouse_controller import MouseController
import time

def test_movement():
    controller = MouseController()
    
    # Move to different positions with different durations
    print("Moving to center (2 seconds)...")
    controller.move_to(500, 500, duration=2.0)  # Slow movement
    
    time.sleep(0.5)  # Pause between movements
    
    print("Moving to top-left (0.5 seconds)...")
    controller.move_to(100, 100, duration=0.5)  # Fast movement
    
    time.sleep(0.5)
    
    print("Moving to bottom-right (3 seconds)...")
    controller.move_to(800, 600, duration=3.0)  # Very slow movement

if __name__ == "__main__":
    print("Starting mouse movement test...")
    print("Move mouse to any corner to abort!")
    time.sleep(2)  # Give user time to read the message
    test_movement()
    print("Test completed!") 