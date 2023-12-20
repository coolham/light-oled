# pyssd1306.py
import os
from oled.display import create_display
from web.flask_api import start_flask_app
from utils.config import MasterConfig
from utils.logger_factory import create_logger

def main():
    display = create_display()
    display.display_text('Init OK.', 8, 8)
    start_flask_app(display)

if __name__ == "__main__":
    logger = create_logger('main')
    logger.info("starting pyssd1306...")
    cur_dir = os.path.dirname(os.path.abspath(__file__))
    config_file = os.path.join(cur_dir, "conf", "config.yaml")
    config = MasterConfig(config_file)
    main()