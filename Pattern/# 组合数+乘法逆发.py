# 组合数+乘法逆发.py

from math import comb as comb

MOD = 1_000_000_007
MX = 100_000

fac = [0] * MX
fac[0] = 1
for i in range(1, MX):
    fac[i] = fac[i - 1] * i % MOD
inv_fac = [0] * MX
inv_fac[-1] = pow(fac[-1], MOD - 2, MOD)
for i in range(MX - 2, -1, -1):
    inv_fac[i] = inv_fac[i + 1] * (i + 1) % MOD


def comb1(n: int, k: int) -> int:
    return fac[n] * inv_fac[k] % MOD * inv_fac[n - k] % MOD


print(comb1(4, 3) == comb(4, 3))
print(comb1(4, 0) == comb(4, 0))
print(comb1(4, 4) == comb(4, 4))
