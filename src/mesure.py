from memory_profiler import memory_usage

# let's see how it is like without generator
def voyons(chemin):
    with open(chemin) as f:
        file=f.readlines()
    return len(file)
        



        
# with generator
def charger(chemin):
    with open(chemin) as f:
        for ligne in f:
            yield ligne

def version_generateur(chemin):
    count=0
    for ligne in charger(chemin):
        count+=1
    return count



if __name__ == '__main__':
    mem_liste = memory_usage((voyons, ("test_grand_fichier.txt",)), interval=0.1)
    mem_gen = memory_usage((version_generateur, ("test_grand_fichier.txt",)), interval=0.1)
    
    print(f"Version liste      — mémoire max : {max(mem_liste):.1f} Mo")
    print(f"Version générateur — mémoire max : {max(mem_gen):.1f} Mo")