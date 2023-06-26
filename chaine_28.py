# chaine de 28 caractères 
chaine = "Une_chaine_de_28_caracteres."
chaine_tmp = ""
compteur  = 0


for i in range(0,len(chaine)):
    chaine_tmp += chaine[i]
    compteur += 1
    if compteur == 7:
        print(chaine_tmp)
        compteur = 0
        chaine_tmp = ""
        
        
