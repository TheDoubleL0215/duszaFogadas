from jatek_letrehozasa import *
from fogadas import *
from jatek_lezaras import *

def mainMenu():
    firstChoose = int(input(
        '''
        Üdvözlünk a fogadás oldalon!

        Válassz az alábbi opciók közül:

        1 -- Játék létrehozása
        2 -- Fogadás leadása
        3 -- Játék lezárása
        4 -- Lekérdezések
        5 -- Kilépés
        
        '''
    ))
    if firstChoose == 1:
        letrehozas()
    if firstChoose == 2:
        fogadasLeadasa()
    if firstChoose == 3:
        lezaras()
    if firstChoose == 5:
        print("Viszlát")
    
while True:
    mainMenu()