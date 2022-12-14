from abc import ABC, abstractmethod

class Funcion(ABC):

    @abstractmethod
    def op(self, valor):
        pass

    def Evaluar(self, valor):
        return self.op(valor)

class Constante(Funcion):

    def __init__(self, valor) -> None:
        self._valor = valor

    def op(self, valor):  return self._valor

class Identidad(Funcion):

    def op(self, valor): return valor

class Operacion(Funcion):

    def __init__(self, argumento):
        self.interna_ = argumento

    def Evaluar(self, valor):
        return self.op(self.interna_.Evaluar(valor))

class InversaAditiva(Operacion):

    def op(self, valor): return -valor

class InversaMultiplicativa(Operacion):

    def op(self, valor): return 1/valor