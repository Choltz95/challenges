s = 0
a, b = 0, 1
while (a < 4000000):
    a, b = b, a + b
    if (b % 2 == 0):
        s += b
print s
