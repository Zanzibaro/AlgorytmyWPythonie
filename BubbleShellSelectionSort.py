def BubbleSort(arr):
    n = len(arr)
    ilZm = 0
    ilPrz = 0

    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                ilZm+=1
                swapped = True
        if swapped == False:
            break
        ilPrz += 1

    print("Zamian:", ilZm, " przejsc: ", ilPrz)

def ShellSort(arr, n):
    test2=0
    gap = n//2
    while gap>0:
        j = gap
        while j<n:
            i = j-gap
            while i>=0:
                if arr[i+gap] > arr[i]:
                    break
                else:
                    arr[i+gap], arr[i] = arr[i], arr[i+gap]  
                    test2 += 2
                i = i - gap
            j += 1
        gap=gap//2
    print("wynik dla Shell Sort", test2)

def SelectionSort(arr):
    ilPrz = 0
    ilZm = 0
    for i in range(len(arr)):
        min_indx = i
        for j in range(i+1, len(arr)):
            if arr[min_indx] > arr[j]:
                min_indx = j
        arr[i], arr[min_indx] = arr[min_indx], arr[i]
        ilZm += 1
        ilPrz += 1

    print("Zamian:", ilZm, " przejsc: ", ilPrz)



arr2 = [64, 25, 12, 22, 11]
SelectionSort(arr2)
print("Tablica posortowana")
for i in range(len(arr2)):
    print("%d" %arr2[i])