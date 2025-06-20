// calculator_core.h
#ifndef CALCULATOR_CORE_H
#define CALCULATOR_CORE_H

#include <vector>

class CalculatorCore {
public:
    // 基本运算
    double add(double a, double b);
    double subtract(double a, double b);
    double multiply(double a, double b);
    double divide(double a, double b);

    // 高级运算
    double power(double base, double exponent);
    double sqrt(double x);
    double log(double x, double base);
    double ln(double x);

    // 三角函数
    double sin(double x, bool inDegrees = true);
    double cos(double x, bool inDegrees = true);
    double tan(double x, bool inDegrees = true);
    double arcsin(double x, bool inDegrees = true);
    double arccos(double x, bool inDegrees = true);
    double arctan(double x, bool inDegrees = true);

    // 统计功能
    double mean(const std::vector<double>& values);
    double median(std::vector<double> values);
    double standardDeviation(const std::vector<double>& values);

    // 转换功能
    double degToRad(double degrees);
    double radToDeg(double radians);

    // 科学计算
    double factorial(int n);
    bool isPrime(int n);
    int gcd(int a, int b);
    int lcm(int a, int b);
};

#endif