class Pila:
    def __init__(self, capacidad_maxima=8):
        self.capacidad_maxima = capacidad_maxima
        self.pila = []
        self.tope = 0

    def insertar(self, elemento):
        if self.tope < self.capacidad_maxima:
            self.pila.append(elemento)
            self.tope += 1
            print(f"Insertado {elemento}. Pila: {self.pila}")
        else:
            print(f"Error: Desbordamiento. No se puede insertar {elemento}, la pila está llena.")

    def eliminar(self):
        if self.tope > 0:
            elemento_eliminado = self.pila.pop()
            self.tope -= 1
            print(f"Eliminado {elemento_eliminado}. Pila: {self.pila}")
        else:
            print(f"Error: Subdesbordamiento. No hay elementos para eliminar, la pila está vacía.")

mi_pila = Pila()

mi_pila.insertar('X')  
mi_pila.insertar('Y')  
mi_pila.eliminar()     
mi_pila.eliminar()     
mi_pila.eliminar()     
mi_pila.insertar('V')  
mi_pila.insertar('W')  
mi_pila.eliminar()     
mi_pila.insertar('R')  

print(f"Elementos finales en la pila: {mi_pila.pila}")
print(f"Total de elementos en la pila: {mi_pila.tope}")
