from setuptools import setup, find_packages

setup(
    name="mouse_movement",
    version="0.1.0",
    packages=["mouse_movement"],
    install_requires=[
        "pyautogui>=0.9.54",
        "numpy>=1.24.0",
        "pytest>=7.4.0",
    ],
) 