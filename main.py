<<<<<<< HEAD
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import math
import operator
import re  # 用于正则表达式检查非法字符

# 创建 FastAPI 实例
app = FastAPI(title="Super Calculator API", description="支持函数、常量和基础运算的超级计算器", version="1.1.0")

# 允许跨域（适用于前端调用）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 请求模型
class ExpressionRequest(BaseModel):
    expression: str

# 计算器核心逻辑
class SuperCalculator:
    def __init__(self):
        self.constants = {
            "pi": math.pi,
            "e": math.e
        }
        self.functions = {
            "sin": math.sin,
            "cos": math.cos,
            "tan": math.tan,
            "log": lambda x: math.log10(x),
            "ln": lambda x: math.log(x),
            "sqrt": math.sqrt,
            "abs": abs,
            "factorial": math.factorial
        }
        self.operators = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv,
            "**": operator.pow
        }

    def validate_expression(self, expression: str):
        # 合法字符：数字、字母、括号、运算符和小数点
        if not re.match(r"^[0-9a-zA-Z+\-*/().,\s^]*$", expression):
            raise ValueError("表达式包含非法字符")

        # 括号配对检查
        if expression.count('(') != expression.count(')'):
            raise ValueError("表达式中的括号不匹配")

        # 可扩展：函数名和常量拼写检查（略）

    def evaluate(self, expression: str) -> float:
        try:
            # 表达式预处理：清空空格、统一小写
            expression = expression.lower().replace(" ", "")

            # 基本语法验证
            self.validate_expression(expression)

            # 替换常量
            for const, value in self.constants.items():
                expression = expression.replace(const, str(value))

            # 允许的名称字典
            allowed_names = {
                **self.functions,
                **self.constants
            }

            # math模块的安全函数也添加进来
            safe_math = {k: getattr(math, k) for k in dir(math) if not k.startswith("__")}
            allowed_names.update(safe_math)

            # 使用 eval 安全执行
            result = eval(expression, {"__builtins__": {}}, allowed_names)
            return result
        except Exception as e:
            raise ValueError(f"表达式无效: {e}")

# 创建计算器实例
calc = SuperCalculator()

# 路由：POST 计算
@app.post("/calculate", summary="计算数学表达式", response_description="返回计算结果")
def calculate(request: ExpressionRequest):
    """
    支持表达式示例：
    - `2 + 2`
    - `sin(pi / 2)`
    - `sqrt(16)`
    - `log(100)`
    - `factorial(5)`
    """
    try:
        result = calc.evaluate(request.expression)
        return {"result": result}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
=======
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import math
import operator

# 创建 FastAPI 实例
app = FastAPI(title="Super Calculator API", description="支持函数、常量和基础运算的超级计算器", version="1.0")

# 允许跨域（如果有前端框架调用，比如 React/Vue）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 可以指定你的前端 URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 请求模型
class ExpressionRequest(BaseModel):
    expression: str

# 计算器逻辑类
class SuperCalculator:
    def __init__(self):
        self.constants = {
            "pi": math.pi,
            "e": math.e
        }
        self.functions = {
            "sin": math.sin,
            "cos": math.cos,
            "tan": math.tan,
            "log": lambda x: math.log10(x),
            "ln": lambda x: math.log(x),
            "sqrt": math.sqrt,
            "abs": abs,
            "factorial": math.factorial
        }
        self.operators = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv,
            "**": operator.pow
        }

    def evaluate(self, expression: str) -> float:
        try:
            # 预处理表达式
            expression = expression.lower().replace(" ", "")

            # 替换常量为具体数值
            for const, value in self.constants.items():
                expression = expression.replace(const, str(value))

            # 构建允许的函数名和常量
            allowed_names = {
                **self.functions,
                **self.constants
            }

            # 添加数学模块中其他安全函数
            safe_math = {k: getattr(math, k) for k in dir(math) if not k.startswith("__")}
            allowed_names.update(safe_math)

            # 安全执行表达式
            result = eval(expression, {"__builtins__": {}}, allowed_names)
            return result
        except Exception as e:
            raise ValueError(f"表达式无效: {e}")

# 实例化计算器
calc = SuperCalculator()

# 路由接口
@app.post("/calculate", summary="计算数学表达式", response_description="返回计算结果")
def calculate(request: ExpressionRequest):
    """
    支持的表达式包括基本运算、常用函数、常量等：
    - 示例：`2 + 2`, `sin(pi/2)`, `sqrt(16)`, `log(100)`
    """
    try:
        result = calc.evaluate(request.expression)
        return {"result": result}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
>>>>>>> e4f049c19148befd72802ac02c9e15e1321463e8
