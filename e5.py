def honap():

    szam = int(input("Kérem ajon meg egfy hónap sorszámot'"))
    if szam <= 0 or szam >= 13:
        print("Hiba: a megadott szám nem egy hónap sorszáma")
    else:
        if szam == 1:
        print("Január")
        elif szam == 2:
        print("Február")
        elif szam == 3:
        print("Március")