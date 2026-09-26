#!/usr/bin/env python3
"""
p1_hello_robot.py
Week 1, Task 12, Program 1
Purpose: the anatomy of a Python script - shebang, docstring, main guard.
"""


def main():
    robot_name = "MTE-Bot"
    wheel_count = 2
    wheel_radius_m = 0.033

    print("Hello from the Robot Operating System Lab")
    print(f"Robot name    : {robot_name}")
    print(f"Wheel count   : {wheel_count}")
    print(f"Wheel radius  : {wheel_radius_m} m")

    circumference = 2 * 3.14159 * wheel_radius_m
    print(f"Wheel circumference: {circumference:.4f} m")


if __name__ == "__main__":
    main()