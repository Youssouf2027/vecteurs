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
def test_longueur():
    v=Vecteur([1,2,3])
    assert len(v) == 3

def test_get_item():
    v = Vecteur([1,2,3])
    assert v[0] == 1
    assert v[1] == 2
    assert v[2] == 3
    assert v[0:2] == Vecteur([1, 2])

def test_iter():
    v = Vecteur([1,2,3])
    for x in v:
        assert list(v) == [1, 2, 3]
def test_contains():
    v = Vecteur([1,2,3])
    assert 2 in v
    assert 4 not in v