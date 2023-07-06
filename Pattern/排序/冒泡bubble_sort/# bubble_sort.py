# bubble_sort.py

def bubble_sort(arr):
    n = len(arr)
    for j in range(n):
        for i in range(0, n - j - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

# bubble_sort.py

def bubble_sort(arr):
    n = len(arr)
    for j in range(n):
        for i in range(0, n - j - 1):
            i_ = i + 1
            if arr[i] > arr[i_]:
                arr[i], arr[i_] = arr[i_], arr[i]
