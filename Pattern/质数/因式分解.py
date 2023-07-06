import time

# 对一个数进行因式分解
def factorization(num):
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
    return temp


st = time.perf_counter()
print(factorization(707829217))
et = time.perf_counter()
print("用时:", et - st)