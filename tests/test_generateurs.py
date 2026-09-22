import tempfile
import os
from vecteurs.generateurs import charger

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