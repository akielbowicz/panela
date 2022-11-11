import pytest
from panela.booleano import Verdadero,Falso, falso, verdadero

@pytest.mark.parametrize("booleano",[verdadero,falso])
def test_negacion(booleano):
    assert booleano.Negar().Negar() == booleano

def test_Y():
    v = verdadero
    f = falso
    assert v.Y(v) == v
    assert v.Y(f) == f
    assert f.Y(v) == f
    assert f.Y(f) == f
    
def test_O():
    v = verdadero
    f = falso
    assert v.O(v) == v
    assert v.O(f) == v
    assert f.O(v) == v
    assert f.O(f) == f

def test_SiEs():
    v = verdadero
    f = falso
    assert v.SiEsVerdadero(lambda : 1) == 1
    assert v.SiEsFalso(lambda : 1) == None
    assert v.SiEs(lambda : 1, lambda : None) == 1

    assert f.SiEsVerdadero(lambda : 1) == None
    assert f.SiEsFalso(lambda : 1) == 1
    assert f.SiEs(lambda : None, lambda: 1) == 1

    
def test_son_unicas_instancias():
    with pytest.raises(Exception):
        Verdadero()

    with pytest.raises(Exception):
        Falso()
