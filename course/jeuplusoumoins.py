import random

# Générer un nombre aléatoire entre 0 et 100
nombre_aléatoire = random.randint(0, 100)

# Initialiser le compteur de coups
nombre_de_coups = 0

# Boucle pour permettre à l'utilisateur de deviner
while True:
    try:
        devine = int(input("Devinez le nombre entre 0 et 100 : "))
        nombre_de_coups += 1

        if devine < nombre_aléatoire:
            print(f"Le nombre est plus grand que {devine}")
        elif devine > nombre_aléatoire:
            print(f"Le nombre est plus petit que {devine}")
        else:
            print(f"Bravo, vous avez trouvé en {nombre_de_coups} essais.")
            break
    except ValueError:
        print("Entrez un nombre valide.")

# Fin du jeu
