import collections
from typing import Tuple, List, Type

numbers = [5, 9, 2, 9, 6, 6, 3, 8, 9, 10]

# collections.Iterable est un type generique.
# Il comprend tous les types iterable comme les listes, les tableaux, les tuples etc...
#def calculate_mean2(it: collections.Iterable):
#    somme = 0
#    for i in it:
#        somme = somme + i


# list est un type plus specifique.
def calculate_mean(li: list[int]) -> float:
    somme = 0
    count = 0
    for i in li:
        count = count + 1
        somme = somme + i
    print(somme)
    print(count)
    result = somme / count
    return result


def calculate_mean3(li: list) -> float:
    somme = 0
    for i in li:
        somme = somme + i
    result = somme / len(li)
    return result


res = calculate_mean(numbers)
print(res)
print(type(res))


res2 = calculate_mean3(numbers)
print(res2)
print(type(res2))


def filter_pairs(li: list[int]) -> list[int]:
    pairs = [x for x in li if x % 2 == 0]
    return pairs



def filter_pairs2(li: list[int]) -> list[int]:
    pairs = []
    for x in li:
        if x % 2 == 0:
            #pairs += [x]
            pairs = pairs + [x]
    print(f"ceci est ma list {pairs}")
    return pairs

filter_pairs2(numbers)



res3 = filter_pairs(numbers)
print(res3)


def find_max(li: list[int]) -> int:
    max_number = max(li)
    return max_number


def find_max2(li: list[int]) -> int:
    max = 0
    for x in li:
        for y in li:
            if x > y:
                max = x
    print(f"FRED MAX {max}")
    return max

find_max2(numbers)

res4 = find_max(numbers)
print(res4)


def modify_list(li: list[int]) -> list[int]:
    calcul = [x * 2 for x in li]
    return calcul


# i correspond à l'index dans ma liste. Je démarre à la position 0 de ma liste (i = 0)
# a chaque itération de boucle for, j'incrémente mon index de 1 (Position 1, puis 2, puis 3...etc)
# dans ma boucle, je multiple la valeur x à la position i, par 2 puis j'itère.
#ici c'est la liste qui est modifiée, et non une création de copie modifiée
def modify_list2(li: list[int]) -> list[int]:
    i = 0
    for x in li:
        li[i] = x * 2
        i += 1
        # i = i + 1
    print(f"FRED LIST x 2 : {li}")
    return li

modify_list2(numbers)

res5 = modify_list(numbers)
print(res5)

print("condenser fonction !")
def display_results(li: list[int]) -> tuple[list[Type[list]], list[Type[list]], list[Type[list]]]:
    resultat1 = []
    resultat2 = []
    resultat3 = []

    somme = 0
    count = 0
    for i in li:
        count = count + 1
        somme = somme + i
    resultat1 = somme / len(li)

    resultat2 = [x for x in li if x % 2 == 0]

    resultat3 = [x * 2 for x in li]

    return resultat1, resultat2, resultat3


res6 = display_results(numbers)
print(res6)


def display_res(li: list):
    print("DISPLAY RESULT")
    print(calculate_mean(li))
    print(filter_pairs(li))
    print(find_max(li))

display_res(numbers)

numbers = [5, 9, 2, 9, 6, 6, 3, 8, 9, 10]
for x in numbers:
    if x % 2 == 0:
        print(f"pair")
    else:
        print(f"impair")

if 1 == True:
    print("1 cest vrai")
if 0 == False:
    print("O cest faux")



for x in numbers:
    if x > 5:
        print(f"je suis pas certaine d'avoir compris l'énnoncé")

if calculate_mean(numbers) > float(5):
    print("cest une bonne moyenne")
