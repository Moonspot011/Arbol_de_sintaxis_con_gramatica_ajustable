import networkx as nx
import matplotlib.pyplot as plt

class Arbol:
    def __init__(self, archivo_gramatica):
        self.gramatica = self.cargar_gramatica(archivo_gramatica)
        self.simbolo_inicial = list(self.gramatica.keys())[0]
        
    def cargar_gramatica(self, archivo):
        gramatica = {}
        with open(archivo, 'r') as f:
            for linea in f:
                if "->" in linea:
                    izquierda, derecha = linea.strip().split("->")
                    izquierda = izquierda.strip()
                    producciones = [produccion.strip().split() for produccion in derecha.split("|")]
                    gramatica[izquierda] = producciones
        return gramatica
    
    def parsear(self, tokens):
        arbol =nx.DiGraph()
        exito, _ = self.expandir(self.simbolo_inicial, tokens, 0, arbol, None)
        return exito, arbol
    
    def expandir(self, simbolo, tokens, posicion, arbol, padre):
        nodo_id = f"f{simbolo}_{posicion}_{len(arbol)}"
        arbol.add_node(nodo_id, label=simbolo)
        if padre:
            arbol.add_edge(padre, nodo_id)
        if simbolo not in self.gramatica:
            if posicion < len(tokens):
                token = tokens[posicion]
                if token == simbolo:
                    return True, posicion + 1
                if simbolo == "num" and token.isdigit():
                    return True, posicion + 1
            return False, posicion
        
        for produccion in self.gramatica[simbolo]:
            nueva_posicion = posicion
            aceptado = True
            if produccion == ["ε"]:
                return True, nueva_posicion
            for simb in produccion:
                exito, nueva_posicion = self.expandir(simb, tokens, nueva_posicion, arbol, nodo_id)
                if not exito:
                    aceptado = False
                    break
            if aceptado:
                return True, nueva_posicion
        return False, posicion

def dibujar_arbol(arbol):
    posicion = nx.spring_layout(arbol)
    etiquetas = nx.get_node_attributes(arbol, "label")
    nx.draw(arbol, posicion, with_labels=True, labels=etiquetas, node_size=2000, node_color="lightblue")
    plt.show()
    
if __name__ == "__main__":
    parser = Arbol("gra.txt")
    
    while True:
        cadena = input("Ingrese una cadena (o 'salir'):").strip()
        if cadena.lower() == "salir":
            break
        tokens = cadena.split()
        exito, arbol = parser.parsear(tokens)
        if exito:
            print("Cadena aceptada")
            dibujar_arbol(arbol)
        else:
            print("Cadena no aceptada")