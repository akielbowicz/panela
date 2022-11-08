class Servicio:

   def cobrar(self, edificacion):
       return edificacion.consumo(self)

   def costoParaCasa(self, parametros):
       return 1.0  

   def costoParaDepartamento(self, parametros):
       return 1.0  

class Agua(Servicio):

   def cobrar(self, edificacion):
       return edificacion.consumoDeAgua(self)

class Gas(Servicio):
   
   def cobrar(self, edificacion):
       return edificacion.consumoDeGas(self)

class Electricidad(Servicio):
   
   def cobrar(self, edificacion):
       return edificacion.consumoDeElectricidad(self)