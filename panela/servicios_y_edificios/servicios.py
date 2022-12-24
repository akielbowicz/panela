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

   def costoParaDepartamento(self, parametros):
        return super().costoParaDepartamento(parametros)/2

class Gas(Servicio):
   
   def cobrar(self, edificacion):
        return edificacion.consumoDeGas(self)

   def costoParaDepartamento(self, parametros):
        return super().costoParaCasa(parametros) / 10
    
   def costoParaCasa(self, parametro):
        return 100 * super().costoParaCasa(parametro)        
    
class Electricidad(Servicio):
   
   def cobrar(self, edificacion):
       return edificacion.consumoDeElectricidad(self)

   def costoParaCasa(self, parametro):
        return 10 * super().costoParaCasa(parametro) 
        
   def costoParaDepartamento(self, parametros):
        return super().costoParaCasa(parametros) * 3.5