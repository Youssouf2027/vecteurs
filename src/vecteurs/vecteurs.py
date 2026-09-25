from __future__ import annotations
from typing import Iterator
from typing import Iterator
import math


class Vecteur:
    def __init__(self, composantes: list[int | float] | tuple[int | float, ...]) -> None:
        if not composantes:
            raise ValueError("La liste des composantes ne peut pas etre vide")
        if not all(isinstance(x, (int, float)) for x in composantes):
            raise ValueError("Toutes les composantes doivent etre des nombres")
        self._composantes: tuple[int | float, ...] = tuple(composantes)

    def __repr__(self) -> str:
        return f"Vecteur({self._composantes})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vecteur):
            return NotImplemented
        return self._composantes == other._composantes

    def __len__(self) -> int:
        return len(self._composantes)

    def __getitem__(self, index: int | slice) -> int | float | Vecteur:
        if isinstance(index, slice):
            return Vecteur(self._composantes[index])
        return self._composantes[index]

    def __iter__(self) -> Iterator[int | float]:
        return iter(self._composantes)

    def __contains__(self, item: object) -> bool:
        return item in self._composantes

    def __add__(self, other: Vecteur) -> Vecteur:
        if not isinstance(other, Vecteur):
            return NotImplemented
        return Vecteur([a + b for a, b in zip(self._composantes, other._composantes)])

    def __sub__(self, other: Vecteur) -> Vecteur:
        return Vecteur([a - b for a, b in zip(self._composantes, other._composantes)])

    def __mul__(self, other: int | float | Vecteur) -> int | float | Vecteur:
        if isinstance(other, (int, float)):
            return Vecteur([a * other for a in self._composantes])
        if isinstance(other, Vecteur):
            return sum(a * b for a, b in zip(self._composantes, other._composantes))
        return NotImplemented

    def __abs__(self) -> float:
        return math.sqrt(sum(a ** 2 for a in self._composantes))

    def __neg__(self) -> Vecteur:
        return Vecteur([-a for a in self._composantes])

    def __radd__(self, other: int | float) -> Vecteur:
        if other == 0:
            return self
        return NotImplemented

    def __rmul__(self, other: int | float) -> int | float | Vecteur:
        return self.__mul__(other)

    def __hash__(self) -> int:
        return hash(self._composantes)
