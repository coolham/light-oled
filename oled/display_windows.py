from oled.display_base import DisplayBase


class WindowsDisplay(DisplayBase):
    """
    Windows系统下的空实现
    """
    def display_text(self, text, x, y):
        print("Display not supported on Windows.")

    def display_multiline_text(self, lines):
        print(lines)
        print("Display not supported on Windows.")
        
    def clear(self):
        print("Display not supported on Windows.")
        
        
        