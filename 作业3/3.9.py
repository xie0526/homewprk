def construct_array(nums):
    n = len(nums)
    left_product = [1] * n  # 左边的乘积
    right_product = [1] * n  # 右边的乘积

    # 计算左边的乘积
    for i in range(1, n):
        left_product[i] = left_product[i-1] * nums[i-1]

    # 计算右边的乘积
    for i in range(n-2, -1, -1):
        right_product[i] = right_product[i+1] * nums[i+1]

    # 构建结果数组
    result = [1] * n
    for i in range(n):
        result[i] = left_product[i] * right_product[i]

    return result

# 测试
nums = [1, 2, 3, 4, 5]
result = construct_array(nums)
print(result)