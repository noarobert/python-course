# Choix de la table 
table = int(input("Quelle table voulez-vous afficher ? : "))

# Liste pour stocker les résultats
resultats = []

# Calculer et stocker les 10 premiers résultats
for i in range(1, 11):
    resultat = table * i
    resultats.append(resultat)

# Afficher la liste des résultats
print(resultats)




