# pyssd1306.py
import os
import uvicorn
from oled.display import create_display
from utils.config import MasterConfig
from utils.logger_factory import create_logger

def main():
    logger = create_logger('main')
    logger.info("starting pyssd1306...")
    cur_dir = os.path.dirname(os.path.abspath(__file__))
    config_file = os.path.join(cur_dir, "conf", "config.yaml")
    config = MasterConfig(config_file)
    
    display = create_display()
    display.display_text_line('Init OK.', 8, 8)
    
    # start_flask_app(display)
    uvicorn.run("web.fastapi_api:app", host="0.0.0.0", port=8003, reload=True)
    

if __name__ == "__main__":
    main()