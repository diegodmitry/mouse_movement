"""
Mouse Controller module for generating human-like mouse movements.
This module handles the core functionality for moving the mouse in a natural way.
"""

import logging
import random
import time
from typing import Tuple, List

import numpy as np
import pyautogui
from src import trajectory

# Configure PyAutoGUI settings
pyautogui.FAILSAFE = True  # Move mouse to corner to abort
pyautogui.PAUSE = 0.0  # Remove default pause to control timing ourselves

class MouseController:
    """Controls mouse movements with human-like characteristics."""
    
    def __init__(self):
        """Initialize the mouse controller with default settings."""
        self.logger = logging.getLogger(__name__)
        print("MouseController initialized")  # Debug print
        
    def move_to(self, x: int, y: int, duration: float = 1.0):
        """
        Move mouse to target position with specified duration and natural movement.
        
        Args:
            x: Target x coordinate
            y: Target y coordinate
            duration: Time to complete movement in seconds (default: 1.0)
        """
        start_x, start_y = pyautogui.position()
        print(f"Starting mouse movement from ({start_x}, {start_y}) to ({x}, {y})")  # Debug print
        
        # Generate fewer points for smoother movement
        points = trajectory.generate_curve_points(
            start=(start_x, start_y),
            end=(x, y),
            points_count=max(20, int(duration * 20))  # Reduced number of points
        )
        print(f"Generated {len(points)} points for movement")  # Debug print
        
        # Calculate timing
        time_per_point = duration / (len(points) - 1)  # Adjust for endpoint
        start_time = time.perf_counter()
        last_time = start_time
        
        try:
            # Move through points
            for i, (px, py) in enumerate(points):
                current_time = time.perf_counter()
                target_time = start_time + (i * time_per_point)
                
                # Sleep if we're ahead of schedule
                if current_time < target_time:
                    time.sleep(target_time - current_time)
                
                # Move to next point
                pyautogui.moveTo(int(px), int(py))
                
                # Debug print every 5th point to reduce output
                if i % 5 == 0:
                    print(f"Moving to point {i}: ({int(px)}, {int(py)})")
                
                last_time = time.perf_counter()
            
            actual_duration = last_time - start_time
            print(f"Movement completed in {actual_duration:.2f} seconds")
            
        except Exception as e:
            print(f"Error during mouse movement: {e}")
            raise
        
        self.logger.debug(
            f"Completed mouse movement from ({start_x}, {start_y}) "
            f"to ({x}, {y}) in {duration:.2f} seconds"
        )
        
    def _calculate_natural_duration(self, distance: float) -> float:
        """
        Calculate natural movement duration based on distance.
        Humans take longer to move longer distances.
        
        Args:
            distance: Distance to move in pixels
            
        Returns:
            Duration in seconds
        """
        # Base duration with some randomization
        base_duration = 0.5 + (distance / 1000.0)
        return base_duration * random.uniform(0.9, 1.1) 