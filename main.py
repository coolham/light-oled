# pyssd1306.py
import os
import shutil
import uvicorn
import logging
from oled.display import create_display
from utils.config import MasterConfig
from utils.logger import log_function, get_logger, set_log_level, set_log_directory
from version import VERSION

# 创建一个专门用于启动信息的logger
startup_logger = logging.getLogger("startup")
startup_logger.setLevel(logging.INFO)
startup_handler = logging.StreamHandler()
startup_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
startup_handler.setFormatter(startup_formatter)
startup_logger.addHandler(startup_handler)

logger = get_logger("app")

def main():
    startup_logger.info("Starting light-oled-display (version: {})...".format(VERSION))
    cur_dir = os.path.dirname(os.path.abspath(__file__))
    config_file = os.path.join(cur_dir, "conf", "config.yaml")
    if not os.path.exists(config_file):
        shutil.copyfile(os.path.join(cur_dir, "conf", "config_sample.yaml"), config_file)   
    
    config = MasterConfig(config_file)
    
    log_level = config.get_config('log', 'level', default='info')
    log_path = config.get_config('log', 'path', default='logs')
    
    # 设置全局日志级别
    print("log_level: {}".format(log_level))
    set_log_level(getattr(logging, log_level.upper()))
    # 设置日志目录
    set_log_directory(log_path)

    display = create_display()
    display.display_text_line('Disp OK.', 8, 8)
    
    uvicorn.run("web.fastapi_api:app", host="127.0.0.1", port=8003, log_level=log_level, reload=False)

if __name__ == "__main__":
    main()