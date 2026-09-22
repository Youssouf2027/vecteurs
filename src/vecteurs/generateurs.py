def charger(chemin):
    with open(chemin) as f:
        for ligne in f:
            yield ligne