# Exercice sur les Variables et les Conditions :

# Partie 1 - Variables et Conditions simples :
# Demandez à l'utilisateur de saisir son âge.
# Stockez cette valeur dans une variable appelée age.

age = 31
# Utilisez une condition pour vérifier si l'âge est supérieur ou égal à 18.

if age >= 18:
    print("vous etes majeur")
else:
    print("vous etes majeur")
# Affichez "Vous êtes majeur !" si la condition est vraie, sinon affichez "Vous êtes mineur."

# Partie 2 - Types de Variables :
# Créez une nouvelle variable appelée nom et demandez à l'utilisateur de saisir son nom.

nom = "lulu"
taille = 1.65
# Créez une troisième variable appelée taille et demandez à l'utilisateur de saisir sa taille (en mètres).
# Utilisez des conditions pour déterminer si la taille de la personne est supérieure à 1.75 mètres. Affichez un message approprié en conséquence.

if taille >= 1.75:
    print ("ts ok")
else:
    print ("t'es un naim")

# Partie 3 - Manipulation de Chaînes de Caractères :
# Concaténez le nom et l'âge pour créer une nouvelle variable appelée message.
# Affichez le message résultant.

message = nom + str(taille)
print (message)

# Partie 4 - Types de Variables Avancées :
# Convertissez l'âge en float.
age = float(age)
# Multipliez la taille par l'âge et stockez le résultat dans une nouvelle variable appelée resultat.
# Affichez le résultat.

def multiplication(x: float, y: float) -> float:
    resultat = x * y
    return resultat

resultat= multiplication(x=age, y=taille)
print(resultat)


# Conseils :
# Utilisez la fonction input() pour obtenir des valeurs de l'utilisateur.

nom_utilisateur = input("Entrez votre nom : ")
print("j'ai envie de te sucer " + nom_utilisateur + " !")

# Pensez à convertir les entrées de l'utilisateur en types appropriés (par exemple, utilisez int() pour convertir une entrée en entier).
# Utilisez les opérateurs de comparaison (<, >, <=, >=, ==, !=) pour les conditions.
# Ce exercice encourage la compréhension des variables, des conditions, des types de variables et de la manipulation de chaînes de caractères en Python.

nom_utilisateur2 = input("Entrez votre nom : ")
print("Bonjour " + nom_utilisateur + " !")

taille_utilisateur = input("Entrez votre taille : ")
age_utilisateur = input("Entrez votre age: ")
print("Vous avez" + age_utilisateur + " ans, et vous mesurez " + taille_utilisateur + " centimètres.")

if taille >= 1.75:
    print ("its ok")
else:
    print ("T'es un naim")



