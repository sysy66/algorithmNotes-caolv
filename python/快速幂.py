# 快速幂.py

MOD = int(1e9 + 7)


def f(x, n, MOD):
    # base 底数
    b = x
    # power 指数
    e = n
    # result 结果
    r = 1
    while e:
        if e & 1:
            r *= b
            r %= MOD
        e >>= 1
        b *= b
        b %= MOD
    return r


x, n = 3, 4
print(pow(x, n, MOD))
print(pow(x, n, MOD) == f(x, n, MOD))
x, n = 107, 8
print(pow(x, n, MOD) == f(x, n, MOD))
