import os
from abc import ABC, abstractmethod
from oled.display_windows import WindowsDisplay
from oled.display_linux import LinuxDisplay



# 根据操作系统创建不同的显示实例
def create_display():
    if os.name == 'nt':  # Windows系统
        return WindowsDisplay()
    else:  # 假设非Windows系统为Linux
        return LinuxDisplay()
    
    