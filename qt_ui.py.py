# qt_ui.py
from PyQt5 import QtWidgets, QtCore

class Ui_CalculatorWindow(object):
    def setupUi(self, CalculatorWindow):
        CalculatorWindow.setObjectName("CalculatorWindow")
        CalculatorWindow.resize(400, 500)
        CalculatorWindow.setWindowTitle("Advanced Calculator")
        self.centralwidget = QtWidgets.QWidget(CalculatorWindow)
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        
        # 显示屏
        self.display = QtWidgets.QLineEdit(self.centralwidget)
        self.display.setReadOnly(True)
        self.display.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.verticalLayout.addWidget(self.display)
        
        # 选项卡
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        
        # 基本选项卡
        self.basicTab = QtWidgets.QWidget()
        self.gridLayout = QtWidgets.QGridLayout(self.basicTab)
        
        # 创建基本按钮
        self.button7 = QtWidgets.QPushButton("7", self.basicTab)
        self.gridLayout.addWidget(self.button7, 0, 0, 1, 1)
        self.button8 = QtWidgets.QPushButton("8", self.basicTab)
        self.gridLayout.addWidget(self.button8, 0, 1, 1, 1)
        self.button9 = QtWidgets.QPushButton("9", self.basicTab)
        self.gridLayout.addWidget(self.button9, 0, 2, 1, 1)
        self.buttonDivide = QtWidgets.QPushButton("/", self.basicTab)
        self.gridLayout.addWidget(self.buttonDivide, 0, 3, 1, 1)
        
        self.button4 = QtWidgets.QPushButton("4", self.basicTab)
        self.gridLayout.addWidget(self.button4, 1, 0, 1, 1)
        self.button5 = QtWidgets.QPushButton("5", self.basicTab)
        self.gridLayout.addWidget(self.button5, 1, 1, 1, 1)
        self.button6 = QtWidgets.QPushButton("6", self.basicTab)
        self.gridLayout.addWidget(self.button6, 1, 2, 1, 1)
        self.buttonMultiply = QtWidgets.QPushButton("*", self.basicTab)
        self.gridLayout.addWidget(self.buttonMultiply, 1, 3, 1, 1)
        
        self.button1 = QtWidgets.QPushButton("1", self.basicTab)
        self.gridLayout.addWidget(self.button1, 2, 0, 1, 1)
        self.button2 = QtWidgets.QPushButton("2", self.basicTab)
        self.gridLayout.addWidget(self.button2, 2, 1, 1, 1)
        self.button3 = QtWidgets.QPushButton("3", self.basicTab)
        self.gridLayout.addWidget(self.button3, 2, 2, 1, 1)
        self.buttonSubtract = QtWidgets.QPushButton("-", self.basicTab)
        self.gridLayout.addWidget(self.buttonSubtract, 2, 3, 1, 1)
        
        self.button0 = QtWidgets.QPushButton("0", self.basicTab)
        self.gridLayout.addWidget(self.button0, 3, 0, 1, 1)
        self.buttonDot = QtWidgets.QPushButton(".", self.basicTab)
        self.gridLayout.addWidget(self.buttonDot, 3, 1, 1, 1)
        self.buttonEqual = QtWidgets.QPushButton("=", self.basicTab)
        self.gridLayout.addWidget(self.buttonEqual, 3, 2, 1, 1)
        self.buttonAdd = QtWidgets.QPushButton("+", self.basicTab)
        self.gridLayout.addWidget(self.buttonAdd, 3, 3, 1, 1)
        
        self.buttonClear = QtWidgets.QPushButton("C", self.basicTab)
        self.gridLayout.addWidget(self.buttonClear, 4, 0, 1, 1)
        self.buttonPower = QtWidgets.QPushButton("^", self.basicTab)
        self.gridLayout.addWidget(self.buttonPower, 4, 1, 1, 1)
        self.buttonSqrt = QtWidgets.QPushButton("√", self.basicTab)
        self.gridLayout.addWidget(self.buttonSqrt, 4, 2, 1, 1)
        
        self.tabWidget.addTab(self.basicTab, "Basic")
        
        # 科学选项卡
        self.scientificTab = QtWidgets.QWidget()
        self.scientificGrid = QtWidgets.QGridLayout(self.scientificTab)
        
        self.buttonSin = QtWidgets.QPushButton("sin", self.scientificTab)
        self.scientificGrid.addWidget(self.buttonSin, 0, 0, 1, 1)
        self.buttonCos = QtWidgets.QPushButton("cos", self.scientificTab)
        self.scientificGrid.addWidget(self.buttonCos, 0, 1, 1, 1)
        self.buttonTan = QtWidgets.QPushButton("tan", self.scientificTab)
        self.scientificGrid.addWidget(self.buttonTan, 0, 2, 1, 1)
        
        self.buttonArcsin = QtWidgets.QPushButton("arcsin", self.scientificTab)
        self.scientificGrid.addWidget(self.buttonArcsin, 1, 0, 1, 1)
        self.buttonArccos = QtWidgets.QPushButton("arccos", self.scientificTab)
        self.scientificGrid.addWidget(self.buttonArccos, 1, 1, 1, 1)
        self.buttonArctan = QtWidgets.QPushButton("arctan", self.scientificTab)
        self.scientificGrid.addWidget(self.buttonArctan, 1, 2, 1, 1)
        
        self.buttonLog = QtWidgets.QPushButton("log", self.scientificTab)
        self.scientificGrid.addWidget(self.buttonLog, 2, 0, 1, 1)
        self.buttonLn = QtWidgets.QPushButton("ln", self.scientificTab)
        self.scientificGrid.addWidget(self.buttonLn, 2, 1, 1, 1)
        self.buttonFactorial = QtWidgets.QPushButton("n!", self.scientificTab)
        self.scientificGrid.addWidget(self.buttonFactorial, 2, 2, 1, 1)
        
        self.buttonPi = QtWidgets.QPushButton("π", self.scientificTab)
        self.scientificGrid.addWidget(self.buttonPi, 3, 0, 1, 1)
        self.buttonE = QtWidgets.QPushButton("e", self.scientificTab)
        self.scientificGrid.addWidget(self.buttonE, 3, 1, 1, 1)
        self.buttonAbs = QtWidgets.QPushButton("|x|", self.scientificTab)
        self.scientificGrid.addWidget(self.buttonAbs, 3, 2, 1, 1)
        
        self.buttonIsPrime = QtWidgets.QPushButton("isPrime", self.scientificTab)
        self.scientificGrid.addWidget(self.buttonIsPrime, 4, 0, 1, 1)
        self.buttonGCD = QtWidgets.QPushButton("GCD", self.scientificTab)
        self.scientificGrid.addWidget(self.buttonGCD, 4, 1, 1, 1)
        self.buttonLCM = QtWidgets.QPushButton("LCM", self.scientificTab)
        self.scientificGrid.addWidget(self.buttonLCM, 4, 2, 1, 1)
        
        self.tabWidget.addTab(self.scientificTab, "Scientific")
        self.verticalLayout.addWidget(self.tabWidget)
        CalculatorWindow.setCentralWidget(self.centralwidget)
        
        # 菜单栏
        self.menubar = QtWidgets.QMenuBar(CalculatorWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 22))
        self.menuMode = QtWidgets.QMenu("Mode", self.menubar)
        CalculatorWindow.setMenuBar(self.menubar)
        
        self.actionDegrees = QtWidgets.QAction("Degrees", CalculatorWindow)
        self.actionDegrees.setCheckable(True)
        self.actionDegrees.setChecked(True)
        self.actionRadians = QtWidgets.QAction("Radians", CalculatorWindow)
        self.actionRadians.setCheckable(True)
        
        self.menuMode.addAction(self.actionDegrees)
        self.menuMode.addAction(self.actionRadians)
        self.menubar.addAction(self.menuMode.menuAction())

