import os
import time
from oled.display_base import DisplayBase
from PIL import Image, ImageDraw, ImageFont
from utils.config import MasterConfig
from helper import get_application_root
from utils.logger import log_function, get_logger

logger = get_logger("disp")


# 在Linux上运行时需要的库
try:
    from luma.core.interface.serial import i2c
    from luma.core.render import canvas
    from luma.oled.device import ssd1306
except ImportError:
    # 在Windows上不会导入这些库
    pass

"""
pip install pillow
"""

class LinuxDisplay(DisplayBase):
    """
    Linux系统下的显示实现
    """
    def __init__(self):
        self.config = MasterConfig()
        self.root_dir = get_application_root()
        self.i2c_port = int(self.config.get_config("ssd1306", "i2c_bus", default="0"))
        self.serial = i2c(port=self.i2c_port, address=0x3C)
        self.device = self._initialize_device()
        self.ch_font_file = None
        self.font_cache = {}
        self._init_font_cache()

    def _initialize_device(self, retries=3, delay=1):
        for attempt in range(retries):
            try:
                return ssd1306(self.serial)
            except Exception as e:
                logger.error("Failed to initialize SSD1306 device (attempt {}): {}".format(attempt + 1, e))
                time.sleep(delay)  # 等待一段时间后重试
        logger.error("All attempts to initialize SSD1306 device failed.")
        return None  # 所有尝试失败后返回None

    def _init_font_cache(self):
        font_ch_file = self.config.get_config("fonts", "ch_font", "file")
        if font_ch_file:
            self.ch_font_file = os.path.join(self.root_dir, font_ch_file)
            if not os.path.exists(self.ch_font_file):
                logger.error("chinese font file:{} not found!".format(self.ch_font_file))
            else:
                # font_size = int(self.config.get_config("fonts", "ch_font", "size", default="32"))
                # self.ch_font = ImageFont.truetype(self.ch_font_file, font_size)
                 # 预缓存特定大小的字体
                font_size = [16, 20, 24, 28, 32]
                for size in font_size:
                    self.font_cache[size] = ImageFont.truetype(self.ch_font_file, size)

                logger.info("chinese font file:{} loaded. size={}".format(self.ch_font_file, font_size))
        else:
            logger.error("chinese font file not specified!")
       
    def _get_font(self, font_size):
        # 从缓存获取字体，如果请求的大小不在预设范围内，则动态创建
        if not font_size:
            font_size = 24
            logger.info("font_size not specified, use default: {}".format(font_size))
        else:
            font_size = int(font_size)
            logger.debug("font_size specified: {}".format(font_size))
            
        return self.font_cache.get(font_size) or ImageFont.truetype(self.ch_font_file, font_size)
            
    def _contains_chinese(self, text):
        for ch in text:
            if '\u4e00' <= ch <= '\u9fff':
                return True
        return False
                        
    def display_text_line(self, text, x, y, font_size=None):
        font = self._get_font(font_size)
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
                font = self._get_font(line.get('font_size'))
                draw.text((x, y), text, font=font, fill="white")
                    
    def clear(self):
        logger.info("clear display")
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
        self.device = self._initialize_device()  # 调用新的初始化方法
        self.init_font()  # 重新初始化字体

        # 可选：清除屏幕
        self.clear()

    def display_marquee_text(self, text, font_size=None, speed=0.1):
        """
        以跑马灯形式显示文本。
        
        :param text: 要显示的文本
        :param font_size: 字体大小
        :param speed: 滚动速度（秒）
        """
        font = self._get_font(font_size)
        text_width, text_height = font.getsize(text)
        width = self.device.width
        height = self.device.height

        # 初始位置在屏幕右侧外
        x = width
        y = (height - text_height) // 2

        while x + text_width > 0:
            with canvas(self.device) as draw:
                draw.text((x, y), text, font=font, fill="white")
            x -= 1  # 每次向左移动一个像素
            time.sleep(speed)  # 控制滚动速度