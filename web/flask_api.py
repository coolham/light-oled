# web/flask_api.py
from flask import Flask, request, jsonify
from utils.config import MasterConfig


app = Flask(__name__)

# 假设 display 是从 pyssd1306.py 传递过来的
def start_flask_app(display):
    @app.route('/display/text', methods=['POST'])
    def display_text():
        # curl -X POST  -H 'Content-Type: application/json' -d '{"text":"Hello, SSD1306!", "x":10, "y":10}' http://localhost:8003/display/text
        data = request.json
        text = data.get('text', '')
        x = data.get('x', 0)
        y = data.get('y', 0)

        display.display_text(text, x, y)
        return jsonify({"code": 0, "message": "ok"})

        
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
        # curl -X POST  -H 'Content-Type: application/json' -d '{\"text\":\"Hello, SSD1306!\", \"x\":10, \"y\":10}' http://localhost:8003/display/test
        data = request.json
        text = data.get('text', '')
        x = data.get('x', 0)
        y = data.get('y', 0)

        display.display_text(text, x, y)
        return jsonify({"status": "Text displayed", "text": text, "x": x, "y": y})



    # flask server
    config = MasterConfig()
    port = config.get_config("server", "port")
    app.run(host='0.0.0.0', port=port)