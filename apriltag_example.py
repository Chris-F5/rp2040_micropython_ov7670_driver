import gc
import machine
import apriltag
from ov7670_wrapper import *
import time

data_pin_base   = 0 # 0 and the next 7 pins. So GPIO 0-7 in this case.
pclk_pin_no     = 8
mclk_pin_no     = 9
href_pin_no     = 12
vsync_pin_no    = 13
reset_pin_no    = 14
shutdown_pin_no = 15
sda_pin_no      = 20
scl_pin_no      = 21

i2c = machine.I2C(0, freq=100000, scl=machine.Pin(scl_pin_no), sda=machine.Pin(sda_pin_no))
ov7670 = OV7670Wrapper(
    i2c_bus=i2c,
    mclk_pin_no=mclk_pin_no,
    pclk_pin_no=pclk_pin_no,
    data_pin_base=data_pin_base,
    vsync_pin_no=vsync_pin_no,
    href_pin_no=href_pin_no,
    reset_pin_no=reset_pin_no,
    shutdown_pin_no=shutdown_pin_no,
    half_capture=True # Capture only (first) greyscale byte of YUV pixel color.
)

ov7670.wrapper_configure_yuv()
ov7670.wrapper_configure_base()
width,height = ov7670.wrapper_configure_size(OV7670_WRAPPER_SIZE_DIV4)
ov7670.wrapper_configure_test_pattern(OV7670_WRAPPER_TEST_PATTERN_NONE)

img = bytearray(width*height)

import select
import sys

def send_img(img):
    # 12 chunks of 1600 bytes for 120x160 img
    for chunk in range(0, len(img), 1600):
        sys.stdout.write(img[chunk:chunk+1600])
        time.sleep(0.05)
        ack = sys.stdin.read(1)

gc.collect()
#print(f"{gc.mem_alloc()}/{gc.mem_alloc()+gc.mem_free()}")
while True:
    ov7670.capture(img)
    # print(img)
    #sys.stdout.buffer.write(img)
    try:
        detections = apriltag.detect(img)
    except MemoryError:
        detections = [(0, 0)]
    print(str(detections))
    send_img(img)
    #poll_obj.poll(1000)

#chars = " .:-=+*#%@"
#for y in range(height):
#    for x in range(width):
#        value = buf[2*(y*width+x)]
#        print(chars[value*len(chars)//256], end='')
#    print('')

