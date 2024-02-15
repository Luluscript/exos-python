# Exercice sur les Boucles sans While :
# Partie 1 - Utilisation de Boucles for :
# Créez une boucle for qui affiche les nombres de 1 à 5.


for i in range(1, 6):
    print(i)
# Partie 2 - Combinaison avec les Variables et les Conditions :
# Demandez à l'utilisateur de saisir un nombre.

nombre = input("Entrez un nombre entre 1 et 5: ")

# Utilisez une boucle for pour afficher le message "Boucle exécutée !" autant de fois que le nombre saisi par l'utilisateur.


for i in range(1, 6):
    if i == int(nombre):
        print("La boucle est exécutée")


# Partie 3 - Manipulation de Variables dans les Boucles :
# Utilisez une boucle for pour afficher chaque lettre du mot saisi par l'utilisateur sur une nouvelle ligne.

Mot = input("Entrez un mot: ")

for lettre in Mot:
    print(Mot)

import sys

mot = input("Entrez un mot : ")

for lettre in mot:
    print(lettre)
    sys.stdout.flush()

# Partie 4 - Utilisation de Boucles pour Calculs :
# Demandez à l'utilisateur de saisir un nombre entier.

valeur_x = input("entrez un chiffre:")
valeur_x= int(valeur_x)

def multiplication(x: int, y: int) -> int:
    resultat = x * y
    return resultat

# Utilisez une boucle for pour afficher la table de multiplication de ce nombre jusqu'à 10.


for valeur_y in range(1, 11):
    res = multiplication(x=valeur_x, y=valeur_y)
    print(res)
# Conseils :
# Utilisez range() pour créer une séquence de nombres dans une boucle for.
# Assurez-vous de convertir les entrées de l'utilisateur en types appropriés si nécessaire.
# Pensez à utiliser les opérateurs de comparaison pour les conditions.
# Cette version simplifiée de l'exercice utilise uniquement des boucles for pour renforcer la compréhension de l'utilisation des boucles en Python.