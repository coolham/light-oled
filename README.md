
# SSD1306 Display Service

Welcome to the SSD1306 Display Service! Please choose the README in your preferred language:

- [Read this in English](README.md)
- [阅读中文版本](README_zh.md)

## Introduction
This project provides a FastAPI-based service to control an SSD1306 OLED display via a simple REST API. It allows displaying text, images, and supports text scrolling features. 

* This program can only run on Linux platforms and needs to use the I2C bus or SPI bus to drive the SSD1306

## Features
- Display text with adjustable position and size
- Show images on the OLED screen
- Clear the display
- Scroll text with variable speed
- Check the current status of the display

## Installation
To run this project, you need to have Python 3 and pip installed on your system.

1. Clone the repository:
 
```shell
git clone https://github.com/coolham/pyssd1306.git
```

2. Navigate to the cloned directory:

```shell
cd pyssd130
```

3. Create a Python virtual environment:

```shell
python3 -m venv venv
```

4. Install required packages:

```shell
pip install -r requirements.txt
```

or installed by manually:

```shell
pip install Pillow
pip install luma.oled
pip install pyyaml
pip install fastapi
```


5. Install font files

Download font files from [here](https://fonts.alibabagroup.com/#/font), and put them in the `fonts` directory.

For example, download [AlibabaPuHuiTi-3](https://puhuiti.oss-cn-hangzhou.aliyuncs.com/AlibabaPuHuiTi-3.zip)

```shell
cd fonts
unzip AlibabaPuHuiTi-3.zip
```

6. Edit the configuration file

'conf/config.yaml' is the configuration file for the service. You can edit it to change the default settings.


## Usage
Start the service by running:
```
python main.py
```

The API endpoints are accessible at `http://localhost:8080/`.

## API Reference
- POST `/display/text`: Display text
- POST `/display/image`: Display an image
- POST `/display/clear`: Clear the display
- POST `/display/scroll`: Scroll text
- GET `/display/status`: Get the current status of the display

## Contributing
Contributions, issues, and feature requests are welcome! Feel free to check [issues page](link-to-your-issues-page).

## License
Distributed under the MIT License. See `LICENSE` for more information.

## Contact


Project Link: https://github.com/coolham/pyssd1306
