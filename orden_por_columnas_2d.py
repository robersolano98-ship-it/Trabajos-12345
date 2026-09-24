matriz = [[3,1,2],[9,5,6],[8,7,4]]
columnas_ordenadas = [sorted(col) for col in zip(*matriz)]
resultado = [list(fila) for fila in zip(*columnas_ordenadas)]
print(resultado)