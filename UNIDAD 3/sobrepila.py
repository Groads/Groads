class MiPila:
    def __init__(self, capacidad_maxima):
        self.max_elem = capacidad_maxima
        self.pila_data = [None] * capacidad_maxima
        self.topo = 0

    def agregar(self, elemento):
        if self.topo < self.max_elem:
            self.pila_data[self.topo] = elemento
            self.topo += 1
            print("Agregado:", elemento)
        else:
            print("Error de desbordamiento: la pila está llena")

    def quitar(self):
        if self.topo > 0:
            elemento_quitar = self.pila_data[self.topo - 1]
            self.topo -= 1
            print("Quitado:", elemento_quitar)
        else:
            print("Error de subdesbordamiento: la pila está vacía")

operaciones = ['X', 'Y', 'Z', 'T', 'U', 'V', 'W', 'p', 'R']

mi_pila = MiPila(8)

for operacion in operaciones:
    if operacion in ['X', 'Y', 'V', 'W', 'R']:
        mi_pila.agregar(operacion)
    else:
        mi_pila.quitar()

print("Número de elementos en la pila:", mi_pila.topo)