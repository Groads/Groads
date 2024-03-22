class Pedido:
    def __init__(self, cantidad, cliente):
        self.cliente = cliente
        self.cantidad = cantidad

    def imprimir_pedido(self):
        print("     Cliente: " + self.obtener_cliente())
        print("     Cantidad: " + str(self.obtener_cantidad()))
        print("     ------------")

    def obtener_cantidad(self):
        return self.cantidad

    def obtener_cliente(self):
        return self.cliente


class InterfazCola:
    def tamano(self):
        pass

    def esta_vacia(self):
        pass

    def frente(self):
        pass

    def agregar(self, info):
        pass

    def quitar(self):
        pass


class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class Cola(InterfazCola):
    def __init__(self):
        self.nodo_frente = None
        self.nodo_final = None

    def tamano(self):
        tamano = 0
        nodo_actual = self.nodo_frente
        while nodo_actual:
            tamano += 1
            nodo_actual = nodo_actual.siguiente
        return tamano

    def esta_vacia(self):
        return self.nodo_frente is None

    def frente(self):
        if self.esta_vacia():
            return None
        return self.nodo_frente.dato

    def agregar(self, info):
        nuevo_nodo = Nodo(info)
        if self.esta_vacia():
            self.nodo_frente = nuevo_nodo
            self.nodo_final = nuevo_nodo
        else:
            self.nodo_final.siguiente = nuevo_nodo
            self.nodo_final = nuevo_nodo

    def quitar(self):
        if self.esta_vacia():
            return None
        dato_quitado = self.nodo_frente.dato
        self.nodo_frente = self.nodo_frente.siguiente
        if self.nodo_frente is None:
            self.nodo_final = None
        return dato_quitado

pedido1 = Pedido(20, "cli1")
pedido2 = Pedido(30, "cli2")
pedido3 = Pedido(40, "cli3")
pedido4 = Pedido(50, "cli4")

pedido1.imprimir_pedido()
pedido2.imprimir_pedido()
pedido3.imprimir_pedido()
pedido4.imprimir_pedido()

print("********* COLA DUMP *********")
print("   Tamaño: " + str(4))

cola = Cola()
cola.agregar(pedido1)
cola.agregar(pedido2)
cola.agregar(pedido3)
cola.agregar(pedido4)

nodo_actual = cola.nodo_frente
num_elemento = 1
while nodo_actual is not None:
    print("   ** Elemento " + str(num_elemento))
    nodo_actual.dato.imprimir_pedido()
    num_elemento += 1
    nodo_actual = nodo_actual.siguiente

print("******************************")
