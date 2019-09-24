

import random


def quick_sort(lst: list, l: int, h: int):
    i, j, c = l, h, lst[0]
    while i < j:
        while i < j and lst[j] >= c:
            j -= 1
        while i < j and lst[i] <= c:
            i += 1
        if i < j:
            lst[i], lst[j] = lst[j], lst[i]
    lst[l] = lst[i]
    lst[i] = c
    quick_sort(lst, low, i-1)
    quick_sort(lst, i+1, h)


def heap_sort(lst: list):
    size = len(lst)
    for i in range(size(len//2-1, -1, -1)):
        adjust_heap(lst, i, len)

    for i in range(size-1, -1, -1):
        lst[0], lst[i] = lst[i], lst[0]
        adjust_heap(lst, 0, i)


def adjust_heap(lst: list, f, size):
    l = f * 2 + 1
    r = f * 2 + 2
    maxer = f

    if l < size and lst[l] > lst[maxer]:
        maxer = l
    if r < size and lst[r] > lst[maxer]:
        maxer = r
    if f != maxer:
        lst[maxer], lst[f] = lst[f], lst[maxer]
        adjust_heap(lst, maxer, len)


def divide(lst: list, low: int, high: int):
    if low < high:
        mid = (low + high)//2
        divide(lst, low, mid)
        divide(lst, mid + 1, high)
        merge(lst, low, mid, mid+1, high)


def merge(lst: list, ls: int, le: int, hs: int, he):

    temp = [None for i in range(len(lst))]
    index = start = ls
    # 成了怎么合并两个有序的列表为一个有序的列表的算法
    while ls <= le and hs < he:
        if lst[ls] <= lst[hs]:
            temp[index] = lst[ls]
            ls += 1
        else:
            temp[index] = lst[hs]
            hs += 1
        index += 1

    while ls <= le:
        temp[index] = lst[ls]
        ls += 1
        index += 1

    while hs <= he:
        temp[index] = lst[hs]
        hs += 1
        index += 1

    while start <= he:
        lst[start] = temp[start]
        start += 1


def shell_sort1(lst: list):
    step = len(lst) // 2
    while step >= 1:
        for i in range(step):
            for j in range(i+step, len(lst), step):
                value = lst[j]
                j -= step
                while j >= i and lst[j] > value:
                    lst[j+step] = lst[j]
                    j -= step
                lst[j+step] = value
        step //= 2
    return lst

def shell_sort2(lst: list):
    step = len(lst) // 2
    while step >= 1:
        for i in range(step):
            for j in range(i + step, len(lst), step):
                value = lst[j]
                while j >= i and value < lst[j - step]:
                    lst[j] = lst[j - step]
                    j -= step
                lst[j] = value
        step //= 2
    return lst

# lst = [random.randint(1, 9) for i in range(10)]
if __name__ == "__main__":
    lst = [4, 5, 6, 1, 3, 9, 2, 7, 8]
    lst2 = lst
    print(shell_sort1(lst))
    print(shell_sort2(lst2))
