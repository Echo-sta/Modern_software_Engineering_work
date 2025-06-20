# calculator.py
import math

class CalculatorCore:
    # 基本运算
    def add(self, a, b): return a + b
    def subtract(self, a, b): return a - b
    def multiply(self, a, b): return a * b
    def divide(self, a, b):
        if b == 0: raise ValueError("Division by zero")
        return a / b
    
    # 高级运算
    def power(self, base, exponent): return math.pow(base, exponent)
    def sqrt(self, x):
        if x < 0: raise ValueError("Square root of negative number")
        return math.sqrt(x)
    def log(self, x, base):
        if x <= 0 or base <= 0 or base == 1: raise ValueError("Invalid logarithm arguments")
        return math.log(x, base)
    def ln(self, x):
        if x <= 0: raise ValueError("Natural logarithm of non-positive number")
        return math.log(x)
    
    # 三角函数
    def sin(self, x, inDegrees=True):
        if inDegrees: x = self.degToRad(x)
        return math.sin(x)
    def cos(self, x, inDegrees=True):
        if inDegrees: x = self.degToRad(x)
        return math.cos(x)
    def tan(self, x, inDegrees=True):
        if inDegrees: x = self.degToRad(x)
        return math.tan(x)
    def arcsin(self, x, inDegrees=True):
        if x < -1 or x > 1: raise ValueError("Arcsin argument must be between -1 and 1")
        result = math.asin(x)
        return self.radToDeg(result) if inDegrees else result
    def arccos(self, x, inDegrees=True):
        if x < -1 or x > 1: raise ValueError("Arccos argument must be between -1 and 1")
        result = math.acos(x)
        return self.radToDeg(result) if inDegrees else result
    def arctan(self, x, inDegrees=True):
        result = math.atan(x)
        return self.radToDeg(result) if inDegrees else result
    
    # 统计功能
    def mean(self, values):
        if not values: raise ValueError("Empty dataset")
        return sum(values) / len(values)
    def median(self, values):
        if not values: raise ValueError("Empty dataset")
        sorted_values = sorted(values)
        n = len(sorted_values)
        if n % 2 == 0:
            return (sorted_values[n//2-1] + sorted_values[n//2]) / 2
        else:
            return sorted_values[n//2]
    def standardDeviation(self, values):
        if len(values) < 2: raise ValueError("Need at least 2 values")
        m = self.mean(values)
        variance = sum((x - m) ** 2 for x in values) / (len(values) - 1)
        return math.sqrt(variance)
    
    # 转换功能
    def degToRad(self, degrees): return degrees * math.pi / 180.0
    def radToDeg(self, radians): return radians * 180.0 / math.pi
    
    # 科学计算
    def factorial(self, n):
        if n < 0: raise ValueError("Factorial of negative number")
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
    def isPrime(self, n):
        if n <= 1: return False
        if n <= 3: return True
        if n % 2 == 0 or n % 3 == 0: return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0: return False
            i += 6
        return True
    def gcd(self, a, b):
        a, b = abs(a), abs(b)
        while b:
            a, b = b, a % b
        return a
    def lcm(self, a, b):
        a, b = abs(a), abs(b)
        if a == 0 or b == 0: return 0
        return a // self.gcd(a, b) * b

class Calculator:
    def __init__(self):
        self.core = CalculatorCore()
        self.history = []
    
    # 基本运算
    def add(self, a, b):
        result = self.core.add(a, b)
        self.add_to_history(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a, b):
        result = self.core.subtract(a, b)
        self.add_to_history(f"{a} - {b} = {result}")
        return result
    
    def multiply(self, a, b):
        result = self.core.multiply(a, b)
        self.add_to_history(f"{a} * {b} = {result}")
        return result
    
    def divide(self, a, b):
        result = self.core.divide(a, b)
        self.add_to_history(f"{a} / {b} = {result}")
        return result
    
    # 高级运算
    def power(self, base, exponent):
        result = self.core.power(base, exponent)
        self.add_to_history(f"{base} ^ {exponent} = {result}")
        return result
    
    def sqrt(self, x):
        result = self.core.sqrt(x)
        self.add_to_history(f"√{x} = {result}")
        return result
    
    def log(self, x, base):
        result = self.core.log(x, base)
        self.add_to_history(f"log_{base}({x}) = {result}")
        return result
    
    def ln(self, x):
        result = self.core.ln(x)
        self.add_to_history(f"ln({x}) = {result}")
        return result
    
    # 三角函数
    def sin(self, x, inDegrees=True):
        result = self.core.sin(x, inDegrees)
        unit = "°" if inDegrees else " rad"
        self.add_to_history(f"sin({x}{unit}) = {result}")
        return result
    
    def cos(self, x, inDegrees=True):
        result = self.core.cos(x, inDegrees)
        unit = "°" if inDegrees else " rad"
        self.add_to_history(f"cos({x}{unit}) = {result}")
        return result
    
    def tan(self, x, inDegrees=True):
        result = self.core.tan(x, inDegrees)
        unit = "°" if inDegrees else " rad"
        self.add_to_history(f"tan({x}{unit}) = {result}")
        return result
    
    def arcsin(self, x, inDegrees=True):
        result = self.core.arcsin(x, inDegrees)
        unit = "°" if inDegrees else " rad"
        self.add_to_history(f"arcsin({x}) = {result}{unit}")
        return result
    
    def arccos(self, x, inDegrees=True):
        result = self.core.arccos(x, inDegrees)
        unit = "°" if inDegrees else " rad"
        self.add_to_history(f"arccos({x}) = {result}{unit}")
        return result
    
    def arctan(self, x, inDegrees=True):
        result = self.core.arctan(x, inDegrees)
        unit = "°" if inDegrees else " rad"
        self.add_to_history(f"arctan({x}) = {result}{unit}")
        return result
    
    # 统计功能
    def mean(self, values):
        result = self.core.mean(values)
        self.add_to_history(f"mean({values}) = {result}")
        return result
    
    def median(self, values):
        result = self.core.median(values)
        self.add_to_history(f"median({values}) = {result}")
        return result
    
    def standardDeviation(self, values):
        result = self.core.standardDeviation(values)
        self.add_to_history(f"stddev({values}) = {result}")
        return result
    
    # 转换功能
    def degToRad(self, degrees):
        result = self.core.degToRad(degrees)
        self.add_to_history(f"{degrees}° = {result} rad")
        return result
    
    def radToDeg(self, radians):
        result = self.core.radToDeg(radians)
        self.add_to_history(f"{radians} rad = {result}°")
        return result
    
    # 科学计算
    def factorial(self, n):
        result = self.core.factorial(n)
        self.add_to_history(f"{n}! = {result}")
        return result
    
    def isPrime(self, n):
        result = self.core.isPrime(n)
        self.add_to_history(f"isPrime({n}) = {result}")
        return result
    
    def gcd(self, a, b):
        result = self.core.gcd(a, b)
        self.add_to_history(f"gcd({a}, {b}) = {result}")
        return result
    
    def lcm(self, a, b):
        result = self.core.lcm(a, b)
        self.add_to_history(f"lcm({a}, {b}) = {result}")
        return result
    
    # 历史记录管理
    def add_to_history(self, entry):
        self.history.append(entry)
        if len(self.history) > 100:  # 限制历史记录数量
            self.history.pop(0)
    
    def get_history(self):
        return self.history
    
    def clear_history(self):
        self.history.clear()