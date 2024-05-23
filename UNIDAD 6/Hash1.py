def buscar_en_diccionario(diccionario, clave):
    if clave in diccionario:
        return diccionario[clave]
    else:
        return None

diccionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
clave = 'c'
resultado = buscar_en_diccionario(diccionario, clave)

if resultado is not None:
    print(f"Clave encontrada. Valor: {resultado}")
else:
    print("Clave no encontrada en el diccionario")
