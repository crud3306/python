#!/usr/bin/python
# -*- coding: utf-8 -*-

# 常用算法
# 平均速度最快的排序算法是？
# 排序方法        平均情况        最好情况        最坏情况        辅助空间         稳定性
# 冒泡排序        O(n^2)         O(n)           O(n^2)           O(1)          稳定
# 选择排序        O(n^2)         O(n^2)         O(n^2)           O(1)          不稳定
# 插入排序        O(n^2)         O(n)           O(n^2)           O(1)          稳定
# 希尔排序  O(n*log(n))~O(n^2)   O(n^1.3)       O(n^2)           O(1)          不稳定
# 堆排序         O(n*log(n))    O(n*log(n))     O(n*log(n))     O(1)           不稳定
# 归并排序       O(n*log(n))    O(n*log(n))     O(n*log(n))     O(n)           稳定
# 快速排序       O(n*log(n))    O(n*log(n))     O(n^2)           O(1)          不稳定

# 冒泡排序
# ---------------
def bubble_sort(lists):
    count = len(lists)
    for i in range(count):
    	current_status = False

        for j in range(i + 1, count):
            if lists[i] > lists[j]:
                lists[i], lists[j] = lists[j], lists[i]
                current_status = True

        if not current_status:
            break
    return lists


# 快速排序
# ---------------
def quick_sort(lists, left, right):
    if left >= right:
        return lists
    key = lists[left]
    low = left
    high = right
    while left < right:
        while left < right and lists[right] >= key:
            right -= 1
        lists[left] = lists[right]
        while left < right and lists[left] <= key:
            left += 1
        lists[right] = lists[left]
    lists[right] = key
    quick_sort(lists, low, left - 1)
    quick_sort(lists, left + 1, high)
    return lists


# 选择排序
# ---------------
# 选择排序法：每一次从待排序的数据元素中选出最小（或最大）的一个元素，存放到序列的起始位置，直到全部排完。
def select_sort(lists):
    count = len(lists)
    for i in range(count):
        min = i
        for j in range(i + 1, count):
            if lists[min] > lists[j]:
                min = j
        lists[min], lists[i] = lists[i], lists[min]
    return lists


# 插入排序
# ---------------
# 列表被分为有序区和无序区两个部分。最初有序区只有一个元素。
# 每次从无序区选择一个元素，插入到有序区的位置，直到无序区变空。
def insert_sort(lists):
    # 循环的是第二个到最后（待摸的牌）
    for i in range(1, len(lists)):
        # 待插入的数（摸上来的牌）
        min = lists[i]
        # 已排好序的最右边一个元素（手里的牌的最右边）
        j = i - 1
        # 一只和排好的牌比较，排好的牌的牌的索引必须大于等于0
        # 比较过程中，如果手里的比摸上来的大，
        while j >= 0 and lists[j] > min:
            # 那么手里的牌往右边移动一位，就是把j付给j+1
            lists[j+1] = lists[j]
            # 换完以后在和下一张比较
            j -= 1
        # 找到了手里的牌比摸上来的牌小或等于的时候，就把摸上来的放到它右边
        lists[j+1] = min
    return lists















