from ov7670 import *

# Wrapper register configurations are based off the Adafruit OV7670
# circuitpython driver.
# https://github.com/adafruit/Adafruit_CircuitPython_OV7670

OV7670_WRAPPER_SIZE_DIV1  = 0 # 640x480
OV7670_WRAPPER_SIZE_DIV2  = 1 # 320x240
OV7670_WRAPPER_SIZE_DIV4  = 2 # 160x120
OV7670_WRAPPER_SIZE_DIV8  = 3 # 80x60
OV7670_WRAPPER_SIZE_DIV16 = 4 # 40x30

OV7670_WRAPPER_TEST_PATTERN_NONE           = 0
OV7670_WRAPPER_TEST_PATTERN_SHIFTING_1     = 1
OV7670_WRAPPER_TEST_PATTERN_COLOR_BAR      = 2
OV7670_WRAPPER_TEST_PATTERN_COLOR_BAR_FADE = 3

class OV7670Wrapper(OV7670):
    def wrapper_configure_base(self):
        self.write_register(OV7670_REG_TSLB          , 0x04)
        self.write_register(OV7670_REG_COM10         , 0x02)
        self.write_register(OV7670_REG_SLOP          , 0x20)
        self.write_register(OV7670_REG_COM8          , 0x80 | 0x40 | 0x20)
        self.write_register(OV7670_REG_GAIN          , 0x00)
        self.write_register(OV7670_REG_COM4          , 0x00)
        self.write_register(OV7670_REG_COM9          , 0x20)
        self.write_register(OV7670_REG_BD50MAX       , 0x05)
        self.write_register(OV7670_REG_BD60MAX       , 0x07)
        self.write_register(OV7670_REG_AEW           , 0x75)
        self.write_register(OV7670_REG_AEB           , 0x63)
        self.write_register(OV7670_REG_VPT           , 0xA5)
        self.write_register(OV7670_REG_HAECC1        , 0x78)
        self.write_register(OV7670_REG_HAECC2        , 0x68)
        self.write_register(OV7670_REG_HAECC3        , 0xDF)
        self.write_register(OV7670_REG_HAECC4        , 0xDF)
        self.write_register(OV7670_REG_HAECC5        , 0xF0)
        self.write_register(OV7670_REG_HAECC6        , 0x90)
        self.write_register(OV7670_REG_HAECC7        , 0x94)
        self.write_register(OV7670_REG_COM8          , 0x80 | 0x40 | 0x20 | 0x04 | 0x01)
        self.write_register(OV7670_REG_COM5          , 0x61)
        self.write_register(OV7670_REG_COM6          , 0x4B)
        self.write_register(OV7670_REG_MVFP          , 0x07)
        self.write_register(OV7670_REG_ADCCTR1       , 0x02)
        self.write_register(OV7670_REG_ADCCTR2       , 0x91)
        self.write_register(OV7670_REG_CHLF          , 0x0B)
        self.write_register(OV7670_REG_ADC           , 0x1D)
        self.write_register(OV7670_REG_ACOM          , 0x71)
        self.write_register(OV7670_REG_OFON          , 0x2A)
        self.write_register(OV7670_REG_COM12         , 0x78)
        self.write_register(OV7670_REG_GFIX          , 0x5D)
        self.write_register(OV7670_REG_REG74         , 0x19)
        self.write_register(OV7670_REG_DM_LNL        , 0x00)
        self.write_register(OV7670_REG_ABLC1         , 0x0C)
        self.write_register(OV7670_REG_THL_ST        , 0x82)
        self.write_register(OV7670_REG_AWBC1         , 0x14)
        self.write_register(OV7670_REG_AWBC2         , 0xF0)
        self.write_register(OV7670_REG_AWBC3         , 0x34)
        self.write_register(OV7670_REG_AWBC4         , 0x58)
        self.write_register(OV7670_REG_AWBC5         , 0x28)
        self.write_register(OV7670_REG_AWBC6         , 0x3A)
        self.write_register(OV7670_REG_LCC3          , 0x04)
        self.write_register(OV7670_REG_LCC4          , 0x20)
        self.write_register(OV7670_REG_LCC5          , 0x05)
        self.write_register(OV7670_REG_LCC6          , 0x04)
        self.write_register(OV7670_REG_LCC7          , 0x08)
        self.write_register(OV7670_REG_AWBCTR3       , 0x0A)
        self.write_register(OV7670_REG_AWBCTR2       , 0x55)
        self.write_register(OV7670_REG_MTX1          , 0x80)
        self.write_register(OV7670_REG_MTX2          , 0x80)
        self.write_register(OV7670_REG_MTX3          , 0x00)
        self.write_register(OV7670_REG_MTX4          , 0x22)
        self.write_register(OV7670_REG_MTX5          , 0x5E)
        self.write_register(OV7670_REG_MTX6          , 0x80)
        self.write_register(OV7670_REG_AWBCTR1       , 0x11)
        self.write_register(OV7670_REG_AWBCTR0       , 0x9F)
        self.write_register(OV7670_REG_BRIGHT        , 0x00)
        self.write_register(OV7670_REG_CONTRAS       , 0x40)
        self.write_register(OV7670_REG_CONTRAS_CENTER, 0x80)

        # Magic reserved registers! I recon my datasheet is outdated.
        # These were got from https://github.com/adafruit/Adafruit_CircuitPython_OV7670
        self.write_register(0x16, 0x02)
        self.write_register(0x29, 0x07)
        self.write_register(0x35, 0x0B)
        self.write_register(0x4D, 0x40)
        self.write_register(0x4E, 0x20)
        self.write_register(0x59, 0x88)
        self.write_register(0x5A, 0x88)
        self.write_register(0x5B, 0x44)
        self.write_register(0x5C, 0x67)
        self.write_register(0x5D, 0x49)
        self.write_register(0x5E, 0x0E)
        self.write_register(0x8D, 0x4F)
        self.write_register(0x8E, 0x00)
        self.write_register(0x8F, 0x00)
        self.write_register(0x90, 0x00)
        self.write_register(0x91, 0x00)
        self.write_register(0x96, 0x00)
        self.write_register(0x9A, 0x80)
        self.write_register(0xA1, 0x03)
        self.write_register(0xB0, 0x84)
        self.write_register(0xB2, 0x0E)
        self.write_register(0xB8, 0x0A)

        gamma_curve = [0x1C, 0x28, 0x3C, 0x55, 0x68, 0x76, 0x80, 0x88, 0x8F, 0x96, 0xA3, 0xAF, 0xC4, 0xD7, 0xE8]
        for i in range(15):
            self.write_register(OV7670_REG_GAM_BASE +  i, gamma_curve[i])

    def wrapper_configure_rgb(self):
        self.write_register(OV7670_REG_COM7  , 0x04)
        self.write_register(OV7670_REG_RGB444, 0x00)
        self.write_register(OV7670_REG_COM15 , 0x10 | 0xC0)

    def wrapper_configure_size(self, size):
        com3,com14,dcw,pclk_div,scaling_bits,vstart,hstart,edge_offset = [
            # com3       , com14, dcw , pclk_div, scaling_bits, vstart, hstart, edge_offset
            ( 0x00       , 0x00 , 0x00, 0x08    , 0x20        ,  9    , 162   , 2          ), # DIV1  640x480
            ( 0x04       , 0x19 , 0x11, 0xF1    , 0x20        , 10    , 174   , 0          ), # DIV2  320x240
            ( 0x04       , 0x1A , 0x22, 0xF2    , 0x20        , 11    , 186   , 2          ), # DIV4  160x120
            ( 0x04       , 0x1B , 0x33, 0xF3    , 0x20        , 12    , 210   , 0          ), # DIV8  80x60
            ( 0x04 | 0x08, 0x1C , 0x33, 0xF4    , 0x40        , 15    , 252   , 3          ), # DIV16 40x30
        ][size]

        self.write_register(OV7670_REG_COM3            , com3)
        self.write_register(OV7670_REG_COM14           , com14)
        self.write_register(OV7670_REG_SCALING_DCWCTR  , dcw)
        self.write_register(OV7670_REG_SCALING_PCLK_DIV, pclk_div)

        xsc = self.read_register(OV7670_REG_SCALING_XSC)
        ysc = self.read_register(OV7670_REG_SCALING_YSC)
        xsc = (xsc & 0x80) | scaling_bits
        ysc = (ysc & 0x80) | scaling_bits
        self.write_register(OV7670_REG_SCALING_XSC, xsc)
        self.write_register(OV7670_REG_SCALING_YSC, ysc)

        vstop = vstart + 480
        hstop = (hstart + 640) % 784
        self.write_register(OV7670_REG_HSTART, hstart >> 3)
        self.write_register(OV7670_REG_HSTOP , hstop >> 3)
        self.write_register(
            OV7670_REG_HREF,
            (edge_offset << 6) | ((hstop & 0b111) << 3) | (hstart & 0b111),
        )
        self.write_register(OV7670_REG_VSTART, vstart >> 2)
        self.write_register(OV7670_REG_VSTOP , vstop >> 2)
        self.write_register(OV7670_REG_VREF  , ((vstop & 0b11) << 2) | (vstart & 0b11))

        self.write_register(OV7670_REG_SCALING_PCLK_DELAY, 0x02)

        return [
            (640, 480),
            (320, 240),
            (160, 120),
            ( 80,  60),
            ( 40,  30)
        ][size]

    def wrapper_configure_test_pattern(self, pattern):
        xsc = self.read_register(OV7670_REG_SCALING_XSC) & ~0x80
        ysc = self.read_register(OV7670_REG_SCALING_YSC) & ~0x80
        if pattern == OV7670_WRAPPER_TEST_PATTERN_SHIFTING_1:
            xsc |= 0x80
        elif pattern == OV7670_WRAPPER_TEST_PATTERN_COLOR_BAR:
            ysc |= 0x80
        elif pattern == OV7670_WRAPPER_TEST_PATTERN_COLOR_BAR_FADE:
            xsc |= 0x80
            ysc |= 0x80
        self.write_register(OV7670_REG_SCALING_XSC, xsc)
        self.write_register(OV7670_REG_SCALING_YSC, ysc)
