def partition(arr, low, high):
    #low --> pierwszy el tablicy
    #high --> ostatni el tablicy
    i = (low-1)
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            i+=1
            arr[i], arr[j] = arr[j], arr[i]
            
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)

def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low<high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)
        
        
arr=[10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n-1)
for i in range(n):
    print(arr[i])
    