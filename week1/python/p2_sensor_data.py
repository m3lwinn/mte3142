#!/usr/bin/env python3
"""
p2_sensor_data.py
Week 1, Task 12, Program 2
Purpose: lists, dictionaries, loops and functions, using the shape of a
real lidar reading.
"""


def average(values):
    """Return the arithmetic mean of a list of numbers."""
    if len(values) == 0:
        return 0.0
    return sum(values) / len(values)


def closest_obstacle(ranges, range_max):
    """Return the smallest valid range. Values at or above range_max are
    treated as 'no return' and ignored, as a real lidar driver does."""
    valid = [r for r in ranges if r < range_max]
    if not valid:
        return None
    return min(valid)


def main():
    # A lidar message carries metadata plus an array of distances.
    scan = {
        "frame_id": "lidar_link",
        "angle_min": -1.5708,
        "angle_max": 1.5708,
        "range_min": 0.12,
        "range_max": 3.50,
        "ranges": [3.50, 2.41, 1.88, 0.95, 0.74, 1.02, 2.30, 3.50],
    }

    print(f"Frame            : {scan['frame_id']}")
    print(f"Number of beams  : {len(scan['ranges'])}")
    print(f"Average range    : {average(scan['ranges']):.3f} m")

    nearest = closest_obstacle(scan["ranges"], scan["range_max"])
    if nearest is None:
        print("Nearest obstacle : none detected")
    else:
        print(f"Nearest obstacle : {nearest:.3f} m")

    print("\nBeam-by-beam report:")
    for index, distance in enumerate(scan["ranges"]):
        if distance >= scan["range_max"]:
            status = "no return"
        elif distance < 1.0:
            status = "TOO CLOSE"
        else:
            status = "clear"
        print(f"  beam {index}: {distance:5.2f} m  ->  {status}")


if __name__ == "__main__":
    main()