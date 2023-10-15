def gongyue(a, b):
    while b!= 0:
        a, b = b, a % b
    return a
       
number1 = int(input())
number2 = int(input())

result = gongyue(number1, number2)
print(result)
