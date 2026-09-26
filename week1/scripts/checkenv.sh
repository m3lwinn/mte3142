#!/bin/bash
# checkenv.sh - report the state of the ROS 2 development environment.
# MTE 3142 Robot Operating System Lab, Week 1.

echo "===== Environment report ====="
echo "User          : $USER"
echo "Home          : $HOME"
echo "Current dir   : $(pwd)"
echo "Ubuntu        : $(. /etc/os-release && echo $PRETTY_NAME)"
echo "Architecture  : $(uname -m)"
echo "Python        : $(python3 --version)"
echo "ROS_DISTRO    : ${ROS_DISTRO:-not set}"
echo "=============================="