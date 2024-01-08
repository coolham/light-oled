import os
from abc import ABC, abstractmethod

class DisplayBase(ABC):
    """
    抽象显示类，定义了显示功能的基本接口
    """
    @abstractmethod
    def display_text_line(self, text, x, y):
        pass

    @abstractmethod
    def clear(self):
        pass
    
    def to_halfwidth(s):
        # 全角数字、英文字母和符号的 Unicode 码范围
        fullwidth_chars = (
            '０１２３４５６７８９'
            'ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ'
            'ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ'
            '！＂＃＄％＆＇（）＊＋，－．／：；＜＝＞？＠［＼］＾＿｀｛｜｝～'
        )
        # 对应的半角字符
        halfwidth_chars = (
            '0123456789'
            'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            'abcdefghijklmnopqrstuvwxyz'
            '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
        )

        # 创建映射表
        mapping_table = str.maketrans(halfwidth_chars, fullwidth_chars)

        # 转换字符串
        return s.translate(mapping_table)


