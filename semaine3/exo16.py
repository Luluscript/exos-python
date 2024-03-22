#EXO16

employes = {}
liste = [10, 2329, 5, "Pierre", 203, "Marie", 867, "Adrien"]

compteur = 1

for element in liste:
    if isinstance(element, str):
        cle = "id-" + str(compteur).zfill(2)
        employes[cle] = element
        compteur += 1

print(employes)

#EXO17

liste = ["Pierre", "Paul", "Marie"]

for indice, element in enumerate(liste, start=0):
    print(indice, element)


#EXO18

ma_liste = [1, 2, 3]

ma_liste.extend([4, 5, 6])

print(ma_liste)

#EXO19

print(len("bonjour"))
def new_len(variable):
    count = 0
    for x in variable:
        count += 1
    return count

mot = 'bonjour'
resultat = new_len(mot)
print(resultat)



