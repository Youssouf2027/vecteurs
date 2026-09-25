from vecteurs.vecteurs import Vecteur
from vecteurs.frozendict import FrozenDict
from vecteurs.matrice import Matrice
import pytest


def test_creation() -> None:
    v = Vecteur([1, 2, 3, 4])
    assert v._composantes == (1, 2, 3, 4)

def test_repr() -> None:
    v = Vecteur((1, 2))
    assert repr(v) == "Vecteur((1, 2))"

def test_egalite() -> None:
    v1 = Vecteur([1, 2])
    v2 = Vecteur([1, 2])
    assert v1 == v2

def test_is_contre_egal() -> None:
    v1 = Vecteur([1, 2])
    v2 = Vecteur([1, 2])
    assert v1 is not v2
    assert v1 == v2

def test_longueur() -> None:
    v = Vecteur([1, 2, 3])
    assert len(v) == 3

def test_get_item() -> None:
    v = Vecteur([1, 2, 3])
    assert v[0] == 1
    assert v[1] == 2
    assert v[2] == 3
    assert v[0:2] == Vecteur([1, 2])

def test_iter() -> None:
    v = Vecteur([1, 2, 3])
    assert list(v) == [1, 2, 3]

def test_contains() -> None:
    v = Vecteur([1, 2, 3])
    assert 2 in v
    assert 4 not in v

def test_addition() -> None:
    v1 = Vecteur([1, 2, 3])
    v2 = Vecteur([4, 5, 6])
    assert v1 + v2 == Vecteur([5, 7, 9])

def test_soustraction() -> None:
    v1 = Vecteur([1, 2, 3])
    v2 = Vecteur([4, 5, 6])
    assert v2 - v1 == Vecteur([3, 3, 3])

def test_multiplication() -> None:
    v1 = Vecteur([1, 2, 3])
    v2 = Vecteur([4, 5, 6])
    assert v1 * 2 == Vecteur([2, 4, 6])
    assert v1 * v2 == 32

def test_abs() -> None:
    v = Vecteur([3, 4])
    assert abs(v) == 5.0

def test_neg() -> None:
    v = Vecteur([3, 4])
    assert -v == Vecteur([-3, -4])

def test_radd() -> None:
    v1 = Vecteur([1, 2, 3])
    assert 0 + v1 == v1

def test_rmul() -> None:
    v1 = Vecteur([1, 2, 3])
    assert 2 * v1 == Vecteur([2, 4, 6])

def test_hash() -> None:
    v1 = Vecteur([1, 2, 3])
    v2 = Vecteur([1, 2, 3])
    assert hash(v1) == hash(v2)

def test_frozendict_accessing_values() -> None:
    V = FrozenDict({"a": 1, "b": 2, "c": 3})
    assert V["a"] == 1

def test_frozendict_length() -> None:
    V = FrozenDict({"a": 1, "b": 2, "c": 3})
    assert len(V) == 3

def test_frozendict_iter() -> None:
    V = FrozenDict({"a": 1, "b": 2, "c": 3})
    keys = [key for key in V]
    assert keys == ["a", "b", "c"]

def test_frozendict_immutable() -> None:
    V = FrozenDict({"a": 1, "b": 2, "c": 3})
    with pytest.raises(TypeError):
        V["a"] = 4

def test_frozendict_dict_key() -> None:
    fd = FrozenDict({"a": 1})
    d = {fd: "valeur"}
    assert d[fd] == "valeur"

def test_matrice_repr() -> None:
    m = Matrice([[1, 2, 3], [4, 5, 6]])
    assert repr(m) == "Matrice([1, 2, 3]\n        [4, 5, 6])"

def test_matrice_eq() -> None:
    m1 = Matrice([[1, 2, 3], [4, 5, 6]])
    m2 = Matrice([[1, 2, 3], [4, 5, 6]])
    assert m1 == m2

def test_matrice_get_item() -> None:
    m = Matrice([[1, 2, 3], [4, 5, 6]])
    assert m[0, 1] == 2
    assert m[1, 2] == 6

def test_transpose() -> None:
    m = Matrice([[1, 2, 3], [4, 5, 6]])
    assert m.transpose() == Matrice([[1, 4], [2, 5], [3, 6]])

def test_matrix_vector_multiplication() -> None:
    m = Matrice([[1, 2, 3], [4, 5, 6]])
    v = Vecteur([7, 8, 9])
    result = m * v
    assert result == Vecteur([50, 122])

def test_incompatible_dimensions() -> None:
    m1 = Matrice([[1, 2, 3], [4, 5, 6]])
    m2 = Matrice([[1, 2], [3, 4]])
    with pytest.raises(ValueError):
        m1 * m2
