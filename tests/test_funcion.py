from random import random
from panela.funcion import Constante, Identidad, InversaAditiva, InversaMultiplicativa


def test_evaluar_constante():
    constante = 5
    f = Constante(constante)
    for _ in range(0,1000):
        assert f.Evaluar(random()) == constante

def test_evaluar_identidad():
    f = Identidad()
    for _ in range(0,1000):
        x = random()
        assert f.Evaluar(x) == x

def test_evaluar_inversa_aditiva():
    constante = 5 
    f = InversaAditiva(Constante(constante))
    g = InversaAditiva(Identidad())
    for _ in range(0,1000):
        x = random()
        assert f.Evaluar(x)+constante == 0.0
        assert g.Evaluar(x)+x == 0.0

def test_evaluar_inversa_multiplicativa():
    constante = 5 
    f = InversaMultiplicativa(Constante(constante))
    g = InversaMultiplicativa(Identidad())
    for _ in range(0,1000):
        x = random()
        assert f.Evaluar(x)*constante == 1.0
        assert abs(g.Evaluar(x)*x - 1.0) < 1e-15

# Derivada
# Integral
# Cache
# Composicion
    # Log
    # Exp

# OperacionBinaria
# Suma
# Multiplicacion
# Max
# Min