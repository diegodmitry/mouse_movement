from src.mouse_controller import MouseController
import time
import sys

def main():
    controller = MouseController()
    try:
        print("Mouse movement program started!")
        print("Press Ctrl+C to stop or move mouse to any corner")
        
        while True:  # Run indefinitely until interrupted
            # Move to different positions with different durations
            print("\nStarting movement sequence...")
            
            print("Moving to center (2 seconds)...")
            controller.move_to(500, 500, duration=2.0)
            time.sleep(1)  # Pause between movements
            
            print("Moving to top-left (0.5 seconds)...")
            controller.move_to(100, 100, duration=0.5)
            time.sleep(1)
            
            print("Moving to bottom-right (3 seconds)...")
            controller.move_to(800, 600, duration=3.0)
            time.sleep(1)
            
            print("\nCompleted one sequence. Starting again in 3 seconds...")
            time.sleep(3)
            
    except KeyboardInterrupt:
        print("\nProgram stopped by user")
        sys.exit(0)
    except Exception as e:
        print(f"\nError occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 