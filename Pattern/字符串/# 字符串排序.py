# 字符串排序.py

s = 'bachfmsbw'

s1 = "".join((lambda x:(x.sort(), x)[1])(list(s)))
print(s1)

s2 = ''.join(sorted(s))
print(s2)

