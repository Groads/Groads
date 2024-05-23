def contar_frecuencia(lista):
    frecuencia = {}
    for elemento in lista:
        if elemento in frecuencia:
            frecuencia[elemento] += 1
        else:
            frecuencia[elemento] = 1
    return frecuencia

lista = [1, 2, 2, 3, 4, 4, 4, 5]
resultado = contar_frecuencia(lista)

print("Frecuencia de elementos:", resultado)
