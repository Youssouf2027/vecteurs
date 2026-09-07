from vecteurs import Vecteur

def test_creation():
    v = Vecteur([1,2,3,4])
    assert v._composantes == [1,2,3,4]

def test_repr():
    v = Vecteur([1, 2])
    assert repr(v) == "Vecteur([1, 2])"

def test_egalite():
    v1 = Vecteur([1, 2])
    v2 = Vecteur([1, 2])
    assert v1 == v2

def test_is_contre_egal():
    v1 = Vecteur([1, 2])
    v2 = Vecteur([1, 2])
    assert v1 is not v2
    assert v1 == v2
    