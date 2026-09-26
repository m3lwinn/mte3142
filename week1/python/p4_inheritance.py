#!/usr/bin/env python3
"""
p4_inheritance.py
Week 1, Task 12, Program 4
Purpose: inheritance and super().__init__().
This is EXACTLY the pattern every ROS 2 Python node uses in Week 3.
"""


class Node:
    """Stand-in for rclpy.node.Node. In Week 3 this class comes from ROS 2
    and you will not write it yourself - but it behaves like this."""

    def __init__(self, node_name):
        self.node_name = node_name
        print(f"  [Node.__init__] base class registered node '{node_name}'")

    def get_name(self):
        return self.node_name

    def log_info(self, message):
        print(f"[INFO] [{self.node_name}]: {message}")


class TemperatureSensorNode(Node):
    """A node that inherits everything Node can do, and adds its own."""

    def __init__(self):
        # Hand the name up to the parent class. Forget this line and the
        # object has no node_name, which is the single most common
        # beginner error in ROS 2.
        super().__init__("temperature_sensor")
        self.readings = []
        print("  [TemperatureSensorNode.__init__] subclass ready")

    def add_reading(self, celsius):
        self.readings.append(celsius)
        self.log_info(f"new reading: {celsius:.1f} C")

    def summary(self):
        if not self.readings:
            self.log_info("no readings yet")
            return
        self.log_info(f"count={len(self.readings)} "
                      f"min={min(self.readings):.1f} "
                      f"max={max(self.readings):.1f}")


def main():
    print("Creating the node object:")
    sensor = TemperatureSensorNode()

    print(f"\nget_name() was inherited from Node -> '{sensor.get_name()}'\n")

    for value in [21.4, 22.8, 25.1, 24.0]:
        sensor.add_reading(value)

    print()
    sensor.summary()


if __name__ == "__main__":
    main()