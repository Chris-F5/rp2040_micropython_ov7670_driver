import machine
from ov7670_wrapper import *

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
)

ov7670.wrapper_configure_rgb()
ov7670.wrapper_configure_base()
width,height = ov7670.wrapper_configure_size(OV7670_WRAPPER_SIZE_DIV8)
ov7670.wrapper_configure_test_pattern(OV7670_WRAPPER_TEST_PATTERN_NONE)

buf = bytearray(width*height*2)
ov7670.capture(buf)

chars = " .:-=+*#%@"
for y in range(height):
    for x in range(width):
        rgb565 = (buf[2*(y*width+x)] << 8) | buf[2*(y*width+x)+1]
        r = ((rgb565 >> 11) & 0x1F) << 3
        g = ((rgb565 >>  5) & 0x3F) << 2
        b = ((rgb565 >>  0) & 0x1F) << 3
        v = max(r, g, b)
        print(chars[v*len(chars)//256], end='')
    print('')
