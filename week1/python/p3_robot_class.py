#!/usr/bin/env python3
"""
p3_robot_class.py
Week 1, Task 12, Program 3
Purpose: classes, __init__, self, attributes and methods.
"""


class DifferentialDriveRobot:
    """A minimal model of a two-wheeled robot."""

    def __init__(self, name, wheel_radius, wheel_separation):
        # These run once, when the object is created.
        self.name = name
        self.wheel_radius = wheel_radius
        self.wheel_separation = wheel_separation
        self.left_wheel_speed = 0.0    # rad/s
        self.right_wheel_speed = 0.0   # rad/s

    def set_wheel_speeds(self, left, right):
        self.left_wheel_speed = left
        self.right_wheel_speed = right

    def linear_velocity(self):
        """Forward speed of the robot body, in m/s."""
        return self.wheel_radius * (self.right_wheel_speed
                                    + self.left_wheel_speed) / 2.0

    def angular_velocity(self):
        """Rotation rate of the robot body, in rad/s."""
        return self.wheel_radius * (self.right_wheel_speed
                                    - self.left_wheel_speed) / self.wheel_separation

    def report(self):
        print(f"[{self.name}] "
              f"wheels L={self.left_wheel_speed:.2f} R={self.right_wheel_speed:.2f} rad/s "
              f"-> v={self.linear_velocity():.3f} m/s, "
              f"w={self.angular_velocity():.3f} rad/s")


def main():
    robot = DifferentialDriveRobot("MTE-Bot", wheel_radius=0.033,
                                   wheel_separation=0.160)

    print("Straight ahead:")
    robot.set_wheel_speeds(10.0, 10.0)
    robot.report()

    print("\nSpinning on the spot:")
    robot.set_wheel_speeds(-10.0, 10.0)
    robot.report()

    print("\nGentle left turn:")
    robot.set_wheel_speeds(8.0, 12.0)
    robot.report()


if __name__ == "__main__":
    main()