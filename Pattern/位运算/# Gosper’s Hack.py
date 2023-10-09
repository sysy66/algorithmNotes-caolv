# Gosper’s Hack
# Gosper's Hack是一种生成n元集合所有k元子集的算法，它巧妙地利用了位运算。

k = 3
n = 5

x = (1 << k) - 1
cnt = 0
while x < (1 << n):
    cnt += 1
    print(bin(x))
    lowbit = x & -x
    left = lowbit + x
    right = ((x ^ left) // lowbit) >> 2
    x = left | right


from math import comb
if comb(n, k) == cnt:
    print(f"n = {n}, k = {k}, comb(n, k) = {cnt}")
    