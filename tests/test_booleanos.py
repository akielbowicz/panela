import pytest
from panela.booleano import Falso, Verdadero

@pytest.mark.parametrize("booleano",[Verdadero(),Falso()])
def test_negacion(booleano):
    assert booleano.Negar().Negar() == booleano

def test_Y():
    v = Verdadero()
    f = Falso()
    assert v.Y(v) == v
    assert v.Y(f) == f
    assert f.Y(v) == f
    assert f.Y(f) == f
    
def test_O():
    v = Verdadero()
    f = Falso()
    assert v.O(v) == v
    assert v.O(f) == v
    assert f.O(v) == v
    assert f.O(f) == f

def test_SiEs():
    v = Verdadero()
    f = Falso()
    assert v.SiEsVerdadero(lambda : 1) == 1
    assert v.SiEsFalso(lambda : 1) == None
    assert f.SiEsVerdadero(lambda : 1) == None
    assert f.SiEsFalso(lambda : 1) == 1