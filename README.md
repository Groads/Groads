### Hola Mundo🙌
class Pila:
    def _init_(self):
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
<!--
**Groads/Groads** is a ✨ _special_ ✨ repository because its `README.md` (this file) appears on your GitHub profile.

Here are some ideas to get you started:

- 🔭 I’m currently working on ...
- 🌱 I’m currently learning ...
- 👯 I’m looking to collaborate on ...
- 🤔 I’m looking for help with ...
- 💬 Ask me about ...
- 📫 How to reach me: ...
- 😄 Pronouns: ...
- ⚡ Fun fact: ...
-->
