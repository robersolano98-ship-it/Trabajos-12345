def busqueda_binaria(arr, valor):
    izq, der = 0, len(arr)-1
    while izq <= der:
        mid = (izq+der)//2
        if arr[mid] == valor: return mid
        elif arr[mid] < valor: izq = mid+1
        else: der = mid-1
    return -1

arr = [10, 20, 30, 40, 50] # debe estar ordenado
print(busqueda_binaria(arr, 40))