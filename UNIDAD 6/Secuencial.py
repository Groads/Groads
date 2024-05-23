def busqueda_secuencial(lista, objetivo):
    for i, elemento in enumerate(lista):
        if elemento == objetivo:
            return i
    return -1
lista = [3, 7, 1, 9, 4, 5]
objetivo = 9
resultado = busqueda_secuencial(lista, objetivo)

if resultado != -1:
    print(f"Elemento encontrado en la posición: {resultado}")
else:
    print("Elemento no encontrado en la lista")
