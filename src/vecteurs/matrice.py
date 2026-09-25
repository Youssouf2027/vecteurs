from __future__ import annotations
from vecteurs.vecteurs import Vecteur


class Matrice:
    def __init__(self, rows: list[list[int | float]]) -> None:
        if not rows:
            raise ValueError("La liste des lignes ne peut pas etre vide")
        row_length = len(rows[0])
        for row in rows:
            if len(row) != row_length:
                raise ValueError("Toutes les lignes doivent avoir la meme longueur")
        self._rows: list[list[int | float]] = [list(r) for r in rows]

    def __repr__(self) -> str:
        row_str = "\n        ".join(str(row) for row in self._rows)
        return f"Matrice({row_str})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Matrice):
            return NotImplemented
        return self._rows == other._rows

    def __getitem__(self, index: tuple[int, int]) -> int | float:
        i, j = index
        return self._rows[i][j]

    def transpose(self) -> Matrice:
        transposed_rows = [list(row) for row in zip(*self._rows)]
        return Matrice(transposed_rows)

    def __mul__(self, other: Vecteur | Matrice) -> Vecteur | Matrice:
        if isinstance(other, Vecteur):
            col_matrix = Matrice([[x] for x in other])
            result = self * col_matrix
            assert isinstance(result, Matrice)
            return Vecteur([row[0] for row in result._rows])

        if not isinstance(other, Matrice):
            return NotImplemented

        if len(self._rows[0]) != len(other._rows):
            raise ValueError("Dimensions incompatibles")

        n_rows = len(self._rows)
        n_cols = len(other._rows[0])
        result_rows: list[list[int | float]] = [[0] * n_cols for _ in range(n_rows)]

        for i in range(n_rows):
            for j in range(n_cols):
                for k in range(len(other._rows)):
                    result_rows[i][j] += self._rows[i][k] * other._rows[k][j]

        return Matrice(result_rows)
