# Exercice sur les Fonctions :
# Partie 1 - Définition et Appel de Fonctions :
# Créez une fonction appelée saluer qui affiche le message "Bonjour, bienvenue !" lorsqu'elle est appelée.
def saluer(name_utilisateur):
    print("bonjour," + name_utilisateur + " bienvenue !")


name_utilisateur = input("Entrer votre nom:")
# Appelez la fonction saluer pour vérifier qu'elle affiche correctement le message.

saluer(name_utilisateur)


# Partie 2 - Paramètres de Fonctions :
# Modifiez la fonction saluer pour prendre un paramètre nom.
# Modifiez l'appel de la fonction pour passer votre nom en argument.

# Partie 3 - Retour de Fonctions :
# Créez une nouvelle fonction appelée carre qui prend un nombre en paramètre et renvoie le carré de ce nombre.
# Appelez la fonction carre avec un nombre de votre choix et affichez le résultat.

def carre(x):
    resultat = x * x
    return resultat


res = carre(5)
print(res)


# Partie 4 - Utilisation de Fonctions dans une Condition :
# Modifiez la fonction carre pour qu'elle renvoie -1 si le nombre passé en paramètre est négatif.
# Utilisez une condition pour afficher le carré du nombre si le résultat n'est pas -1, sinon affichez "Nombre négatif, impossible de calculer le carré."

def carre_2(x):
    if x < 0:
        return -1
    else:
        resultat = x * x
        return resultat


res2 = carre_2(-4)
if res2 != -1:
    print(res2)
else:
    print("Nombre négatif, impossible de calculer le carré.")


# Conseils :
# Utilisez le mot-clé def pour définir une fonction.
# Utilisez les parenthèses pour définir les paramètres de la fonction.
# Utilisez le mot-clé return pour renvoyer une valeur à partir d'une fonction.
# Appelez vos fonctions avec les arguments appropriés.
# Cet exercice vise à familiariser les débutants avec la création, l'appel, et la modification de fonctions en Python.
