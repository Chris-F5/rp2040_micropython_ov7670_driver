#!/bin/bash
feh -Z out.png &
ampy --port /dev/ttyACM0 run apriltag_example.py | python3 apriltag_example_show.py
