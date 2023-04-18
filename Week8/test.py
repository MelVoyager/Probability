import sympy as sp

t = sp.Symbol('t')
lambda_val = 4

# 泊松分布的矩生成函数
mgf = sp.exp(lambda_val * (sp.exp(t) - 1))

# 求1-4阶矩
moment1 = mgf.diff(t).subs(t, 0)
moment2 = mgf.diff(t, 2).subs(t, 0)
moment3 = mgf.diff(t, 3).subs(t, 0)

# 计算均值、方差和三阶中心矩
mean = moment1
variance = moment2 - mean**2
third_central_moment = moment3 - 3 * mean * moment2 + 2 * mean**3

# 计算标准差
std_dev = sp.sqrt(variance)

# 计算偏度系数
skewness = third_central_moment / std_dev**3

print("Skewness: ", skewness)
