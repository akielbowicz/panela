from abc import ABC, abstractmethod

class Funcion(ABC):

    def __init__(self) -> None:
        self.interna_ = lambda x: None

    def Evaluar(self, valor):
        return self.interna_(valor)

class Constante(Funcion):

    def __init__(self, valor) -> None:
        self.interna_ = lambda x: valor

class Identidad(Funcion):

    def __init__(self) -> None:
        self.interna_ = lambda x: x

class Operacion(Funcion):

    def __init__(self, argumento):
        self.interna_ = argumento

    @abstractmethod
    def op(self, valor):
        pass

    def Evaluar(self, valor):
        return self.op(self.interna_.Evaluar(valor))


class InversaAditiva(Operacion):

    def op(self, valor): return -valor

class InversaMultiplicativa(Operacion):

    def op(self, valor): return 1/valor