names = ["toto" ,"lulu" ,"fred" ,"thanos"]
ville = ["paris" ,"marseille"]
nb = 1

for x in names:
    if x == "thanos":
        print(f"bonjour thanos")
    else:
        print(f"pas de thanos")

def findOccurence(l: list, search: str):
    for x in l:
        if x == search:
            print(f"bonjour {x}")
        else:
            print(f"pas de {search}")

def addition(x: int, y: int) -> int:
    resultat = x + y
    return resultat


n = "paris"
print("1er appel de fonction")
findOccurence(names, n)
print("2eme appel de fonction")
findOccurence(ville, n)

res = addition(4, 8)

res2 = addition(7, 9)

print(res)
print(res2)

res3 = addition(res, res2)

print(res3)


