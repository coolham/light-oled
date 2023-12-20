import os
import time
from oled.display_base import DisplayBase
from PIL import Image, ImageDraw, ImageFont
from utils.config import MasterConfig
from utils.logger_factory import create_logger

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
        self.logger = create_logger('oled')
        self.config = MasterConfig()
        self.en_font_file = self.config.get_config("fonts", "en_font", "file")
        self.ch_font_file = self.config.get_config("fonts", "ch_font", "file")
        self.i2c_port = int(self.config.get_config("ssd1306", "i2c_bus", default="0"))
        self.serial = i2c(port=self.i2c_port, address=0x3C)
        self.device = ssd1306(self.serial)
        self.en_font = None
        self.cn_font = None
        self.init_font()
       
    def init_font(self):
        if not self.en_font_file or not os.path.exists(self.en_font_file):
            self.logger.error("english font file:{} not found!".format(self.en_font_file))
        else:
            self.en_font = ImageFont.truetype(self.en_font_file, 16)
             
        if not self.ch_font_file or not os.path.exists(self.ch_font_file):
            self.logger.error("chinese font file:{} not found!".format(self.ch_font_file))
        else:
            self.ch_font = ImageFont.truetype(self.ch_font_file, 32)
    
                    
    def display_text(self, text, x, y):
        # 在SSD1306上显示文本的实现
        with canvas(self.device) as draw:
            draw.text((x, y), text, font=self.en_font, fill="white")
        return True
    
    def clear(self):
        # 清除屏幕的实现
        pass
    
    