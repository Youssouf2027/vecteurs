from vecteurs import Vecteur
from vecteurs.frozendict import FrozenDict
import pytest

from vecteurs.matrice import Matrice

def test_creation():
    v = Vecteur([1,2,3,4])
    assert v._composantes == (1,2,3,4)

def test_repr():
    v = Vecteur((1, 2))
    assert repr(v) == "Vecteur((1, 2))"

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

def test_hash():
    v1 = Vecteur([1,2,3])
    v2 = Vecteur([1,2,3])
    assert hash(v1) == hash(v2)

    # -----------------------------------------second series of tests---------------------------------------------

def test_accessingValues():
    V= FrozenDict({'a': 1, 'b': 2, 'c': 3})
    assert V['a'] == 1

def test_length():
    V= FrozenDict({'a': 1, 'b': 2, 'c': 3})
    assert len(V) == 3

def test_iter():
    V= FrozenDict({'a': 1, 'b': 2, 'c': 3})
    keys = [key for key in V]
    assert keys == ['a', 'b', 'c']

def test_immutable():
    V= FrozenDict({'a': 1, 'b': 2, 'c': 3})
   
    with pytest.raises(TypeError):
        V['a'] = 4
def test_dict_key():
    fd = FrozenDict({"a": 1})
    d = {fd: "valeur"}
    assert d[fd] == "valeur"

def test_repre():
    m = Matrice([[1,2,3],[4,5,6]])
    assert repr(m) == "Matrice([1, 2, 3]\n        [4, 5, 6])"

def test_eq():
    m1 = Matrice([[1,2,3],[4,5,6]])
    m2 = Matrice([[1,2,3],[4,5,6]])
    assert m1 == m2

# m[i, j] returns the right element
def test_get_item():
    m = Matrice([[1,2,3],[4,5,6]])
    assert m[0, 1] == 2
    assert m[1, 2] == 6

# transpose() works
def test_transpose():
    m = Matrice([[1,2,3],[4,5,6]])
    transposed = m.transpose()
    assert transposed == Matrice([[1,4],[2,5],[3,6]])

# Matrix × Vecteur works
def test_matrix_vector_multiplication():
    m = Matrice([[1,2,3],[4,5,6]])
    v = Vecteur([7,8,9])
    result = m * v
    assert result == Vecteur([50, 122])  # 1*7 + 2*8 + 3*9 = 50 and 4*7 + 5*8 + 6*9 = 122

# Incompatible dimensions raise ValueError
def test_incompatible_dimensions():
    m1 = Matrice([[1,2,3],[4,5,6]])  # 2×3
    m2 = Matrice([[1,2],[3,4]])       # 2×2
    with pytest.raises(ValueError):
        m1 * m2