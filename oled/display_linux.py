import time
from oled.display_base import DisplayBase
from PIL import Image, ImageDraw, ImageFont
from utils.config import MasterConfig

# 在Linux上运行时需要的库
try:
    from luma.core.interface.serial import i2c
    from luma.core.render import canvas
    from luma.oled.device import ssd1306
except ImportError:
    # 在Windows上不会导入这些库
    pass


class LinuxDisplay(DisplayBase):
    """
    Linux系统下的显示实现
    """
    def __init__(self):
        self.config = MasterConfig()
        self.en_font_file = self.config.get_config("fonts", "en_font_file")
        self.cn_font_file = self.config.get_config("fonts", "cn_font_file")
        self.i2c_port = self.config.get_config("ssd1306", "i2c_port")
        self.serial = i2c(port=self.i2c_port, address=0x3C)
        self.device = ssd1306(self.serial)
        self.en_font = None
        self.cn_font = None
        self.init_font()
       
    def init_font(self):
         self.en_font = ImageFont.truetype(self.en_font_file, 16)
         self.cn_font = ImageFont.truetype(self.cn_font_file, 32)
        
    def display_text(self, text, x, y):
        # 在SSD1306上显示文本的实现
        with canvas(self.device) as draw:
            draw.text((x, y), text, font=self.en_font, fill="white")

    def clear(self):
        # 清除屏幕的实现
        pass
    
    