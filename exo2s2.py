texte = "Ca commence a piquer severe"

txt = ["C", "a"]


def analyze_text(s: str):
    mots = 0
    lettres = 0
    # je compte le nombre de lettre en comptant le nombre de fois que ma boucle itere
    for x in s:
        lettres += 1
        # je compte le nombre de mots, en comptant le nombre de caractères vide (" ") auquel je rajoute 1
        if x == " ":
            mots += 1
            print("j'ai un espace")

    print(f"J'ai {mots+1} mots")
    print(f"j'ai {lettres} lettres")


def analyze_text2(s: str):
    index = 0
    last_space = 0
    word_list = []
    for x in s:
        index += 1
        if x == " ":
            word_list.append(s[last_space:index-1])
            last_space = index
    print(word_list)
    print(f"J'ai {len(word_list)+1} mots")


analyze_text(texte)
analyze_text2(texte)


def analyze_text3(s: str):
    count = 0
    for i in s:
        count = count + 1
    print(count)

analyze_text3(texte)