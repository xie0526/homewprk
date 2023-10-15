import math

def cube_root_newton(c):
    g = c / 2
    
    while abs(g * g * g - c) > 0.0000000001:
        g = (2 * g + c / (g * g)) / 3
    
    return g

def cube_root_power(c):
    return c ** (1/3)

def cube_root_math(c):
    return math.pow(c, 1/3)

# 示例用法
c = 10
print(cube_root_newton(c))   # 2.154434690031884
print(cube_root_power(c))    # 2.154434690031884
print(cube_root_math(c))     # 2.154434690031884