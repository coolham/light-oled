import os
import time
from oled.display_base import DisplayBase
from PIL import Image, ImageDraw, ImageFont
from utils.config import MasterConfig
from utils.logger_factory import create_logger
from helper import get_application_root


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
        self.root_dir = get_application_root()
        self.i2c_port = int(self.config.get_config("ssd1306", "i2c_bus", default="0"))
        self.serial = i2c(port=self.i2c_port, address=0x3C)
        self.device = ssd1306(self.serial)
        self.en_font_file = None
        self.ch_font_file = None
        self.en_font = None
        self.ch_font = None
        self.init_font()
       
    def init_font(self):
        font_en_file = self.config.get_config("fonts", "en_font", "file")
        if font_en_file:
            self.en_font_file = os.path.join(self.root_dir, font_en_file)
            if not os.path.exists(self.en_font_file ):
                self.logger.error("english font file:{} not found!".format(self.en_font_file ))
            else:
                self.en_font = ImageFont.truetype(self.en_font_file, 16)
                self.logger.info("english font file:{} loaded.".format(self.en_font_file))
        else:
            self.logger.error("english font file not specified!")
                 
        font_ch_file = self.config.get_config("fonts", "ch_font", "file")
        if font_ch_file:
            self.ch_font_file = os.path.join(self.root_dir, font_ch_file)
            if not os.path.exists(self.ch_font_file):
                self.logger.error("chinese font file:{} not found!".format(self.ch_font_file))
            else:
                self.ch_font = ImageFont.truetype(self.ch_font_file, 32)
                self.logger.info("chinese font file:{} loaded.".format(self.ch_font_file))
        else:
            self.logger.error("chinese font file not specified!")
            
    def _contains_chinese(self, text):
        for ch in text:
            if '\u4e00' <= ch <= '\u9fff':
                return True
        return False
                        
    def display_text_line(self, text, x, y):
        # 检测是否包含中文
        if self._contains_chinese(text):
            font = self.ch_font
            self.logger.info("display chinese text:{}".format(text))
        else:
            font = self.en_font
        # 在SSD1306上显示文本的实现
        with canvas(self.device) as draw:
            draw.text((x, y), text, font=font, fill="white")
        return True
    
    def display_text_multiline(self, lines):
        """
        显示多行文本，其中每一行都可以指定独立的(x, y)位置。
        lines 参数是一个列表，每个元素是一个字典，包含 'text', 'x', 和 'y' 键。
        """
        with canvas(self.device) as draw:
            for line in lines:
                text = line['text']
                x = line['x']
                y = line['y']
                # 选择合适的字体
                font = self.cn_font if self._contains_chinese(text) else self.en_font
                draw.text((x, y), text, font=font, fill="white")
                    
    def clear(self):
        self.logger.info("clear display")
        # 使用黑色矩形覆盖整个屏幕来清除内容
        with canvas(self.device) as draw:
            draw.rectangle(self.device.bounding_box, outline="black", fill="black")
    

    def reset(self):
        """
        重新初始化SSD1306显示屏。
        """
        # 关闭当前设备连接（如果需要的话）
        if self.device:
            self.device.cleanup()

        # 重新初始化设备
        self.serial = i2c(port=self.i2c_port, address=0x3C)
        self.device = ssd1306(self.serial)
        self.init_font()  # 重新初始化字体

        # 可选：清除屏幕
        self.clear()