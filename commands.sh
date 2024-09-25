#!/bin/bash

set -ex
ampy --port /dev/ttyACM0 put ov7670.py /ov7670.py
ampy --port /dev/ttyACM0 put ov7670_wrapper.py /ov7670_wrapper.py
ampy --port /dev/ttyACM0 run example.py
