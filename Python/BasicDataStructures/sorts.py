import random
from heaps import heapsort

def mergesort(l, low, high):
    def merge(l, low, middle, high):
        left_runner = low
        right_runner = middle + 1;

        # While there are elements in right run:
        sorted_l = []

        while left_runner <= middle and right_runner <= high:
            if l[left_runner] <= l[right_runner]:
                sorted_l.append(l[left_runner])
                left_runner += 1
            else:
                sorted_l.append(l[right_runner])
                right_runner += 1

        while left_runner <= middle:
            sorted_l.append(l[left_runner])
            left_runner += 1

        while right_runner <= high:
            sorted_l.append(l[right_runner])
            right_runner += 1

        for i in range(low, high + 1):
            l[i] = sorted_l[i - low]

    # This is the mergesort that uses merge
    if low < high:
        middle = int((low + high) / 2)
        mergesort(l, low, middle)
        mergesort(l, middle+1, high)
        return merge(l, low, middle, high)

def insertion_sort(l):
    # No need to sort empty list
    if l == []:
        return l

    new_l = [l[0]]
    new_l_len = 0

    for elem in l[1:]:
        for i in range(new_l_len, -1, -1):
            if elem >= new_l[i]:
                new_l.insert(i+1, elem)
                new_l_len += 1
                break
            if i == 0:
                new_l.insert(0, elem)
                new_l_len += 1

    return new_l

def quicksort(l):
    if len(l) <= 1:
        return l

    pivot_index = random.randint(0, len(l)-1)
    pivot = l.pop(pivot_index)
    lte_pivot = []
    gt_pivot = []

    for elem in l:
        if elem <= pivot:
            lte_pivot.append(elem)
        else:
            gt_pivot.append(elem)

    return quicksort(lte_pivot) + [pivot] + quicksort(gt_pivot)

def quicksort_inplace(l, left=None, right=None):
    def partition(l, left, right, pivot_index):
        '''
            left is the index of the leftmost element of the subarray
            right is the index of the rightmost element of the subarray (inclusive)
            number of elements in subarray = right-left+1
        '''
        pivot_value = l[pivot_index]
        l[pivot_index], l[right] = l[right], l[pivot_index] # more pivot to end
        store_index = left
        for i in range(left, right):
            if l[i] <= pivot_value:
                l[i], l[store_index] = l[store_index], l[i]
                store_index += 1
        l[right], l[store_index] = l[store_index], l[right] # move pivot to its final place
        return store_index

    # in-place quicksort
    if left is None:
        left = 0
        right = len(l)-1

    if left < right:
        pivot_index = random.randint(left, right-1)
        pivot_new_index = partition(l, left, right, pivot_index)
        quicksort_inplace(l, left, pivot_new_index-1)
        quicksort_inplace(l, pivot_new_index+1, right)



