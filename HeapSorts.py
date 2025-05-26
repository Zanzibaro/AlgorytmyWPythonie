import random
import time

#Recursion
def Heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[largest] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        Heapify(arr, n, largest)

def HeapSort(arr):
    n = len(arr)

    for i in range (n // 2 - 1, -1, -1):
        Heapify(arr, n, i)

    for i in range (n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        Heapify(arr, i, 0)

#Ternary
def TernaryHeapify(arr, n, i):
    largest = i
    left = 3 * i + 1
    middle = 3 * i + 2
    right = 3 * i + 3

    if left < n and arr[left] > arr[largest]:
        largest = left

    if middle < n and arr[middle] > arr[largest]:
        largest = middle

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        TernaryHeapify(arr, n, largest)

def TernaryHeapSort(arr):
    n = len(arr)

    for i in range (n // 3 - 1, -1, -1):
        Heapify(arr, n, i)

    for i in range (n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        TernaryHeapify(arr, i, 0)

# Iterative
def HeapifyIterative(arr, n, i):
    largest = i

    while True:
        left = 2 * largest + 1
        right = 2 * largest + 2
        swap = largest

        if left < n and arr[largest] < arr[left]:
            swap = left

        if right < n and arr[largest] < arr[right]:
            swap = right

        if swap == largest:
            break

        arr[largest], arr[swap] = arr[swap], arr[largest]
        largest = swap

def HeapSortIterative(arr):
    n = len(arr)

    for i in range (n // 2 - 1, -1, -1):
        HeapifyIterative(arr, n, i)

    for i in range (n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        HeapifyIterative(arr, i, 0)

def main():        
    n = int(input("Wprowadź ile chcesz mieć elementów w tablicy: "))
    arr = []

    for i in range(n):
        arr.append(random.randint(-100, 100))

    start_time = time.time()
    HeapSort(arr)
    end_time = time.time()

    print(f"HeapSort: Czas sortowania: {end_time - start_time:.5f} sekund")


    start_time = time.time()
    TernaryHeapSort(arr)
    end_time = time.time()

    print(f"TernaryHeapSort: Czas sortowania: {end_time - start_time:.5f} sekund")


    start_time = time.time()
    HeapSortIterative(arr)
    end_time = time.time()

    print(f"HeapSortIterative: Czas sortowania: {end_time - start_time:.5f} sekund")

if __name__ == "__main__":
    main()