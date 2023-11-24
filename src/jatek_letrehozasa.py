import os.path
def letrehozas():
    path = 'txt/jatekok.txt'

    check_file = os.path.isfile(path)
    
    if check_file:
        file = open("txt/jatekok.txt", "a", encoding="utf-8")
    else:
        file = open("txt/jatekok.txt", "x", encoding="utf-8")
        file = open("txt/jatekok.txt", "a", encoding="utf-8")

    

    szervezo = input("Szervező: ")
    jatek = input("Játék megnevezése: ")
    alanyok = input("Alanyok (veszzővel elválasztva): ")
    esemenyek = input("Események (vesszővel elválasztva): ")

    alanyok_list = []
    esemenyek_list = []
    alanyok_szama = alanyok.count(",")+1
    esemenyek_szama = esemenyek.count(",")+1

    file.write(szervezo+";"+jatek+";"+str(alanyok_szama)+";"+str(esemenyek_szama)+"\n")

    for i in range(alanyok_szama):
        alanyok_list.append(alanyok.split(",")[i])
        file.write(alanyok.split(",")[i]+"\n")
    
    for i in range(esemenyek_szama):
        esemenyek_list.append(esemenyek.split(",")[i])
        file.write(esemenyek.split(",")[i]+"\n")

letrehozas()