# pyssd1306.py
import os
import shutil
import uvicorn
import logging
from oled.display import create_display
from utils.config import MasterConfig
from utils.logger import log_function, get_logger, set_log_level,set_log_directory
from version import VERSION


logger = get_logger("app")

def main():
    logger.info("starting light-oled-display(version: {})...".format(VERSION))
    cur_dir = os.path.dirname(os.path.abspath(__file__))
    config_file = os.path.join(cur_dir, "conf", "config.yaml")
    if not os.path.exists(config_file):
        # if config.yaml not found, copy sample config file
        shutil.copyfile(os.path.join(cur_dir, "conf", "config_sample.yaml"), config_file)   
    
    config = MasterConfig(config_file)
    
    log_level = config.get_config('log', 'level', default='info')
    log_dir = config.get_config('log', 'dir', default='logs')
    
    # 设置全局日志级别
    set_log_level(getattr(logging, log_level.upper()))
    # 设置日志目录
    set_log_directory(log_dir)

    display = create_display()
    display.display_text_line('Disp OK.', 8, 8)
    
    # start_flask_app(display)
    uvicorn.run("web.fastapi_api:app", host="127.0.0.1", port=8003, log_level=log_level, reload=False)
    

if __name__ == "__main__":
    main()