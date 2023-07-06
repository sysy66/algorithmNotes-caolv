#分解质因子

temp = []
p, x = 2, num
while p * p <= x:
    if x % p == 0:
        temp.append(p)
        x //= p
        while x % p == 0:
            temp.append(p)
            x //= p
    p += 1
if x > 1:
    temp.append(x)