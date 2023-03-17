import pytest
import operaciones
def test_suma():
    a=1
    b=2
    resultado=3
    assert resultado==operaciones.suma(a,b)

def test_resta():
    a=1
    b=2
    resultado=3
    assert resultado==operaciones.resta(a,b)

def test_div():
    a=1
    b=2
    resultado=3
    assert resultado==operaciones.div(a,b)

def test_mul():
    a=1
    b=2
    resultado=3
    assert resultado==operaciones.multiplicar(a,b)
