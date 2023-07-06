# 字符串排序.py

s = 'bachfmsbw'
s = "".join((lambda x:(x.sort(),x)[1])(list(s)))
print(s)