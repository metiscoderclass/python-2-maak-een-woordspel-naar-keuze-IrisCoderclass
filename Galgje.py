while True:
    print("Welkom bij galgje, probeer het woord te raden, als je wil stoppen typ QQ, als je het woord wil raden typ ?.")
    W = "CSharp"
    G = 0
    L = input("Geef een letter")
    if (L == "?"):
        GW = input("Wat denk je dat het woord is?")
        if (GW == "CSharp" or "csharp" or "Csharp" or "cSharp" or "CSHARP") :
            print("Goed geraden!")
            break
        if not (GW == "CSharp" or "csharp" or "Csharp" or "cSharp" or "CSHARP") :
            print("Sorry, dat was fout.")
    elif not L.isalpha():
        print("ERROR: Je mag alleen letters invoeren")
    if (L == "QQ"):
        print("Doei")
        break