class CalculatorUI(QtWidgets.QMainWindow):
    def __init__(self, calculator):
        super().__init__()
        self.ui = Ui_CalculatorWindow()
        self.ui.setupUi(self)
        self.calculator = calculator
        
        # 状态变量
        self.first_operand = None
        self.second_operand = None
        self.operator = None
        self.awaiting_operand = True
        self.use_degrees = True
        self.pending_function = None  # 待执行的科学函数
        
        # 连接基本数字按钮
        self.ui.button0.clicked.connect(lambda: self.digit_pressed("0"))
        self.ui.button1.clicked.connect(lambda: self.digit_pressed("1"))
        self.ui.button2.clicked.connect(lambda: self.digit_pressed("2"))
        self.ui.button3.clicked.connect(lambda: self.digit_pressed("3"))
        self.ui.button4.clicked.connect(lambda: self.digit_pressed("4"))
        self.ui.button5.clicked.connect(lambda: self.digit_pressed("5"))
        self.ui.button6.clicked.connect(lambda: self.digit_pressed("6"))
        self.ui.button7.clicked.connect(lambda: self.digit_pressed("7"))
        self.ui.button8.clicked.connect(lambda: self.digit_pressed("8"))
        self.ui.button9.clicked.connect(lambda: self.digit_pressed("9"))
        self.ui.buttonDot.clicked.connect(lambda: self.digit_pressed("."))
        
        # 连接基本操作按钮
        self.ui.buttonAdd.clicked.connect(lambda: self.operation_pressed("+"))
        self.ui.buttonSubtract.clicked.connect(lambda: self.operation_pressed("-"))
        self.ui.buttonMultiply.clicked.connect(lambda: self.operation_pressed("*"))
        self.ui.buttonDivide.clicked.connect(lambda: self.operation_pressed("/"))
        self.ui.buttonPower.clicked.connect(lambda: self.operation_pressed("^"))
        self.ui.buttonEqual.clicked.connect(self.equal_pressed)
        self.ui.buttonClear.clicked.connect(self.clear_pressed)
        
        # 连接单目运算按钮 - 设置待执行函数
        self.ui.buttonSqrt.clicked.connect(lambda: self.function_pressed("sqrt"))
        
        # 连接三角函数按钮 - 设置待执行函数
        self.ui.buttonSin.clicked.connect(lambda: self.function_pressed("sin"))
        self.ui.buttonCos.clicked.connect(lambda: self.function_pressed("cos"))
        self.ui.buttonTan.clicked.connect(lambda: self.function_pressed("tan"))
        self.ui.buttonArcsin.clicked.connect(lambda: self.function_pressed("arcsin"))
        self.ui.buttonArccos.clicked.connect(lambda: self.function_pressed("arccos"))
        self.ui.buttonArctan.clicked.connect(lambda: self.function_pressed("arctan"))
        
        # 连接其他科学计算按钮
        self.ui.buttonLog.clicked.connect(lambda: self.operation_pressed("log"))
        self.ui.buttonLn.clicked.connect(lambda: self.function_pressed("ln"))
        self.ui.buttonFactorial.clicked.connect(lambda: self.function_pressed("factorial"))
        self.ui.buttonPi.clicked.connect(self.pi_pressed)
        self.ui.buttonE.clicked.connect(self.e_pressed)
        self.ui.buttonAbs.clicked.connect(lambda: self.function_pressed("abs"))
        self.ui.buttonIsPrime.clicked.connect(lambda: self.function_pressed("isPrime"))
        self.ui.buttonGCD.clicked.connect(lambda: self.operation_pressed("gcd"))
        self.ui.buttonLCM.clicked.connect(lambda: self.operation_pressed("lcm"))
        
        # 连接角度/弧度切换
        self.ui.actionDegrees.triggered.connect(lambda: self.set_angle_mode(True))
        self.ui.actionRadians.triggered.connect(lambda: self.set_angle_mode(False))
        
        # 初始化显示
        self.ui.display.setText("0")
    
    def digit_pressed(self, digit):
        current_text = self.ui.display.text()
        if self.awaiting_operand:
            self.ui.display.setText(digit)
            self.awaiting_operand = False
        else:
            self.ui.display.setText(current_text + digit)
    
    def operation_pressed(self, op):
        # 如果有待执行的函数，先执行
        if self.pending_function:
            self.apply_pending_function()
        current_text = self.ui.display.text()
        try:
            self.first_operand = float(current_text)
            self.operator = op
            self.awaiting_operand = True
        except ValueError:
            self.ui.display.setText("Error")
            self.awaiting_operand = True
    
    # 设置待执行的函数
    def function_pressed(self, func_name):
        self.pending_function = func_name
        # 不立即清除显示，允许用户输入参数
        if not self.awaiting_operand:
            self.ui.display.setText(f"{func_name}({self.ui.display.text()})")
            self.awaiting_operand = True
        else:
            self.ui.display.setText(f"{func_name}()")
            self.awaiting_operand = True
    
    # 应用待执行的函数
    def apply_pending_function(self):
        if not self.pending_function:
            return
        try:
            current_text = self.ui.display.text()
            # 如果显示的是函数名，提取括号内的参数
            if "(" in current_text and ")" in current_text:
                param_text = current_text[current_text.find("(")+1:current_text.find(")")]
                if param_text:
                    value = float(param_text)
                else:
                    value = 0
            else:
                value = float(current_text)
            result = 0
            if self.pending_function == "sqrt":
                result = self.calculator.sqrt(value)
            elif self.pending_function == "sin":
                result = self.calculator.sin(value, self.use_degrees)
            elif self.pending_function == "cos":
                result = self.calculator.cos(value, self.use_degrees)
            elif self.pending_function == "tan":
                result = self.calculator.tan(value, self.use_degrees)
            elif self.pending_function == "arcsin":
                result = self.calculator.arcsin(value, self.use_degrees)
            elif self.pending_function == "arccos":
                result = self.calculator.arccos(value, self.use_degrees)
            elif self.pending_function == "arctan":
                result = self.calculator.arctan(value, self.use_degrees)
            elif self.pending_function == "ln":
                result = self.calculator.ln(value)
            elif self.pending_function == "factorial":
                result = self.calculator.factorial(int(value))
            elif self.pending_function == "abs":
                result = abs(value)
            elif self.pending_function == "isPrime":
                result = "Yes" if self.calculator.isPrime(int(value)) else "No"
            self.ui.display.setText(str(result))
            self.pending_function = None
            self.awaiting_operand = True
        except Exception as e:
            self.ui.display.setText(f"Error: {str(e)}")
            self.pending_function = None
            self.awaiting_operand = True
    
    def equal_pressed(self):
        # 如果有待执行的函数，先执行
        if self.pending_function:
            self.apply_pending_function()
            return
        if self.operator is None:
            return
        current_text = self.ui.display.text()
        try:
            self.second_operand = float(current_text)
            result = 0
            if self.operator == "+":
                result = self.calculator.add(self.first_operand, self.second_operand)
            elif self.operator == "-":
                result = self.calculator.subtract(self.first_operand, self.second_operand)
            elif self.operator == "*":
                result = self.calculator.multiply(self.first_operand, self.second_operand)
            elif self.operator == "/":
                result = self.calculator.divide(self.first_operand, self.second_operand)
            elif self.operator == "^":
                result = self.calculator.power(self.first_operand, self.second_operand)
            elif self.operator == "log":
                result = self.calculator.log(self.second_operand, self.first_operand)
            elif self.operator == "gcd":
                result = self.calculator.gcd(int(self.first_operand), int(self.second_operand))
            elif self.operator == "lcm":
                result = self.calculator.lcm(int(self.first_operand), int(self.second_operand))
            self.ui.display.setText(str(result))
            self.first_operand = result
            self.operator = None
            self.awaiting_operand = True
        except Exception as e:
            self.ui.display.setText(f"Error: {str(e)}")
            self.awaiting_operand = True
    
    def clear_pressed(self):
        self.ui.display.setText("0")
        self.first_operand = None
        self.second_operand = None
        self.operator = None
        self.pending_function = None  # 清除待执行的函数
        self.awaiting_operand = True
    
    def pi_pressed(self):
        import math
        self.ui.display.setText(str(math.pi))
        self.awaiting_operand = True
    
    def e_pressed(self):
        import math
        self.ui.display.setText(str(math.e))
        self.awaiting_operand = True
    
    def set_angle_mode(self, use_degrees):
        self.use_degrees = use_degrees
        self.ui.actionDegrees.setChecked(use_degrees)
        self.ui.actionRadians.setChecked(not use_degrees)