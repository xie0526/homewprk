c = 2
g = 0.1

while abs(g * g - c) > 0.00000001:
    g = (g + c / g) / 2

print(g)