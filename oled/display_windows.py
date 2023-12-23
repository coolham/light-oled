from oled.display_base import DisplayBase


class WindowsDisplay(DisplayBase):
    """
    Windows系统下的空实现
    """
    def display_text_line(self, text, x, y, font_size=24):
        print("Display not supported on Windows.")

    def display_text_multiline(self, lines):
        print(lines)
        print("Display not supported on Windows.")
        
    def clear(self):
        print("Display not supported on Windows.")
        
    def reset(self):
        print("Display not supported on Windows.")
        