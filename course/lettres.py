text = 'Hello World!'

# Convertir le texte en minuscules
text = text.lower()

# Initialiser le dictionnaire de résultat avec des comptes initiaux à zéro
resultat = {chr(i): 0 for i in range(ord('a'), ord('z')+1)}

# Parcourir le texte et compter les lettres
for char in text:
    if 'a' <= char <= 'z':
        resultat[char] += 1

# Afficher le résultat
print(resultat)