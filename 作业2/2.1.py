def find_max_product():
    n = int(input("请输入一个正整数："))
    
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    
    factors = []
    while n > 4:
        factors.append(3)
        n -= 3
    
    factors.append(n - 1)
    factors.append(1)
    
    return factors

result = find_max_product()
print("正整数列表的乘积最大为：", result)
