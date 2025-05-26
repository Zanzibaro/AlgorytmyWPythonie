def countSort(arr):
  
    # posortowane wyjscie
    output = [0 for i in range(len(arr))]
  
    # stworzenie tablicy licznikow i zainicjalizowanie jej jako 0
    count = [0 for i in range(256)]
  
    # do przechowywania odpowiedzi
    # string jest niezmienny
    ans = ["" for _ in arr]
  
    # przechowyanie liczby zliczonych znakow
    for i in arr:
        count[ord(i)] += 1                             
  
    # zmien count[i] tak aby count[i] teraz przechowywal
    # pozycje tego znaku w tablicy odpowiedzi 
    for i in range(256):
        count[i] += count[i-1]
  
    # zbuduj tablice odpowiedzi
    for i in range(len(arr)):
        output[count[ord(arr[i])]-1] = arr[i]
        count[ord(arr[i])] -= 1
  
    # skopiuj tablice wyjsciowa do arr,
    # teraz arr przechowuje posortowane znaki
    for i in range(len(arr)):
        ans[i] = output[i]
    return ans 

arr = "##%%AAaabB*hgsjZZZidun"
#arr = "0122345"
ans = countSort(arr)
print("posortowana tablica % s" %("".join(ans))) 

 