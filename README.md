# Human-Like Mouse Movement Simulator

A Python tool that simulates natural, human-like mouse movements. This project creates smooth, realistic mouse movements with natural acceleration and randomization patterns.

## Features

- 🖱️ Natural mouse movement patterns
- 🎯 Customizable movement speeds
- 🔄 Continuous operation mode
- ⚡ Variable acceleration/deceleration
- 🎲 Random path deviation for realism
- 🛑 Easy abort functionality (move to corner or Ctrl+C)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/human-like-mouse-simulator.git
cd human-like-mouse-simulator
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Quick Start

Run the basic movement test:
```bash
python main.py
```

The mouse will move in a pattern:
1. Center of screen (2 seconds)
2. Top-left corner (0.5 seconds)
3. Bottom-right corner (3 seconds)
4. Repeat

To stop the program:
- Press Ctrl+C
- OR move mouse to any screen corner

## Usage Examples

### Basic Movement
```python
from src.mouse_controller import MouseController

controller = MouseController()

# Move to position (x=500, y=500) in 2 seconds
controller.move_to(500, 500, duration=2.0)
```

### Custom Movement Sequence
```python
controller = MouseController()

# Fast movement
controller.move_to(100, 100, duration=0.5)

# Slow, precise movement
controller.move_to(800, 600, duration=3.0)
```

## Configuration

The movement characteristics can be adjusted in:
- `src/trajectory.py`: Path calculation and randomization
- `src/mouse_controller.py`: Timing and movement execution

Key parameters:
- `points_count`: Number of points in movement path (default: 20)
- `deviation`: Maximum random deviation from direct path
- `duration`: Time to complete movement

## Project Structure

```
project/
├── src/
│   ├── mouse_controller.py  # Core movement logic
│   ├── trajectory.py        # Path calculations
│   └── test_movement.py     # Movement tests
├── main.py                  # Main program
└── requirements.txt         # Dependencies
```

## Dependencies

- pyautogui: Mouse control
- numpy: Mathematical calculations
- pytest: Testing framework

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## Acknowledgments

- PyAutoGUI for mouse control functionality
- NumPy for mathematical operations
