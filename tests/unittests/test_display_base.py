import sys
import os

# 添加项目根目录到系统路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# 在VSCode中运行Python代码时,默认情况下是以启动Python进程时的当前工作目录为基准去搜索模块的。
sys.path.append(os.getcwd())


