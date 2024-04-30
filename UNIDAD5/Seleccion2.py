def selection_sort_even_odd(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] % 2 < arr[min_idx] % 2 or (arr[j] % 2 == arr[min_idx] % 2 and arr[j] < arr[min_idx]):
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

arr = [7, 12, 5, 18, 3, 14, 10]
selection_sort_even_odd(arr)
print("Lista ordenada con números pares e impares usando Ordenamiento por Selección:")
for num in arr:
    print(num, end=" ")
