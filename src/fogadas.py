def fogadasLeadasa():
    validateName = True
    while(validateName):
        fogadoNeve = input("Fogadó neve: ")
        if fogadoNeve == "" or fogadoNeve == " ":
            print("A fogadó neve helytelen, adjon meg egy valós nevet")

fogadasLeadasa()