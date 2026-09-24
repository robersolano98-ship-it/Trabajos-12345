def busqueda_secuencial(arr, valor):
    for i in range(len(arr)):
        if arr[i] == valor:
            return i
    return -1

arr = [10, 20, 30, 40]
print(busqueda_secuencial(arr, 30))