GL = ""
FL = ""
W = "banaan"
G = 0
AL= len(W)

while True:
    print("Welkom bij galgje, probeer het woord te raden, als je wil stoppen typ QQ, als je het woord wil raden typ ?.")
    L = input("Geef een letter")
    L = L.lower()

    if (L == "?"):
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
    elif not L.isalpha():
        print("ERROR: Je mag alleen letters invoeren")
    if (L == "QQ"):
        print("Doei")
        break
    if L in GL:
        print("Deze letter heb je al een keer geraden.")
    elif L in FL:
        print("Deze letter heb je al een keer geraden.")
    elif L in W:
        GL = GL + L
        AGL = len(GL)
        print("Je goed geraden letters zijn: " + GL)
        print("Je fout geraden letters zijn: " + FL)
        if (AGL == AL):
            GWL = input("Wat denk je dat het woord is?")
            GWL = GWL.lower()
            if (GWL == W):
                print("Goed geraden!")
                break
            else:
                print("Sorry, dat was fout.")
                G = G + 1
                print("Je goed geraden letters zijn: " + GL)
    else:
        print("Dat was fout")
        G = G + 1
        FL = FL + L
        print("Je goed geraden letters zijn: " + GL)
        print("Je fout geraden letters zijn: " + FL)
    if (G == 5):
        print("Sorry je hebt verloren, het woord was " + W)
        break