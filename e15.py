def egeszBeolvas():
    szam = int(input("Kérem adjon meg egy egész számot!"))
    return szam
def teglalap():
    oldal1 = egeszBeolvas()
    oldal2 = egeszBeolvas()

    if oldal1>0 and (oldal2 > 0):
        kerulet = 2 * (oldal1 + oldal2)
        terulet = oldal1 * oldal2
        print("A téglalap kerülete: " + str(kerulet) + ", területe: " + str(terulete))
else
    print("Hiba: a téglap oldalai nem pozitívak")
