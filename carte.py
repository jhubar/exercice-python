from random import randint
compteur_carte_pair = 0
compteur_tirage = 0 
while compteur_carte_pair < 3:
    carte = randint(1,13)
    print(carte)
    if carte % 2 == 0:
        compteur_carte_pair += 1
    compteur_tirage += 1
      
if compteur_tirage >=4:
    print("Apres le 4eme tirage, on a eu", compteur_carte_pair, "cartes paires")
