n = 16
star = "*"

def demi_losange():
    for i in range(1, n//2+1):
        ligne = "*" * i
        print(ligne)

    for i in range(n//2+1, n+1):
        ligne = star * (n+1-i)
        print(ligne)


n2 = 9

def demi_losange2():
    for i in range(n):
        ligne = "*" * i
        print(ligne)

    for i in range(n):
        ligne = star * (n-i)
        print(ligne)

#EXO 12

produits = [
    {"nom": "Ordinateur", "prix": 1000},
    {"nom": "Smartphone", "prix": 500},
    {"nom": "Tablette", "prix": 300},
]


def reduc_produits():
    for x in produits:
        x["prix"] -= 0.1 * x["prix"]
        print(x["prix"])


#EXO13

lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

print(lorem.upper())
print(lorem.lower())
print(lorem.count(" elit"))
print(lorem.replace("dolor","horor"))
print(lorem.split("consectetur"))

#EXO 14
import math

# Utilisation de la valeur de pi
valeur_pi = math.pi
print(valeur_pi)

rayon = 10.0

def calculer_volume_sphere(float) -> float:
    volume = (4 * math.pi / 3) * (rayon ** 3)
    print(volume)


calculer_volume_sphere(rayon)


#EXO 15


def addition(a, b):
        c = a + b
        return c


resultat = addition(5, 10)
print(resultat)



