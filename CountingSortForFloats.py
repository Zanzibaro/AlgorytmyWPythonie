def count_sort(arr,decimal_places):
    factor = 10**decimal_places
    scaled_arr = [int(round(num*factor))for num in arr]
    max_element = int(max(scaled_arr))
    min_element = int(min(scaled_arr))
    range_of_elements = max_element - min_element + 1
    
    # Utworz tablice zliczania, aby przechowywac wystapienia poszczegolnych
    # elementow i zainicjuj tablice licznikow zerem
    #count_arr = [0 for _ in range(range_of_elements)]
    #output_arr = [0 for _ in range(len(arr))]
    
    count_arr = [0 for _ in range(range_of_elements)]
    output_arr = [0 for _ in range(len(arr))]
  
    # przechowaj liczbe wystapien kazdej wartosci
    for i in range(0, len(arr)):
        count_arr[scaled_arr[i]-min_element] += 1
  
    # Zmien count_arr[i] tak, aby count_arr[i] zawieralo teraz aktualne
    # pozycja tego elementu w tablicy wyjsciowej
    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i-1]
  
    # zbudowanie tablicy wyjsciowej
    for i in range(len(arr)-1, -1, -1):
        output_arr[count_arr[scaled_arr[i] - min_element] - 1] = scaled_arr[i]
        count_arr[scaled_arr[i] - min_element] -= 1

    #kopiowanie tablicy output do arr
    for i in range(0, len(arr)):
        scaled_arr[i] = output_arr[i]/factor
  
    return scaled_arr
  
arr = [-5.1, -10.2, 0.76, -3.32, 8.12, 5.2, -1, 10]
ans = count_sort(arr,2)
print("Tablica posortowana to" + str(ans))
 