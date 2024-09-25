import machine
import rp2
import time

# See the Omni Vision OV7670 datasheet for register info.
OV7670_REG_GAIN               = const(0x00)
OV7670_REG_BLUE               = const(0x01)
OV7670_REG_RED                = const(0x02)
OV7670_REG_VREF               = const(0x03)
OV7670_REG_COM1               = const(0x04)
OV7670_REG_BAVE               = const(0x05)
OV7670_REG_GbAVE              = const(0x06)
OV7670_REG_AECHH              = const(0x07)
OV7670_REG_RAVE               = const(0x08)
OV7670_REG_COM2               = const(0x09)
OV7670_REG_PID                = const(0x0A)
OV7670_REG_VER                = const(0x0B)
OV7670_REG_COM3               = const(0x0C)
OV7670_REG_COM4               = const(0x0D)
OV7670_REG_COM5               = const(0x0E)
OV7670_REG_COM6               = const(0x0F)
OV7670_REG_AECH               = const(0x10)
OV7670_REG_CLKRC              = const(0x11)
OV7670_REG_COM7               = const(0x12)
OV7670_REG_COM8               = const(0x13)
OV7670_REG_COM9               = const(0x14)
OV7670_REG_COM10              = const(0x15)
OV7670_REG_HSTART             = const(0x17)
OV7670_REG_HSTOP              = const(0x18)
OV7670_REG_VSTART             = const(0x19)
OV7670_REG_VSTOP              = const(0x1A)
OV7670_REG_PSHFT              = const(0x1B)
OV7670_REG_MIDH               = const(0x1C)
OV7670_REG_MIDL               = const(0x1D)
OV7670_REG_MVFP               = const(0x1E)
OV7670_REG_LAEC               = const(0x1F)
OV7670_REG_ADCCTR0            = const(0x20)
OV7670_REG_ADCCTR1            = const(0x21)
OV7670_REG_ADCCTR2            = const(0x22)
OV7670_REG_ADCCTR3            = const(0x23)
OV7670_REG_AEW                = const(0x24)
OV7670_REG_AEB                = const(0x25)
OV7670_REG_VPT                = const(0x26)
OV7670_REG_BBIAS              = const(0x27)
OV7670_REG_GbBIAS             = const(0x28)
OV7670_REG_EXHCH              = const(0x2A)
OV7670_REG_EXHCL              = const(0x2B)
OV7670_REG_RBIAS              = const(0x2C)
OV7670_REG_ADVFL              = const(0x2D)
OV7670_REG_ADVFH              = const(0x2E)
OV7670_REG_YAVE               = const(0x2F)
OV7670_REG_HSYST              = const(0x30)
OV7670_REG_HSYEN              = const(0x31)
OV7670_REG_HREF               = const(0x32)
OV7670_REG_CHLF               = const(0x33)
OV7670_REG_ARBLM              = const(0x34)
OV7670_REG_ADC                = const(0x37)
OV7670_REG_ACOM               = const(0x38)
OV7670_REG_OFON               = const(0x39)
OV7670_REG_TSLB               = const(0x3A)
OV7670_REG_COM11              = const(0x3B)
OV7670_REG_COM12              = const(0x3C)
OV7670_REG_COM13              = const(0x3D)
OV7670_REG_COM14              = const(0x3E)
OV7670_REG_EDGE               = const(0x3F)
OV7670_REG_COM15              = const(0x40)
OV7670_REG_COM16              = const(0x41)
OV7670_REG_COM17              = const(0x42)
OV7670_REG_AWBC1              = const(0x43)
OV7670_REG_AWBC2              = const(0x44)
OV7670_REG_AWBC3              = const(0x45)
OV7670_REG_AWBC4              = const(0x46)
OV7670_REG_AWBC5              = const(0x47)
OV7670_REG_AWBC6              = const(0x48)
OV7670_REG_REG4B              = const(0x4B)
OV7670_REG_DNSTH              = const(0x4C)
OV7670_REG_MTX1               = const(0x4F)
OV7670_REG_MTX2               = const(0x50)
OV7670_REG_MTX3               = const(0x51)
OV7670_REG_MTX4               = const(0x52)
OV7670_REG_MTX5               = const(0x53)
OV7670_REG_MTX6               = const(0x54)
OV7670_REG_BRIGHT             = const(0x55)
OV7670_REG_CONTRAS            = const(0x56)
OV7670_REG_CONTRAS_CENTER     = const(0x57)
OV7670_REG_MTXS               = const(0x58)
OV7670_REG_LCC1               = const(0x62)
OV7670_REG_LCC2               = const(0x63)
OV7670_REG_LCC3               = const(0x64)
OV7670_REG_LCC4               = const(0x65)
OV7670_REG_LCC5               = const(0x66)
OV7670_REG_MANU               = const(0x67)
OV7670_REG_MANV               = const(0x68)
OV7670_REG_GFIX               = const(0x69)
OV7670_REG_GGAIN              = const(0x6A)
OV7670_REG_DBLV               = const(0x6B)
OV7670_REG_AWBCTR3            = const(0x6C)
OV7670_REG_AWBCTR2            = const(0x6D)
OV7670_REG_AWBCTR1            = const(0x6E)
OV7670_REG_AWBCTR0            = const(0x6F)
OV7670_REG_SCALING_XSC        = const(0x70)
OV7670_REG_SCALING_YSC        = const(0x71)
OV7670_REG_SCALING_DCWCTR     = const(0x72)
OV7670_REG_SCALING_PCLK_DIV   = const(0x73)
OV7670_REG_REG74              = const(0x74)
OV7670_REG_REG76              = const(0x76)
OV7670_REG_SLOP               = const(0x7A)
OV7670_REG_GAM_BASE           = const(0x7B)
OV7670_R76_BLKPCOR            = const(0x80)
OV7670_R76_WHTPCOR            = const(0x40)
OV7670_REG_RGB444             = const(0x8C)
OV7670_REG_DM_LNL             = const(0x92)
OV7670_REG_LCC6               = const(0x94)
OV7670_REG_LCC7               = const(0x95)
OV7670_REG_HAECC1             = const(0x9F)
OV7670_REG_HAECC2             = const(0xA0)
OV7670_REG_SCALING_PCLK_DELAY = const(0xA2)
OV7670_REG_BD50MAX            = const(0xA5)
OV7670_REG_HAECC3             = const(0xA6)
OV7670_REG_HAECC4             = const(0xA7)
OV7670_REG_HAECC5             = const(0xA8)
OV7670_REG_HAECC6             = const(0xA9)
OV7670_REG_HAECC7             = const(0xAA)
OV7670_REG_BD60MAX            = const(0xAB)
OV7670_REG_ABLC1              = const(0xB1)
OV7670_REG_THL_ST             = const(0xB3)
OV7670_REG_SATCTR             = const(0xC9)

