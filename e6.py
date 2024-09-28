def szog():

vSzam = float(input("Kérem adjon meg egy valós számot!"))
if (vSzam >= 0) and (vSzam <=360):
    if vSzam == 0:
        print(vSzam+" -> nullszög")
    elif (vSzam>0) and (vSzam<90):
        print(str(vSzam)+" -> hegyesszög")
    elif vSzam == 90:
        print(str(vSzam) + " -> derékszög")
    if (vSzam >= 90) and (vSzam <=180):
        print(vSzam + " -> tompaszög")
    elif vSzam == 180:
        print(str(vSzam) + " -> "egyeneszög")
    if (vSzam >= 180) and (vSzam <= 360):
            print(vSzam + " -> homorúszög")
    elif vSzam == 360:
        print(str(vSzam) + " -> "teljesszöh")
else:print("HIBA: nem jó")