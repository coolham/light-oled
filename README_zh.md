
# SSD1306 显示服务

Welcome to the SSD1306 Display Service! Please choose the README in your preferred language:

- [Read this in English](README.md)
- [阅读中文版本](README_zh.md)

## 介绍
本项目提供了一个基于Flask的服务，通过简单的REST API来控制SSD1306 OLED显示屏。它支持显示文本、图像，并具有文本滚动功能。

* 这个程序只能运行在Linux类平台，需要使用I2C总线或者SPI总线来驱动SSD1306

## 特点
- 显示可调位置和大小的文本
- 在OLED屏幕上显示图像
- 清除显示屏
- 变速滚动文本
- 检查显示屏的当前状态

## 安装
运行此项目需要在系统上安装Python 3和pip。

1. 克隆仓库：
   ```
   git clone https://github.com/coolham/pyssd1306.git
   ```

2. 进入克隆的目录：
   ```
   cd pyssd1306
   ```

3. 安装所需包：
   ```
   pip install -r requirements.txt
   ```

也可以单独安装：

```
pip install flask
pip install Pillow
pip install luma.oled
pip install pyyaml
pip install flask
pip install fastapi
```


## 使用
运行以下命令启动服务：
```
python pyssd1306.py
```

API端点可在 `http://localhost:8080/` 访问。

## API 参考

- POST `/display/text`：显示文本
- POST `/display/image`：显示图像
- POST `/display/clear`：清除显示
- POST `/display/scroll`：滚动文本
- GET `/display/status`：获取显示屏的当前状态

## 贡献
欢迎贡献、问题和功能请求！请随时查看[问题页面](链接到你的问题页面)。

## 许可证
根据MIT许可证分发。有关更多信息，请参阅`LICENSE`文件。

## 联系方式

项目链接：https://github.com/coolham/pyssd1306
