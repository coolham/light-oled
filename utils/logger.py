import os
import logging
from logging.handlers import TimedRotatingFileHandler
import datetime
from functools import wraps
from contextlib import contextmanager
import functools
import inspect


# Modifying the Logger class to ensure all log messages are written to the same file

class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self, log_dir='logs'):
        print("Logger _initialize: {}".format(log_dir))
        now_str = datetime.datetime.now().strftime('%Y%m%d')
        
        # 检查并创建日志目录
        if not os.path.exists(log_dir):
            try:
                os.makedirs(log_dir)
            except Exception as e:
                print(f"Failed to create log directory {log_dir}: {e}")
                log_dir = 'logs'  # 回退到默认目录
                if not os.path.exists(log_dir):
                    os.makedirs(log_dir)

        log_file = f'light_oled_{now_str}.log'
        log_file = os.path.join(log_dir, log_file)

        self.root_logger = logging.getLogger()

        # 移除所有现有的处理器
        for handler in self.root_logger.handlers[:]:
            self.root_logger.removeHandler(handler)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(filename)s:%(lineno)d')

        file_handler = TimedRotatingFileHandler(log_file, when='D', interval=1, backupCount=30, encoding='utf-8')
        file_handler.setFormatter(formatter)
        self.root_logger.addHandler(file_handler)

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        self.root_logger.addHandler(console_handler)

    def set_log_directory(self, log_dir):
        print("Logger set_log_directory: {}".format(log_dir))
        self._initialize(log_dir)

    def get_logger(self, name=None):
        if name is None:
            return logging.getLogger("app")
        return logging.getLogger(name)

    def set_level(self, level):
        print("Logger set_level: {}".format(level))
        self.root_logger.setLevel(level)

# 全局logger实例
logger_instance = Logger()

def get_logger(name=None):
    return logger_instance.get_logger(name)

def set_log_level(level):
    logger_instance.set_level(level)

def set_logger_level(name, level):
    logger = logging.getLogger(name)
    logger.setLevel(level)

def set_log_directory(log_dir):
    logger_instance.set_log_directory(log_dir)

# 在文件末尾添加这个函数
def set_module_log_level(module_name, level):
    set_logger_level(module_name, level)


# 添加这行来创建一个默认的 logger
logger = get_logger("app")

def log_function(level=logging.DEBUG):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # 获取被装饰函数所在的模块
            module = inspect.getmodule(func)
            
            # 尝试在模块中找到名为 'logger' 的变量
            module_logger = getattr(module, 'logger', None)
            
            # 如果模块中没有定义 logger，则使用默认的 "app" logger
            if module_logger is None:
                logger = logging.getLogger("app")
            else:
                logger = module_logger
            
            logger.log(level, f"Entering {func.__name__} - {func.__code__.co_filename}:{func.__code__.co_firstlineno}")
            result = func(*args, **kwargs)
            logger.log(level, f"Exiting {func.__name__}")
            return result
        return wrapper
    return decorator

@contextmanager
def temporary_log_level(new_level, logger_name=None):
    logger = get_logger(logger_name)
    old_level = logger.level
    logger.setLevel(new_level)
    try:
        yield
    finally:
        logger.setLevel(old_level)

# 使用示例
@log_function(level=logging.DEBUG)
def example_function():
    logger = get_logger()
    logger.info("This is an info message")
    with temporary_log_level(logging.DEBUG):
        logger.debug("This is a temporary debug message")
    logger.info("Back to info level")

if __name__ == "__main__":
    example_function()

    # 测试自定义 logger 名称
    custom_logger = get_logger("panel")
    custom_logger.info("This is a message from the panel logger")


