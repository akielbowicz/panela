from panela.servicios_y_edificios.edificacion import Casa, Departamento
from panela.servicios_y_edificios.servicios import Agua, Electricidad, Gas

casa = Casa(litros=10.0, watts=3.0, m3=100.0)
departamento = Departamento(litros=5.0, watts=20.0, m3=0.0)

def test_cobro_de_Agua():
    assert Agua().cobrar(casa)== 1.0
    assert Agua().cobrar(departamento)== 0.5
    
def test_cobro_de_Electricidad():
    assert Electricidad().cobrar(casa) == 10.0
    assert Electricidad().cobrar(departamento) == 3.5

def test_cobro_de_Gas():
    assert Gas().cobrar(casa) == 100.0
    assert Gas().cobrar(departamento) == 0.1