

def comptage_voyelle():
    pass

def lettre_trouvee(mots,lettre,mot_trouve):
    trouver = 0
    for i in range(len(mots)):
        if lettre == mots[i]:
            mot_trouve[i] = lettre
            trouver += 1
    return trouver,mot_trouve
    

def gagant(mot_trouve):
    for i in range(len(mot_trouve)):
        if mot_trouve[i] == "_":
            return 0
    return 1    


def perdant():
    print("Vous avez perdu")

def pendu():
    mot_a_trouver = "python"
    mot_trouve = ["_"]*len(mot_a_trouver)
    nombre_de_vie = 2
    while nombre_de_vie > 0:
        lettre = input("Entrez une lettre: ")
        trouver,mot_trouve = lettre_trouvee(mot_a_trouver,lettre,mot_trouve)
        
        if trouver == 0:
            nombre_de_vie -= 1
        print(mot_trouve)
        print("Il vous reste", nombre_de_vie, "vie")
        if gagant(mot_trouve) == 1:
            print("Vous avez gagné")
            break
            
    if nombre_de_vie == 0:
        perdant()
      
    

pendu()
