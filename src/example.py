import time, random
original = [i for i in range(10000)]
random.shuffle(original)
list1 = list(original)
list2 = list(original)
list3 = list(original)
list4 = list(original)



# Merge Sort

def mergeSort(li:list):
    if len(li) > 1:
        mid = len(li) // 2
        L = li[:mid]
        R = li[mid:]

        mergeSort(L)
        mergeSort(R)

        li.clear()
        while len(L) > 0 and len(R) > 0:
            if L[0] <= R[0]:
                li.append(L[0])
                L.pop(0)
            else:
                li.append(R[0])
                R.pop(0)
        for i in L:
            li.append(i)
        for i in R:
            li.append(i)

print("Original list: {}".format(list1))
start = time.time()
mergeSort(list1)
print('Sorted list by mergeSort method: {}'.format(list1))
end = time.time() - start
print('During time: {}'.format(end))



# Quick Sorting

def partition(list:list, low, high):
    i = (low-1)
    pivot = list[high]

    for j in range(low, high):
        if list[j] < pivot:
            i += 1
            list[i], list[j] = list[j], list[i]

    list[i+1], list[high] = list[high], list[i+1]
    return (i+1)

def quickSort(li:list, low, high):
    if low < high:
        pi = partition(li, low, high)

        quickSort(li, low, pi-1)
        quickSort(li, pi+1, high)

start = time.time()
n = len(list2); quickSort(list2, 0, n-1)
print('Sorted list by quicksort method: {}'.format(list2))
end = time.time() - start
print("During time: {}".format(end))





# Heap Sorting

def heapify(list, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and list[i] < list[l]:
        largest = l

    if r < n and list[largest] < list[r]:
        largest = r

    if largest != i:
        list[i], list[largest] = list[largest], list[i]

        heapify(list, n, largest)

def heapsort(list):
    n = len(list)

    for i in range(n//2 - 1, -1, -1):
        heapify(list, n, i)

    for i in range(n-1, 0, -1):
        list[i], list[0] = list[0], list[i]
        heapify(list, i, 0)

start = time.time()
heapsort(list3)
print('Sorted by heapsort method: {}'.format(list3))
end = time.time() - start
print("During time: {}".format(end))

start = time.time()
list4.sort()
print('Sorted by Python sort method: {}'.format(list4))
end = time.time()-start
print('During time: {}'.format(end))

print("hello world")