import time
import random
def pigeonhole_sort(a):

    # okreslenie zakresu wartości na liście
    # (tj. liczba przegródek, których potrzebujemy)
    my_min = min(a)
    my_max = max(a)
    size = my_max - my_min + 1
  
    # lista przegrodek
    holes = [0] * size
  
    # zapelnij przegordki.
    for x in a:
        assert type(x) is int, "tylko liczby calkowite"
        holes[x - my_min] += 1
  
    # umiesc elementy spowrotem w tablicy w kolejnosci rosnacej
    i = 0
    for count in range(size):
        while holes[count] > 0:
            holes[count] -= 1
            a[i] = count + my_min
            i += 1
              
def CountingSortReal(arr, decimalPlaces = 1):
    if not arr:
        return []
    scaledArr = [int(round(num)) for num in arr]
    maxVal = max(scaledArr)
    minVal = min(scaledArr)
    count = [0] * (maxVal - minVal + 1)
    
    for num in scaledArr:
        count[num - minVal] += 1
    sortedArr = []
    for i, c in enumerate(count):
        sortedArr.extend([i + minVal] * c)
    
    result = [num for num in sortedArr]
    return result
        
        

a = [random.randint(0, 10) for i in range(200000)]
a1 = a
a2 = a
print("Czas zeby posortowac pigeon sortem")
start_time = time.time()
pigeonhole_sort(a1)
end_time = time.time()
print(end_time - start_time)

print("=============")
print("Czas zeby posortowac counting sortem")

start_time = time.time()
CountingSortReal(a2)
end_time = time.time()
print(end_time - start_time)

 