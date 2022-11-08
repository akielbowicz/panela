class Edificacion:
    _litros = 0.0
    _watts  = 0.0
    _m3     = 0.0

    def __init__(self, litros, watts, m3):
        self._litros = litros
        self._watts  = watts
        self._m3     = m3
    
    def consumo(self, servicio):
        return 9999.9
    
    def consumoDeAgua(self, servicio):
        raise NotImplementedError()

    def consumoDeElectricidad(self, servicio):
        raise NotImplementedError()

    def consumoDeGas(self, servicio):
        raise NotImplementedError()

class Casa(Edificacion):

    def consumoDeAgua(self, servicio):
        return servicio.costoParaCasa(self._litros)

    def consumoDeElectricidad(self, servicio):
        return servicio.costoParaCasa(self._watts)

    def consumoDeGas(self, servicio):
        return servicio.costoParaCasa(self._m3)

class Departamento(Edificacion):

    def consumoDeAgua(self, servicio):
        return servicio.costoParaDepartamento(self._litros)

    def consumoDeElectricidad(self, servicio):
        return servicio.costoParaDepartamento(self._watts)

    def consumoDeGas(self, servicio):
        return servicio.costoParaDepartamento(self._m3)