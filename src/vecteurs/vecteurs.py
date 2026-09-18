import math
class Vecteur:
    def __init__(self,composantes):
        if not composantes:
            raise ValueError("LA liste des composantes ne peut pas être vide")
        if not all(isinstance(x,(int,float)) for x in composantes):
            raise ValueError("Toutes les composantes doivent être des nombres")
        self._composantes = tuple(composantes) 

    def __repr__(self):
        return f"Vecteur({self._composantes})"

    def __eq__(self,other):
        if not isinstance(other,Vecteur):
            return NotImplemented
        return self._composantes == other._composantes
    def __len__(self):
        return len(self._composantes)
    def __getitem__(self,index):
        if isinstance(index,slice):
            return(Vecteur(self._composantes[index]))
        return self._composantes[index]
    def __iter__(self):
        return iter(self._composantes)

    def __contains__(self,item):
        return item in self._composantes
    def __add__(self,other):
        if not isinstance(other,Vecteur):
            return NotImplemented
        return Vecteur([a+b for a,b in zip(self._composantes,other._composantes)])

    def __sub__(self,other):
        return Vecteur([a-b for a,b in zip(self._composantes,other._composantes)])

    def __mul__(self,other):
        if isinstance(other,(int,float)):
            return Vecteur([a*other for a in self._composantes])
        if isinstance(other,Vecteur):
            return sum(a*b for a,b in zip(self._composantes,other._composantes))

    def __abs__(self):
        return math.sqrt(sum (a**2 for a in self._composantes))

    def __neg__(self):
        return Vecteur([-a for a in self._composantes])

    def __radd__(self,other):
        if other == 0:
            return self
        return NotImplemented

    def __rmul__(self,other):
        return self.__mul__(other)

    def __hash__(self):
        return hash(self._composantes)

            