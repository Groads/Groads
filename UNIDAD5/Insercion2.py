def insertion_sort_alpha(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        
arr = ["banana", "apple", "orange", "grape", "pear"]
insertion_sort_alpha(arr)
print("Lista ordenada alfabéticamente usando Ordenamiento por Inserción:")
for word in arr:
    print(word, end=" ")
