#!/usr/bin/env python3
"""
p6_mini_ros.py
Week 1, Task 12, Program 6 (capstone)
Purpose: a working miniature of the ROS 2 publish/subscribe pattern,
written in plain Python. Nothing here is ROS 2 - but in Week 3 you will
write almost identical code using the real rclpy library.
"""

import time


# --------------------------------------------------------------------
# The "middleware". In real ROS 2 this is DDS, and it is far cleverer.
# --------------------------------------------------------------------
class Graph:
    """Keeps track of who publishes and who subscribes to each topic."""

    def __init__(self):
        self.subscribers = {}          # topic name -> list of callbacks

    def subscribe(self, topic, callback):
        self.subscribers.setdefault(topic, []).append(callback)

    def publish(self, topic, message):
        for callback in self.subscribers.get(topic, []):
            callback(message)          # deliver to every subscriber


GRAPH = Graph()


class Node:
    def __init__(self, node_name):
        self.node_name = node_name

    def log_info(self, message):
        print(f"[INFO] [{self.node_name}]: {message}")

    def create_publisher(self, topic):
        return Publisher(topic)

    def create_subscription(self, topic, callback):
        GRAPH.subscribe(topic, callback)
        self.log_info(f"subscribed to '{topic}'")


class Publisher:
    def __init__(self, topic):
        self.topic = topic

    def publish(self, message):
        GRAPH.publish(self.topic, message)


# --------------------------------------------------------------------
# Two application nodes.
# --------------------------------------------------------------------
class DistanceSensorNode(Node):
    """Publishes a distance reading on the topic /distance."""

    def __init__(self):
        super().__init__("distance_sensor")
        self.publisher = self.create_publisher("/distance")
        self.samples = [2.40, 1.85, 1.20, 0.65, 0.30]
        self.index = 0

    def publish_once(self):
        if self.index >= len(self.samples):
            return False
        value = self.samples[self.index]
        self.index += 1
        self.log_info(f"publishing {value:.2f} m")
        self.publisher.publish(value)
        return True


class SafetyMonitorNode(Node):
    """Subscribes to /distance and reacts when the robot gets too close."""

    STOP_DISTANCE = 0.50

    def __init__(self):
        super().__init__("safety_monitor")
        self.create_subscription("/distance", self.distance_callback)

    def distance_callback(self, distance):
        """Runs every time a message arrives. We never call it ourselves."""
        if distance < self.STOP_DISTANCE:
            self.log_info(f"heard {distance:.2f} m -> STOP, obstacle too close")
        else:
            self.log_info(f"heard {distance:.2f} m -> continue")


def main():
    sensor = DistanceSensorNode()
    monitor = SafetyMonitorNode()

    print("-" * 58)
    while sensor.publish_once():
        time.sleep(0.4)
    print("-" * 58)
    print("Both nodes ran without ever calling each other directly.")
    print("That indirection is the whole idea behind ROS 2.")


if __name__ == "__main__":
    main()