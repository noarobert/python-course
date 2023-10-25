import random

def choix_utilisateur():
    choix = input("Choisissez Pierre (P), Feuille (F) ou Ciseaux (C) : ").strip().upper()
    while choix not in ["P", "F", "C"]:
        print("Choix invalide. Veuillez choisir entre Pierre (P), Feuille (F) ou Ciseaux (C).")
        choix = input("Choisissez Pierre (P), Feuille (F) ou Ciseaux (C) : ").strip().upper()
    return choix

def choix_ordinateur():
    return random.choice(["P", "F", "C"])

def determiner_gagnant(choix_utilisateur, choix_ordinateur):
    if choix_utilisateur == choix_ordinateur:
        return "match nul"
    elif (choix_utilisateur == "P" and choix_ordinateur == "C") or \
         (choix_utilisateur == "C" and choix_ordinateur == "F") or \
         (choix_utilisateur == "F" and choix_ordinateur == "P"):
        return "utilisateur"
    else:
        return "ordinateur"

score_utilisateur = 0
score_ordinateur = 0

while score_utilisateur < 2 and score_ordinateur < 2:
    print(f"Score actuel - Utilisateur: {score_utilisateur}, Ordinateur: {score_ordinateur}")
    choix_u = choix_utilisateur()
    choix_o = choix_ordinateur()

    print(f"Utilisateur choisit {choix_u}")
    print(f"Ordinateur choisit {choix_o}")

    gagnant = determiner_gagnant(choix_u, choix_o)
    if gagnant == "match nul":
        print("Match nul !")
    else:
        print(f"{gagnant.capitalize()} gagne la manche !")
        if gagnant == "utilisateur":
            score_utilisateur += 1
        else:
            score_ordinateur += 1

if score_utilisateur > score_ordinateur:
    print("Utilisateur remporte la partie !")
else:
    print("Ordinateur remporte la partie !")

# Enregistrement du jeu dans un fichier
with open("jeu_shifumi.txt", "a") as f:
    f.write(f"Résultat final - Utilisateur: {score_utilisateur}, Ordinateur: {score_ordinateur}\n")

