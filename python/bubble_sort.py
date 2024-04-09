# bubble_sort.py

def bubble_sort(arr):
    n = len(arr)
    for j in range(n - 1):
        for i in range(0, n - j - 1):
            i_ = i + 1
            if arr[i] > arr[i_]:
                arr[i], arr[i_] = arr[i_], arr[i]
        print(f'第{j + 1}轮排序后arr: {arr}')


arr = [6, 5, 4, 3, 2, 1]
print(f'举例arr: {arr}')
bubble_sort(arr)

while True:
    a = [int(x) for x in input("输入几个整数。空格为间隔。\n").split()]
    bubble_sort(a)
