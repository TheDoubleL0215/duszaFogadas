def fogadasLeadasa():

    # Load fogadasok
    fogadasFile = open("txt/fogadasok.txt", "r+", encoding='utf-8')
    fogadasok = fogadasFile.readlines()
    listedPersons = []
    allPersonCredential = []
    allGameDetails = []

    #Main
    aktivSzavazasok = []
    print(fogadasok)

    for line in fogadasok:
        print(f"Ez a line: {line}")
        fogado_neve = line.split(';')[0]
        listedPersons.append(fogado_neve)
        fogado_jatek_nev = line.split(';')[1]
        fogado_tet = int(line.split(';')[2])
        fogado_fogadott_alany = line.split(';')[3]
        fogado_esemeny_nev = line.split(';')[4]
        fogado_esemeny_ertek = line.split(';')[5]

        betPerson = {
            "name" : fogado_neve,
            "jatek_nev" : fogado_jatek_nev,
            "jatek_tet" : fogado_tet,
            "jatek_alany" : fogado_fogadott_alany,
            "jatek_esemeny_nev" : fogado_esemeny_nev,
            "jatek_esemeny_ertek" : fogado_esemeny_ertek
        }
        allPersonCredential.append(betPerson)

    print(f"Ez az allperson",allPersonCredential)

    #Load jatekok
    jatekokFile = open("txt/jatekok.txt", "r+", encoding='utf-8')
    jatekok = jatekokFile.readlines()
    informationLines = []
    allLines = []
    # Az összes sor lekérése
    for x in jatekok:
        allLines.append(x)
    print("EZ AZ ALL LINE: ", allLines)

    # Információs sor lekérése
    for sor in jatekok:
        if ";" in sor:
            informationLines.append(sor)
            letrehozoNeve = sor.split(';')[0]
            szavazasNeve = sor.split(';')[1]
            alanySzam = sor.split(';')[2]
            esemSzam = int(sor.split(';')[3].replace("\n", ""))
            tempAlanyCounter = 0
            alanyIndiNevList = []
            tempElemCounter = 0
            elemIndiNevList = []
            for x in range(int(alanySzam)):
                alanyIndiNevId = allLines.index(sor) + 1 + tempAlanyCounter
                alanyIndiNev = allLines[alanyIndiNevId].replace("\n", "")
                alanyIndiNevList.append(alanyIndiNev)
                tempAlanyCounter += 1
            for y in range(esemSzam):
                elemIndiNevId = allLines.index(sor) + 1 + tempAlanyCounter
                print(elemIndiNevId)
                elemIndiNev = allLines[elemIndiNevId].replace("\n", "")
                elemIndiNevList.append(elemIndiNev)
                tempAlanyCounter += 1

            jsonjatek = {
                "letrehozoNeve" : letrehozoNeve,
                "szavazasNeve" : szavazasNeve,
                "alanySzam" : alanySzam,
                "esemSzam" : esemSzam,
                "alanyIndiNevList" : alanyIndiNevList,
                "elemIndiNevList" : elemIndiNevList
            }

            allGameDetails.append(jsonjatek)

    print("Ez a info ", informationLines)
    print("Van Isten! ", allGameDetails)

    # User auth
    validateName = True
    while(validateName):
        fogadoNeve = input("Fogadó neve: ")
        if fogadoNeve == "" or fogadoNeve == " ":

            print("A fogadó neve helytelen, adjon meg egy valós nevet")
        else:
            #Innentől a valid userrel hajt végre műveleteket
            validateName = False
            if fogadoNeve in listedPersons:
                for item in allPersonCredential:
                    if item["name"] == fogadoNeve:
                        kredit = 100 - item["jatek_tet"]
            else:
                kredit = 100
            print(f'''
                Üdvözlünk {fogadoNeve}!
                Felhasználható kredited: {kredit}
                Aktív szavazások:
            ''')
            gamesNamesList = []
            tempgameNameCount = 0
            for x in allGameDetails:
                gameName = x["szavazasNeve"]
                print(f"{tempgameNameCount+1} -- {gameName}")
                gamesNamesList.append(gameName)
                tempgameNameCount += 1

            notValidChose = True
            while(notValidChose):
                chosenpole = int(input(">> "))
                if chosenpole > len(gamesNamesList):
                    print("Valós értéket adj meg!")
                else:
                    inChosenGame = allGameDetails[chosenpole-1]
                    #Data
                    inChosenGameCreator = inChosenGame["letrehozoNeve"]
                    inChosenGameName = inChosenGame["szavazasNeve"]
                    inChosenGameAlanys = inChosenGame["alanyIndiNevList"]
                    inChosenGameEvents = inChosenGame["elemIndiNevList"]

                    print(f'''
                        Szavazás neve: {inChosenGameName}
                        Létrehozó: {inChosenGameCreator}
                        Alanyok: 
                    
                    ''')

                    tempAlanysCount = 0
                    tempEventsCount = 0
                    for x in range(len(inChosenGame["alanyIndiNevList"])):
                        print(f"{tempAlanysCount+1} -- {inChosenGameAlanys[tempAlanysCount]}")
                        tempAlanysCount += 1

                    print("Események: ")

                    for x in range(len(inChosenGame["elemIndiNevList"])):
                        print(f"{tempEventsCount+1} -- {inChosenGameEvents[tempEventsCount]}")
                        tempEventsCount += 1


                    userChoseAlany = int(input("Alany >> "))
                    userChoseEvent = int(input("Esemény >> "))
                    chipsTrue = True
                    while(chipsTrue):
                        userchoseBet = int(input("Tét >> "))
                        if(userchoseBet > kredit):
                            print("Túl nagy összeget adtál meg")
                        else:
                            chipsTrue = False
                    result = input("Eredmény >> ")


                    fogadasFile.write(f"\n"+str(fogadoNeve)+";"+str(inChosenGameName)+";"+str(userchoseBet)+";"+str(inChosenGameAlanys[userChoseAlany-1])+";"+str(inChosenGameAlanys[userChoseEvent-1])+";"+str(result))

                    notValidChose = False


        