from decimal import *
from matrix import *

getcontext().prec = 500

flag = ""
curr = [Decimal(ord(x)) for x in flag]
n = len(flag)
r = Decimal(0.5)

matrix = [[0 for x in range(n)] for y in range(n)]
for i in range(n):
    if i == 0:
        matrix[i] = [2 + 2 * r, -r] + [Decimal(0)] * (n - 2)
    elif i == n - 1:
        matrix[i] = [Decimal(0)] * (n - 2) + [-r, 2 + 2 * r]
    else:
        matrix[i] = [Decimal(0)] * (i - 1) + [-r, 2 + 2 * r, -r] + [Decimal(0)] * (n - i - 2)

inv = invert(matrix)

for step in range(100):
    temp = [curr[0]] + [Decimal(2) * curr[x + 1] + r * (curr[x] - Decimal(2) * curr[x + 1] + curr[x + 2]) for x in range(n - 2)] + [curr[n - 1]]
    curr = mult(inv, temp)

f = open("encrypted", "w")
f.write(str(curr))
f.close()
