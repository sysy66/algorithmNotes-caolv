def gcd(a,b):
	while a % b != 0:
		r = a % b
		a = b
		b = r
	return b

# lem(a,b) = a*b//gcd(a,b)
# 最小公倍数gcd
# 最大公约数lem

def gcd2(a, b):
    while a:
        a, b = b % a, a
    return b