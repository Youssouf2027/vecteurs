class Vecteur:
    def __init__(self, composantes):
        if not composantes:
            raise ValueError("LA liste des composantes ne peut pas être vide")
        if not all(isinstance(x,(int,float)) for x in composantes):
            raise ValueError("Toutes les composantes doivent être des nombres")
        self._composantes = list(composantes) 


    def __repr__(self):
        return f"Vecteur({self._composantes})"

    def __eq__(self,other):
        if not isinstance(other,Vecteur):
            return NotImplemented
        return self._composantes == other._composantes