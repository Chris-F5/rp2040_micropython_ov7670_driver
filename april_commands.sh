#!/bin/bash

set -ex

MPYDIR=~/r/micropython
$MPYDIR/mpy-cross/build/mpy-cross ov7670.py
$MPYDIR/mpy-cross/build/mpy-cross ov7670_wrapper.py
#$MPYDIR/mpy-cross/build/mpy-cross apriltag_example.py

#ampy --port /dev/ttyACM1 rm /ov7670.py
#ampy --port /dev/ttyACM1 rm /ov7670_wrapper.py

ampy --port /dev/ttyACM0 put ov7670.mpy /ov7670.mpy
ampy --port /dev/ttyACM0 put ov7670_wrapper.mpy /ov7670_wrapper.mpy
ampy --port /dev/ttyACM0 run apriltag_example.py
#ampy --port /dev/ttyACM1 put apriltag_example.py
