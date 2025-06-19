##########
# 小组成员：司静、周旺旺、曾琢
# 程序说明: 中间接口
# 完成人：司静
##########


from flask import Flask, request, jsonify
import ctypes

app = Flask(__name__)
@app.route('/')
def index():
    return "Server is running!"



# 加载 DLL
dll = ctypes.CDLL("./fun.dll")

# 设置函数参数与返回类型
dll.sin_approx_degrees.argtypes = [ctypes.c_double, ctypes.c_int]
dll.sin_approx_degrees.restype = ctypes.c_double

dll.cos_approx_degrees.argtypes = [ctypes.c_double, ctypes.c_int]
dll.cos_approx_degrees.restype = ctypes.c_double

dll.tan_approx.argtypes = [ctypes.c_double, ctypes.c_int]
dll.tan_approx.restype = ctypes.c_double

dll.arcsin_approx.argtypes = [ctypes.c_double, ctypes.c_double]
dll.arcsin_approx.restype = ctypes.c_double

dll.arccos_approx.argtypes = [ctypes.c_double, ctypes.c_double]
dll.arccos_approx.restype = ctypes.c_double

dll.arctan_approx.argtypes = [ctypes.c_double, ctypes.c_double]
dll.arctan_approx.restype = ctypes.c_double

# 包装函数
def sin(x):
    return dll.sin_approx_degrees(x, 10)

def cos(x):
    return dll.cos_approx_degrees(x, 10)

def tan(x):
    return dll.tan_approx(x, 10)

def asin(x):
    return dll.arcsin_approx(x, 0.01)

def acos(x):
    return dll.arccos_approx(x, 0.01)

def atan(x):
    return dll.arctan_approx(x, 0.01)

# 接口：支持 POST 请求，参数用 JSON 格式传递
@app.route('/calc', methods=['POST'])
def calc():
    data = request.get_json()
    func = data.get("func")  # 要调用的函数名
    x = float(data.get("x"))

    try:
        if func == "sin":
            result = sin(x)
        elif func == "cos":
            result = cos(x)
        elif func == "tan":
            result = tan(x)
        elif func == "asin":
            result = asin(x)
        elif func == "acos":
            result = acos(x)
        elif func == "atan":
            result = atan(x)
        else:
            return jsonify({"error": "Invalid function name"}), 400
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    print("Starting Flask app...")
    app.run(port=8000)
