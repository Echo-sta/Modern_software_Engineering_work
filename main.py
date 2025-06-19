from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import math
import operator
import re
import ast

# 创建 FastAPI 实例
app = FastAPI(title="Super Calculator API", description="支持函数、常量和基础运算的超级计算器", version="1.4.0")

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

# 安全的 AST 表达式检查器
class SafeEvaluator(ast.NodeVisitor):
    ALLOWED_NODES = {
        ast.Expression, ast.BinOp, ast.UnaryOp, ast.Call, ast.Num, ast.Name,
        ast.Load, ast.Pow, ast.Mult, ast.Div, ast.Add, ast.Sub, ast.Mod,
        ast.USub, ast.UAdd, ast.Constant  # Python 3.8+ 用 Constant 替代 Num
    }

    def __init__(self, allowed_names):
        self.allowed_names = allowed_names

    def visit(self, node):
        if type(node) not in self.ALLOWED_NODES:
            raise ValueError(f"不允许的表达式结构: {type(node).__name__}")
        return super().visit(node)

    def visit_Call(self, node):
        if not isinstance(node.func, ast.Name):
            raise ValueError("不允许的函数调用方式")
        if node.func.id not in self.allowed_names:
            raise ValueError(f"未知函数: {node.func.id}")
        self.generic_visit(node)

    def visit_Name(self, node):
        if node.id not in self.allowed_names:
            raise ValueError(f"未知变量或函数: {node.id}")

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

            # 替换常量
            for const, value in self.constants.items():
                expression = re.sub(rf'\b{const}\b', str(value), expression)

            allowed_names = {
                **self.functions,
                **self.constants
            }

            # ✅ 安全解析并编译表达式
            tree = ast.parse(expression, mode='eval')
            SafeEvaluator(allowed_names).visit(tree)
            result = eval(compile(tree, filename="<ast>", mode="eval"), {"__builtins__": {}}, allowed_names)
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
