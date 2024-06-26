def busqueda_binaria(lista, objetivo):
    izquierda, derecha = 0, len(lista) - 1
    
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    
    return -1

lista = [1, 3, 4, 5, 7, 9]
objetivo = 5
resultado = busqueda_binaria(lista, objetivo)

if resultado != -1:
    print(f"Elemento encontrado en la posición: {resultado}")
else:
    print("Elemento no encontrado en la lista")
