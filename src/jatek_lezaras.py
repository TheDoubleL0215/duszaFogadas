import os

def lezaras():
    nev = input('Név: ')
    jatek_neve = input('Játék neve: ')
    with open('txt/jatekok.txt', 'r', encoding='utf-8') as fajl0:
        jatekok = fajl0.readlines()
    for sor in jatekok:
         if ';' in sor:
            szervezo = sor.split(';')[0]
            jatek = sor.split(';')[1] 
            if jatek_neve == jatek and nev == szervezo:
                print("Üdvözlünk!\n")
                path = 'txt/eredmenyek.txt'
                # Megvizsgáljuk, hogy létre van-e hozva a fájl
                check_file = os.path.isfile(path)
                




                sorlista = []
                with open('txt/fogadasok.txt', 'r', encoding='utf-8') as fajl:
                    fogadasok = fajl.readlines()
                if check_file:
                    file = open("txt/eredmenyek.txt", "a", encoding="utf-8")
                else:
                    file = open("txt/eredmenyek.txt", "x", encoding="utf-8")
                    file = open("txt/jatekok.txt", "a", encoding="utf-8")
                file.write(jatek+"\n")
                fogadasok = [s.strip() for s in fogadasok] 
                for fogadas in fogadasok:
                    felosztas3 = fogadas.split(',')
                    for sor in felosztas3:
                        felosztas4 = sor.split(';')
                        sorlista.append(felosztas4)
                        if felosztas4[1] == jatek:
                            
                            file.write(szervezo+";"+felosztas4[4]+";"+felosztas4[5])


lezaras()