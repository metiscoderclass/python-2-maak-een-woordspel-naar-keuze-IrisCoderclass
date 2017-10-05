while True:
    print("Welkom bij galgje, probeer het woord te raden, als je wil stoppen typ QQ, als je het woord wil raden typ ?.")
    W = "csharp"
    G = 0
    L = input("Geef een letter")
    L = L.lower()

    if (L == "c" or "s" or "h" or "a" or "r" or "p"):
        GL = GL + L
        AGL = len(GL)
        if (AGL == 6):
            GWL = input("Wat denk je dat het woord is?")
            GWL = GWL.lower()
            if (GWL == W):
                print("Goed geraden!")
                break
            else:
                print("Sorry, dat was fout.")
                G = G + 1
    if (L == "?"):
        GW = input("Wat denk je dat het woord is?")
        GW = GW.lower()
        if (GW == W) :
            print("Goed geraden!")
            break
        else:
            print("Sorry, dat was fout.")
            G = G + 1
    elif not L.isalpha():
        print("ERROR: Je mag alleen letters invoeren")
    if (L == "QQ"):
        print("Doei")
        break
    if (G == 5):
        print("Sorry je hebt verloren, het woord was CSharp")
        break



