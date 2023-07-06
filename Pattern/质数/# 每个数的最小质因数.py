# 每个数的最小质因数


class PrimeHelper:
    __slots__ = "_minPrime"  # 每个数的最小质因数

    def __init__(self, maxN: int):
        """预处理 O(nloglogn)"""
        minPrime = list(range(maxN + 1))
        upper = int(maxN ** 0.5) + 1
        for i in range(2, upper):
            if minPrime[i] < i:
                continue
            for j in range(i * i, maxN + 1, i):
                if minPrime[j] == j:
                    minPrime[j] = i
        self._minPrime = minPrime

    def isPrime(self, n: int) -> bool:
        if n < 2:
            return False
        return self._minPrime[n] == n

    def getPrimeFactors(self, n: int):
        """求n的质因数分解 O(logn)"""
        pre, f = 1, self._minPrime
        while n > 1:
            m = f[n]
            if m != pre:
                yield m
                pre = m
            n //= m

    def getPrimes(self) -> list[int]:
        return [x for i, x in enumerate(self._minPrime) if i >= 2 and i == x]


ph = PrimeHelper(1000000)


class PrimeHelper:
    __slots__ = "_minPrime"

    def __init__(self, maxN):
        minPrime = list(range(maxN + 1))
        i = 2
        while i * i <= maxN:
            if minPrime[i] == i:
                for j in range(i * i, maxN + 1, i):
                    if minPrime[j] == j:
                        minPrime[j] = i
            i += 1
        self._minPrime = minPrime

    def isPrime(self, n):
        return n >= 2 and self._minPrime[n] == n

    def getPrimeFactors(self, n):
        pre, f = 1, self._minPrime
        while n > 1:
            m = f[n]
            if m != pre:
                yield m
                pre = m
            n //= m

    def getPrimes(self):
        return [x for i, x in enumerate(self._minPrime) if i > 1 and i == x]

ph = PrimeHelper(10 ** 6)