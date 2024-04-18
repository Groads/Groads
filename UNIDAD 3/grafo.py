import networkx as nx
import matplotlib.pyplot as plt

# Definición de los estados y sus relaciones con los costos de traslado
estados = {
    'CDMX': {'Puebla': 130, 'Hidalgo': 120, 'EdoMex': 100},
    'Puebla': {'CDMX': 130, 'Veracruz': 200, 'Morelos': 90},
    'Hidalgo': {'CDMX': 120, 'Queretaro': 80, 'Pachuca': 50},
    'EdoMex': {'CDMX': 100, 'Morelos': 120, 'Queretaro': 200},
    'Veracruz': {'Puebla': 200, 'Oaxaca': 150, 'Tabasco': 180},
    'Morelos': {'Puebla': 90, 'EdoMex': 120, 'Guerrero': 100},
    'Queretaro': {'Hidalgo': 80, 'EdoMex': 200, 'Guanajuato': 120},
    'Oaxaca': {'Veracruz': 150, 'Chiapas': 100, 'Guerrero': 180},
    'Tabasco': {'Veracruz': 180, 'Chiapas': 200},
    'Guerrero': {'Morelos': 100, 'Oaxaca': 180, 'Chiapas': 150},
    'Chiapas': {'Oaxaca': 100, 'Tabasco': 200, 'Guerrero': 150, 'Guanajuato': 300},
    'Guanajuato': {'Queretaro': 120, 'Chiapas': 300}
}

# Crear el grafo
G = nx.Graph()

# Agregar nodos al grafo
for estado in estados:
    G.add_node(estado)

# Agregar aristas ponderadas al grafo
for estado, conexiones in estados.items():
    for vecino, costo in conexiones.items():
        G.add_edge(estado, vecino, weight=costo)

# Función para calcular el costo total de un recorrido entre dos puntos especificados
def calcular_costo_entre_puntos(punto_inicio, punto_fin):
    try:
        recorrido = nx.shortest_path(G, source=punto_inicio, target=punto_fin, weight='weight')
        costo_total = sum(G[recorrido[i]][recorrido[i+1]]['weight'] for i in range(len(recorrido) - 1))
        return recorrido, costo_total
    except nx.NetworkXNoPath:
        print("No se encontró un camino entre", punto_inicio, "y", punto_fin)
        return None, None

# Función para imprimir el recorrido y su costo
def imprimir_recorrido(recorrido):
    print("->".join(recorrido))
    print("Costo total:", calcular_costo_entre_puntos(recorrido[0], recorrido[-1])[1])

# Función para encontrar un recorrido sin repetición utilizando DFS
def encontrar_recorrido_sin_repetir():
    inicio = list(estados.keys())[0]
    recorrido = list(nx.dfs_preorder_nodes(G, source=inicio))
    recorrido.append(inicio)  # Agregar el inicio al final para formar un circuito
    return recorrido

# Función para encontrar un recorrido con al menos un estado repetido
def encontrar_recorrido_con_repetición():
    inicio = list(estados.keys())[0]
    recorrido = list(nx.dfs_preorder_nodes(G, source=inicio))
    # Modificar el recorrido para incluir al menos un estado repetido
    recorrido_con_repetición = recorrido[:-1] + [recorrido[1]]
    return recorrido_con_repetición

# Función para dibujar el grafo
def dibujar_grafo():
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=2000, node_color='lightblue', font_size=10)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()

# Recorrer todos los 7 estados sin repetir ninguno
recorrido_sin_repetir = encontrar_recorrido_sin_repetir()
imprimir_recorrido(recorrido_sin_repetir)

# Recorrer los 7 estados repitiendo al menos uno de ellos
recorrido_con_repetición = encontrar_recorrido_con_repetición()
imprimir_recorrido(recorrido_con_repetición)

# Dibujar el grafo
dibujar_grafo()

