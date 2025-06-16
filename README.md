# 🧮 超级计算器 API（基于 FastAPI）

这是一个基于 FastAPI 实现的超级计算器接口，支持数学表达式的解析与计算，涵盖常见函数、常量和基础运算。

后端由司静同学开发，供小组成员测试和集成使用。

---

##  使用步骤

### 第一步：安装依赖

建议在虚拟环境中操作（如使用 `venv` 或 `conda`）：

```bash
pip install -r requirements.txt

###  第二步：启动服务

```bash
uvicorn main:app --reload


然后打开浏览器访问：

📍 http://127.0.0.1:8000/docs
即可访问自动生成的 Swagger 接口文档，用于测试接口。
