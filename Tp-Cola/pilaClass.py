class Pila():
    
    def __init__(self):  #metodo constructor self-> referencia al abjeto que esta llamando
        self.elements = []

    def __eq__(self, stack_aux):
        if isinstance(stack_aux, Pila):
            return self.__elements == stack_aux.__elements
        else:
            return False

    def push(self, dato):
        self.elements.append(dato)


    def pop(self):
        if self.size() > 0:
            dato = self.elements.pop()
            return dato
        
    def size(self):
        return len(self.elements)

    
    def on_top(self):
        if self.size() > 0:
            return self.elements[-1]

