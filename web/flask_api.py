# web/flask_api.py
from flask import Flask
from utils.config import MasterConfig


app = Flask(__name__)

# 假设 display 是从 pyssd1306.py 传递过来的
def start_flask_app(display):
    @app.route('/display/text', methods=['POST'])
    def display_text():
        # 实现文本显示的逻辑
        pass

    @app.route('/display/image', methods=['POST'])
    def display_image():
        # 实现图像显示的逻辑
        pass
    
    @app.route('/display/clear', methods=['POST'])
    def clear_display():
        # 实现清屏的逻辑
        pass    
    
    @app.route('/display/scroll', methods=['POST'])
    def scroll_text():
        # 实现文本滚动的逻辑
        pass

    @app.route('/display/status', methods=['GET'])
    def display_status():
        # 实现状态查询的逻辑
        pass

    @app.route('/display/test', methods=['POST'])
    def test_text():
        # 实现文本滚动的逻辑
        display.display_text("Hello World!", 0, 0)



    # flask server
    config = MasterConfig()
    port = config.get_config("server", "port")
    app.run(host='0.0.0.0', port=port)