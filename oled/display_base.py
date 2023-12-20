import os
from abc import ABC, abstractmethod

class DisplayBase(ABC):
    """
    抽象显示类，定义了显示功能的基本接口
    """
    @abstractmethod
    def display_text(self, text, x, y):
        pass

    @abstractmethod
    def clear(self):
        pass