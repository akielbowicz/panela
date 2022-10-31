from abc import ABC, abstractmethod
from gettext import install

class Booleano(ABC):
    _instance = None

    def __new__(cls):
        if cls._instance:
           raise Exception("Usar verdadero.")
        cls._instance = super().__new__(cls)
        return cls._instance
    
    @abstractmethod
    def Negar(self):
        pass

    @abstractmethod
    def Y(self, otro):
        pass

    @abstractmethod
    def SiEsVerdadero(self, bloque):
        pass

    @abstractmethod
    def SiEsFalso(self, bloque):
        pass

    @abstractmethod
    def SiEs(self, bloqueSiV, bloqueSiF):
        pass

    def __eq__(self, __o: object) -> bool:
        return type(self) == type(__o)

    def __repr__(self) -> str:
        return str(type(self).__name__)

class Verdadero(Booleano):

    def Negar(self):
        return falso

    def Y(self, otro):
        return otro

    def O(self, otro):
        return self

    def SiEsVerdadero(self, bloque):
        return bloque()

    def SiEsFalso(self, bloque):
        return

    def SiEs(self, bloqueSiV, bloqueSiF):
        return bloqueSiV()

class Falso(Booleano):

    def Negar(self):
        return verdadero

    def Y(self, otro):
        return self

    def O(self, otro):
        return otro

    def SiEsVerdadero(self, bloque):
        return

    def SiEsFalso(self, bloque):
        return bloque()

    def SiEs(self, bloqueSiV, bloqueSiF):
        return bloqueSiF()

verdadero = Verdadero()
falso = Falso()