// calculator_core.cpp
#include "calculator_core.h"
#include <cmath>
#include <stdexcept>
#include <algorithm>

#ifndef M_PI
#define M_PI 3.14159265358979323846
#endif

// 基本运算
double CalculatorCore::add(double a, double b) { return a + b; }
double CalculatorCore::subtract(double a, double b) { return a - b; }
double CalculatorCore::multiply(double a, double b) { return a * b; }
double CalculatorCore::divide(double a, double b) {
    if (b == 0) throw std::invalid_argument("Division by zero");
    return a / b;
}

// 高级运算
double CalculatorCore::power(double base, double exponent) { return std::pow(base, exponent); }
double CalculatorCore::sqrt(double x) {
    if (x < 0) throw std::invalid_argument("Square root of negative number");
    return std::sqrt(x);
}
double CalculatorCore::log(double x, double base) {
    if (x <= 0 || base <= 0 || base == 1) throw std::invalid_argument("Invalid logarithm arguments");
    return std::log(x) / std::log(base);
}
double CalculatorCore::ln(double x) {
    if (x <= 0) throw std::invalid_argument("Natural logarithm of non-positive number");
    return std::log(x);
}

// 三角函数
double CalculatorCore::sin(double x, bool inDegrees) {
    if (inDegrees) x = degToRad(x);
    return std::sin(x);
}
double CalculatorCore::cos(double x, bool inDegrees) {
    if (inDegrees) x = degToRad(x);
    return std::cos(x);
}
double CalculatorCore::tan(double x, bool inDegrees) {
    if (inDegrees) x = degToRad(x);
    return std::tan(x);
}
double CalculatorCore::arcsin(double x, bool inDegrees) {
    if (x < -1 || x > 1) throw std::invalid_argument("Arcsin argument must be between -1 and 1");
    double result = std::asin(x);
    return inDegrees ? radToDeg(result) : result;
}
double CalculatorCore::arccos(double x, bool inDegrees) {
    if (x < -1 || x > 1) throw std::invalid_argument("Arccos argument must be between -1 and 1");
    double result = std::acos(x);
    return inDegrees ? radToDeg(result) : result;
}
double CalculatorCore::arctan(double x, bool inDegrees) {
    double result = std::atan(x);
    return inDegrees ? radToDeg(result) : result;
}

// 统计功能
double CalculatorCore::mean(const std::vector<double>& values) {
    if (values.empty()) throw std::invalid_argument("Empty dataset");
    double sum = 0;
    for (double value : values) sum += value;
    return sum / values.size();
}
double CalculatorCore::median(std::vector<double> values) {
    if (values.empty()) throw std::invalid_argument("Empty dataset");
    std::sort(values.begin(), values.end());
    size_t n = values.size();
    if (n % 2 == 0) {
        return (values[n / 2 - 1] + values[n / 2]) / 2;
    }
    else {
        return values[n / 2];
    }
}
double CalculatorCore::standardDeviation(const std::vector<double>& values) {
    if (values.size() < 2) throw std::invalid_argument("Need at least 2 values");
    double m = mean(values);
    double sum = 0.0;
    for (double value : values) {
        sum += std::pow(value - m, 2);
    }
    return std::sqrt(sum / (values.size() - 1));
}

// 转换功能
double CalculatorCore::degToRad(double degrees) { return degrees * M_PI / 180.0; }
double CalculatorCore::radToDeg(double radians) { return radians * 180.0 / M_PI; }

// 科学计算
double CalculatorCore::factorial(int n) {
    if (n < 0) throw std::invalid_argument("Factorial of negative number");
    double result = 1.0;
    for (int i = 2; i <= n; ++i) {
        result *= i;
    }
    return result;
}
bool CalculatorCore::isPrime(int n) {
    if (n <= 1) return false;
    if (n <= 3) return true;
    if (n % 2 == 0 || n % 3 == 0) return false;
    int i = 5;
    while (i * i <= n) {
        if (n % i == 0 || n % (i + 2) == 0) return false;
        i += 6;
    }
    return true;
}
int CalculatorCore::gcd(int a, int b) {
    a = std::abs(a);
    b = std::abs(b);
    while (b) {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}
int CalculatorCore::lcm(int a, int b) {
    a = std::abs(a);
    b = std::abs(b);
    if (a == 0 || b == 0) return 0;
    return a / gcd(a, b) * b;
}