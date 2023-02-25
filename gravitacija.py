C = 6.674 * pow(10, -11)
M = 5.972 * pow(10, 24)
r = 6.371 * pow(10, 6)

height = int(input())
a = (C * M) / pow(r + height, 2)
print(height)
print(a)
