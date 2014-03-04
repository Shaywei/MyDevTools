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
