class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self, elemento):
        self.items.append(elemento)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        else:
            raise IndexError("La pila está vacía")

    def ver_tope(self):
        if not self.esta_vacia():
            return self.items[-1]
        else:
            raise IndexError("La pila está vacía")
mi_pila = Pila()

mi_pila.apilar(30)
mi_pila.apilar(60)
mi_pila.apilar(50)

print("Tope de la pila:", mi_pila.ver_tope())

while not mi_pila.esta_vacia():
    elemento = mi_pila.desapilar()
    print("Desapilando:", elemento)
