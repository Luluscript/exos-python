
#EXO 3
def exo_3():
    n = 11
    dollar = "$"

    for x in range(n):
        print(" " * (n-x) + (dollar + " ") * x)


#EXO 4
ma_liste = ["Pierre", "Paul", "Marie"]
def exo_4():
    premier_element = ma_liste[0]
    dernier_element = ma_liste[-1]
    print(premier_element, dernier_element)

    deux_premiers = ma_liste[0:2]
    deux_derniers = ma_liste[-2:4]
    print(len(ma_liste))
    print(deux_premiers)
    print(deux_derniers)

#EXO 5
def exo5():
    site_web = "Docstring"
    langage = "Python"
    prenom = "Patrick"

    le_doc = site_web[0:3]
    print(le_doc)

    #print(len(langage))
    le_python = langage[-4:len(langage)+1]
    print(le_python)

#EXO6
def exo6():
    # Changez les valeurs de a et / ou b 👇
    a = 6
    b = 10

    # Ne touchez pas à cette ligne ⛔️
    vrai_01 = a + b == 16

    # Changez les valeurs de a et / ou b 👇
    a = 4
    b = 4

    # Ne touchez pas à cette ligne ⛔️
    vrai_02 = bool(a * b)

    # Changez les valeurs de a et / ou b 👇
    a = "45"
    b = "4"

    # Ne touchez pas à cette ligne ⛔️
    vrai_03 = bool(int(a) - int(b))

    print(vrai_01)
    print(vrai_02)
    print(vrai_03)


#EXO 7
def exo7():
    resultat = range(2, 101, 2)
    for x in resultat:
        print(x)
    #liste = range(1, 101)
    #def filter_pairs2(li:[int]) -> list[int]:
        #pairs = []
        #for x in li:
            #if x % 2 == 0:
                #pairs += [x]
                #pairs = pairs + [x]
        #return pairs


    #resultat = filter_pairs2(liste)
    #print(resultat)


#EXO 8
def exo8():
    prenom = "Pierre"

    if type(prenom) == str:
        resultat = "Premiere verification réussie"
        print(resultat)

    prenom = 0

    if type(prenom) == str:
        resultat = "Deuxieme verification réussie"
        print(resultat)


#EXO 9
def exo9():
    site_web = "Docstring"
    mot = site_web

    for lettre in mot:
        print(lettre)

    une_liste = ["je m'appelle Ludivine"]
    print(type(une_liste))

    un_dictionnaire = {"un chien": "animal a 4 pattes"}
    print(type(un_dictionnaire))

    un_tuple = ("Pomme", "Banane", "chocolat")
    print(type(un_tuple))

    un_set = {"Pomme", "Banana", "cocolat"}
    print(type(un_set))

#list : tableau d’éléments indexés de 0 à n exclu auquel on peut ajouter ou retirer des éléments
#dict : tableau d’éléments indexés par des types immuables auquel on peut ajouter ou retirer des éléments
#tuple : tableau d’éléments indexés de 0 à n exclu qu’on ne peut pas modifier
#set : tableau d’éléments uniques non indexés
#frozenset : set immuables (non modifiable)

print("exo7")
exo9()