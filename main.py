# main.py
import sys
from PyQt5 import QtWidgets
from calculator import Calculator
from qt_ui import CalculatorUI

def main():
    # 创建应用
    app = QtWidgets.QApplication(sys.argv)
    
    # 创建计算器实例
    calculator = Calculator()
    
    # 创建UI
    window = CalculatorUI(calculator)
    window.show()
    
    print("计算器已启动!")
    
    # 运行应用
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()