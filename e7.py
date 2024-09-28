import math
#A program számítsa ki egy beolvasott valós szám négyzetgyökét! A program adjon hibaüzenetet, ha a felhasználó negatív számból akar gyököt vonni!
def negyzetgyok():

    szam = float(input("Adjon meg egy számot!"))
    if szam > 0:
        gyok = math.sqrt(szam)
        print(gyok)
    else:
        print("HIBA: negatív szám gyökét akarja számolni")
