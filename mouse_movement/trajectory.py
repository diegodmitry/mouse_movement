"""
Trajectory module for calculating natural mouse movement paths.
"""

import numpy as np
from typing import List, Tuple

def generate_curve_points(
    start: Tuple[int, int],
    end: Tuple[int, int],
    control_points: int = 2,
    points_count: int = 20
) -> List[Tuple[float, float]]:
    """Generate a smooth curve between two points."""
    
    # Calculate distance for scaling randomness
    distance = np.sqrt((end[0] - start[0])**2 + (end[1] - start[1])**2)
    
    # Generate control point with randomness scaled to distance
    t = np.random.uniform(0.3, 0.7)
    control_x = start[0] + (end[0] - start[0]) * t
    control_y = start[1] + (end[1] - start[1]) * t
    
    # Scale random deviation based on distance
    deviation = min(distance * 0.1, 100)  # Cap maximum deviation
    control_x += np.random.normal(0, deviation)
    control_y += np.random.normal(0, deviation)
    
    # Generate smoother curve with fewer points
    t_values = np.linspace(0, 1, points_count)
    points = []
    
    for t in t_values:
        # Quadratic Bezier curve formula
        x = (1-t)**2 * start[0] + 2*(1-t)*t * control_x + t**2 * end[0]
        y = (1-t)**2 * start[1] + 2*(1-t)*t * control_y + t**2 * end[1]
        points.append((x, y))
    
    return points 