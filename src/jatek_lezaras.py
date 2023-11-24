def lezaras():
    nev = input('Név: ')
    jatek_neve = input('Játék neve: ')
    with open('txt/jatekok.txt', 'r', encoding='utf-8') as fajl0:
        jatekok = fajl0.readlines()
    for sor in jatekok:
         if ';' in sor:
            print(sor)
            szervezo = sor.split(';')[0]
            jatek = sor.split(';')[1] 
            if jatek_neve == jatek and nev == szervezo:
                sorlista = []
                with open('txt/fogadasok.txt', 'r', encoding='utf-8') as fajl:
                    fogadasok = fajl.readlines()
                fogadasok = [s.strip() for s in fogadasok] 
                for fogadas in fogadasok:
                    felosztas3 = fogadas.split(',')
                    for sor in felosztas3:
                        felosztas4 = sor.split(';')
                        sorlista.append(felosztas4)
                print(sorlista)
            else:
                print('Próbáld újra!')
lezaras()
