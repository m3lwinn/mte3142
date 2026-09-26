#!/usr/bin/env python3
"""
p5_callbacks.py
Week 1, Task 12, Program 5
Purpose: functions as objects, and the callback pattern.
A ROS 2 timer and a ROS 2 subscriber both work exactly like this.
"""

import time


class Timer:
    """Calls a function you hand it, once every period_s seconds."""

    def __init__(self, period_s, callback):
        # 'callback' is a FUNCTION stored in a variable. Note there are no
        # parentheses after it - we are storing it, not calling it.
        self.period_s = period_s
        self.callback = callback

    def spin(self, ticks):
        for _ in range(ticks):
            time.sleep(self.period_s)
            self.callback()          # NOW we call it.


class CounterNode:

    def __init__(self):
        self.count = 0
        # Pass the bound method self.on_timer as the callback.
        self.timer = Timer(period_s=0.5, callback=self.on_timer)

    def on_timer(self):
        """The callback. We never call this ourselves; the Timer does."""
        self.count += 1
        print(f"[INFO] [counter]: tick {self.count}")

    def run(self, ticks):
        print("Starting timer. The Timer object owns the loop, not us.")
        self.timer.spin(ticks)
        print(f"Finished. Callback ran {self.count} times.")


def main():
    node = CounterNode()
    node.run(5)


if __name__ == "__main__":
    main()