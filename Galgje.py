import random
GL = ""
FL = ""
woordenlijst = ["csharp", "banaan","unity", "minecraft", "overwatch", "japan", "anime", "laptop", "metis", "nintendo", "apple"]
W = random.choice(woordenlijst)
G = 0
AL = len(W)
WRGL = ""

def printtussenstand():
    global WRGL
    WRGL = ""
    for L in W:
        if L in GL:
            WRGL = WRGL + L
        else:
            WRGL = WRGL + "_"
    print(WRGL)

while True:
    print("Welkom bij galgje, probeer het woord te raden, als je wil stoppen typ QQ, als je het woord wil raden typ ?.(the word can be a programming language or a brand or game name, so watch out)")
    L = input("Geef een letter")
    L = L.lower()
    LL = len(L)

    if (L == "qq"):
        print("Doei")
        break

    elif not (LL == 1):
        print("ERROR: Je mag niet meer dan een letter invoeren")

    elif (L == "?"):
        GW = input("Wat denk je dat het woord is?")
        GW = GW.lower()
        if (GW == W) :
            print("Goed geraden!")
            break
        else:
            print("Sorry, dat was fout.")
            G = G + 1
            print("Je goed geraden letters zijn: " + GL)
            print("Je fout geraden letters zijn: " + FL)
            printtussenstand()
    elif not L.isalpha():
        print("ERROR: Je mag alleen letters invoeren")

    elif L in GL:
        print("Deze letter heb je al een keer geraden.")

    elif L in FL:
        print("Deze letter heb je al een keer geraden.")

    elif L in W:
        GL = GL + L
        print("Je goed geraden letters zijn: " + GL)
        print("Je fout geraden letters zijn: " + FL)
        printtussenstand()


    else:
        print("Dat was fout")
        G = G + 1
        FL = FL + L
        print("Je goed geraden letters zijn: " + GL)
        print("Je fout geraden letters zijn: " + FL)
        printtussenstand()


    if (G == 5):
        print("Sorry je hebt verloren, het woord was " + W)
        print("__________  ")
        print("|/       |  ")
        print("|       ( ) ")
        print("|       /|\ ")
        print("|       / \ ")
        print("|           ")
        print("|           ")
        print("|           ")
        print("| ____      ")
        break
    elif(G == 4):
        print("__________  ")
        print("|/          ")
        print("|           ")
        print("|           ")
        print("|           ")
        print("|           ")
        print("|           ")
        print("|           ")
        print("| ____      ")
    elif(G == 3):
        print("            ")
        print("|/          ")
        print("|           ")
        print("|           ")
        print("|           ")
        print("|           ")
        print("|           ")
        print("|           ")
        print("| ____      ")
    elif(G == 2):
        print("            ")
        print("|           ")
        print("|           ")
        print("|           ")
        print("|           ")
        print("|           ")
        print("|           ")
        print("|           ")
        print("| ____      ")
    elif(G == 1):
        print("            ")
        print("            ")
        print("            ")
        print("            ")
        print("            ")
        print("            ")
        print("            ")
        print("            ")
        print(" ____       ")

    if (WRGL == W):
        print("Je hebt gewonnen, het woord was " + W)
        break