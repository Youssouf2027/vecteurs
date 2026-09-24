import tempfile
import os
from vecteurs.generateurs import charger
from vecteurs.generateurs import mon_chain, mon_islice, mon_groupby

def test_nombre_de_lignes():
    # créer un fichier temporaire avec 3 lignes
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
        f.write("ligne 1\n")
        f.write("ligne 2\n")
        f.write("ligne 3\n")
        chemin = f.name
    
    # compter les lignes produites par le générateur
    lignes = list(charger(chemin))

   

    
    # vérifier
    assert len(lignes) == 3
  

    
    # nettoyer
    os.remove(chemin)




def test_fichier_vide():
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
        chemin = f.name  # fichier vide — rien écrit
    
    lignes = list(charger(chemin))
    
    assert len(lignes) == 0  # combien de lignes dans un fichier vide ?
    
    os.remove(chemin)

def test_mon_chain():
    iterable1 = [1, 2, 3]
    iterable2 = ['a', 'b']
    iterable3 = [True, False]
    
    result = list(mon_chain(iterable1, iterable2, iterable3))
    
    assert result == [1, 2, 3, 'a', 'b', True, False]

def test_mon_islice():
    iterable = range(10)
    result = list(mon_islice(iterable, 3, 7))
    
    assert result == [3, 4, 5, 6]

def test_mon_groupby():
    data = [1, 1, 2, 2, 2, 3, 3, 1]
    key_func = lambda x: x
    
    result = list(mon_groupby(data, key_func))
    
    expected = [(1, [1, 1]), (2, [2, 2, 2]), (3, [3, 3]), (1, [1])]
    
    assert result == expected