class OV7670:
    def __init__(
        self,
        i2c_bus: machine.I2C,
        mclk_pin_no: int,
        pclk_pin_no: int,
        data_pin_base: int,
        vsync_pin_no: int,
        href_pin_no: int,
        reset_pin_no: int,
        shutdown_pin_no: Optional[int] = None,
        i2c_id: int = 0x21,
        mclk_frequency: int = 16000000,
    ):
        self.i2c = i2c_bus
        self.mclk_pin = machine.Pin(mclk_pin_no)
        self.reset_pin = machine.Pin(reset_pin_no, machine.Pin.OUT)
        self.shutdown_pin = machine.Pin(shutdown_pin_no, machine.Pin.OUT) if shutdown_pin_no else None
        for i in range(8):
            machine.Pin(data_pin_base + i, machine.Pin.IN)
        self.i2c_id = i2c_id
        self.mclk_frequency = mclk_frequency

        self.mclk_pwm = machine.PWM(self.mclk_pin, freq=mclk_frequency, duty_u16=32768)

        if self.shutdown_pin:
            self.shutdown_pin.value(1)
            time.sleep(0.001)
            self.shutdown_pin.value(0)
            time.sleep(0.3)

        self.reset_pin.value(0)
        time.sleep(0.001)
        self.reset_pin.value(1)
        time.sleep(0.001)

        i2c_subordinates = self.i2c.scan()
        if i2c_id not in i2c_subordinates:
            raise Exception(f"I2C device {i2c_id} not found on bus. Check your wiring.")

        @rp2.asm_pio(in_shiftdir=rp2.PIO.SHIFT_RIGHT, push_thresh=32, autopush=True)
        def pio_capture():
            wait(0, gpio, vsync_pin_no)
            wait(1, gpio, vsync_pin_no)
            wrap_target()
            wait(1, gpio, href_pin_no)
            wait(1, gpio, pclk_pin_no)
            in_(pins, 8)
            wait(0, gpio, pclk_pin_no)
            wrap()
        self.sm = rp2.StateMachine(0, pio_capture, in_base=machine.Pin(data_pin_base))
        self.dma = rp2.DMA()
        self.dma_ctrl = self.dma.pack_ctrl(inc_read=False, treq_sel=4)

    def write_register(self, reg: int, value: int):
        self.i2c.writeto(self.i2c_id, bytearray([reg, value]))

    def read_register(self, reg: int) -> int:
        self.i2c.writeto(self.i2c_id, bytearray([reg]))
        return self.i2c.readfrom(self.i2c_id, 1)[0]

    def capture(self, buf: bytearray):
        self.dma.config(
            read=self.sm,
            write=buf,
            count=len(buf)//4,
            trigger=False,
            ctrl=self.dma_ctrl,
        )
        self.sm.active(0)
        self.sm.restart()
        self.sm.active(1)
        self.dma.active(1)
        while self.dma.active():
            pass
        self.sm.active(0)
