from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import math
import operator
import re

# 创建 FastAPI 实例
app = FastAPI(title="Super Calculator API", description="支持函数、常量和基础运算的超级计算器", version="1.3.0")

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

# 计算历史记录（内存存储）
calculation_history = []

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
            "ln": math.log,
            "sqrt": math.sqrt,
            "abs": abs,
            "factorial": math.factorial,
            "exp": math.exp  # ✅ 支持指数函数
        }
        self.operators = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv,
            "**": operator.pow
        }

    def validate_expression(self, expression: str):
        if not re.match(r"^[0-9a-zA-Z+\-*/().,\s^]*$", expression):
            raise ValueError("表达式包含非法字符")
        if expression.count('(') != expression.count(')'):
            raise ValueError("表达式中的括号不匹配")

    def evaluate(self, expression: str) -> float:
        try:
            expression = expression.lower().replace(" ", "")
            self.validate_expression(expression)

            for const, value in self.constants.items():
                expression = re.sub(rf'\b{const}\b', str(value), expression)

            allowed_names = {
                **self.functions,
                **self.constants
            }

            safe_math = {k: getattr(math, k) for k in dir(math) if not k.startswith("__")}
            allowed_names.update(safe_math)

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
    - `exp(1)` ✅ 支持指数函数
    - `e + 1`
    """
    try:
        result = calc.evaluate(request.expression)

        # ✅ 添加到历史记录
        calculation_history.append({
            "expression": request.expression,
            "result": result
        })

        return {"result": result}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

# ✅ 路由：GET 计算历史记录
@app.get("/history", summary="获取计算历史记录", response_description="返回历史记录")
def get_history():
    return {"history": calculation_history}
