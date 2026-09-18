# Représentation interne : liste de listes (chaque sous-liste est une ligne)
# Choix : plus lisible et plus simple à manipuler qu'une liste plate
from vecteurs.vecteurs import Vecteur
class Matrice:
    def __init__(self,rows):
        if not rows:
            raise ValueError("La liste des lignes ne peut pas être vide")

        # Validate that all rows have the same length
        row_length = len(rows[0])
        for row in rows:
            if len(row) != row_length:
                raise ValueError("Toutes les lignes doivent avoir la même longueur")

        self._rows = list(rows)

    def __repr__(self):
        row_str = "\n        ".join(str(row) for row in self._rows)
        return f"Matrice({row_str})"

    def __eq__(self,other):
        if not isinstance(other, Matrice):
            return NotImplemented
        return self._rows == other._rows

    def __getitem__(self,index):
        i,j = index

        return self._rows[i][j]

    def transpose(self):
        transposed_rows = [list(row) for row in zip(*self._rows)]
        return Matrice(transposed_rows) 

    def __mul__(self, other):
        if isinstance(other, Vecteur):
            col = [[x] for x in other]
            other_as_matrix = Matrice(col)
            result = self * other_as_matrix
            return Vecteur([row[0] for row in result._rows])
        
        if not isinstance(other, Matrice):
            return NotImplemented
        
        if len(self._rows[0]) != len(other._rows):
            raise ValueError("Dimensions incompatibles")
        
        row = len(self._rows)
        col = len(other._rows[0])
        result_rows = [[0] * col for _ in range(row)]
        
        for i in range(row):
            for j in range(col):
                for k in range(len(other._rows)):
                    result_rows[i][j] += self._rows[i][k] * other._rows[k][j]
        
        return Matrice(result_rows)
                    
       

        
        
        
        
        



     