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

def test_addition():
    v1 = Vecteur([1,2,3])
    v2 = Vecteur([4,5,6])
    v3 = Vecteur([5,7,9])
    assert v1+v2 == v3

def test_soustrction():
    v1 = Vecteur([1,2,3])
    v2 = Vecteur([4,5,6])
    v3 = Vecteur([3,3,3])
    assert v2-v1 == v3

def test_multiplication():
    v1 = Vecteur([1,2,3])
    v2 = Vecteur([4,5,6])
    assert v1*2 == Vecteur([2,4,6])
    assert v1*v2 == 32

def test_abs():
    v=Vecteur([3,4])
    assert abs(v) == 5.0

def test_neg():
    v=Vecteur([3,4])
    assert -v == Vecteur([-3,-4])

def test_radd():
    v1 = Vecteur([1,2,3])
    v2 = 0
    assert v2 + v1 == v1

def test_rmul():
    v1 = Vecteur([1,2,3])
    assert 2 * v1 == Vecteur([2,4,6])