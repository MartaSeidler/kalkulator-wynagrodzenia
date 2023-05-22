print("""
*** KALKULATOR WYNAGRODZENIA NETTO DO UMOWY O PRACĘ W 2023 ROKU ***
""")

brutto = int(input("Podaj wynagrodzenie brutto: "))


# obliczenie składek
skladka_emerytalna_procent = 9.76 / 100
skladka_rentowa_procent = 1.5 / 100
skladka_chorobowa_procent = 2.45 / 100

skladka_emerytalna = round((skladka_emerytalna_procent * brutto), 2)
skladka_rentowa = round((skladka_rentowa_procent * brutto), 2)
skladka_chorobowa = round((skladka_chorobowa_procent * brutto), 2)

skladki = skladka_emerytalna + skladka_rentowa + skladka_chorobowa

podstawa_skladki_zdrowotnej = brutto - skladki
skladka_zdrowotna_procent = 9 / 100
skladka_zdrowotna = round((skladka_zdrowotna_procent * podstawa_skladki_zdrowotnej), 2)


# obliczenie podatku
czy_koszty_zwiekszone = input("""
Czy Twój zakład pracy znajduje się poza miejscowością, w której mieszkasz?
t = tak
n = nie
""")

if czy_koszty_zwiekszone == "t":
    koszty_uzyskania_przychodu = 300
elif czy_koszty_zwiekszone == "n":
    koszty_uzyskania_przychodu = 250
else:
    print("Błąd kosztów uzyskania przychodu")

czy_ulga_podatkowa = input("""
Czy przysługuje Ci ulga podatkowa?
t = tak
n = nie
""")

if czy_ulga_podatkowa == "t":
    ulga_podatkowa = 300
elif czy_ulga_podatkowa == "n":
    ulga_podatkowa = 0
else:
    print("Błąd ulgi podatkowej")

dochod = round(podstawa_skladki_zdrowotnej - koszty_uzyskania_przychodu)
procent_podatku = 12 / 100
podatek = round((procent_podatku * dochod), 2)
zaliczka_na_podatek = round(podatek - ulga_podatkowa)


# obliczenie kwoty netto
netto = round((brutto - skladki - skladka_zdrowotna - zaliczka_na_podatek), 2)


# wydruk wyników
print(f"""
wynagrodzenie brutto: {brutto}

składka emerytalna: {skladka_emerytalna},
składka rentowa: {skladka_rentowa},
składka chorobowa: {skladka_chorobowa},
razem składki ZUS: {skladki}

podstawa składki zdrowotnej: {podstawa_skladki_zdrowotnej}
składka zdrowotna: {skladka_zdrowotna}

koszty uzyskania przychodu: {koszty_uzyskania_przychodu}
dochód: {dochod}
obliczony podatek: {podatek}
miesięczna ulga podatkowa: {ulga_podatkowa}
zaliczka na podatek: {zaliczka_na_podatek}

kwota netto: {netto}""")


# obliczenie zajęcia komorniczego
czy_komornik = input("""
Czy masz zajęcie komornicze?
t = tak
n = nie
""")

komornik_alimenty_procent = 60 / 100

if czy_koszty_zwiekszone == "t":
    kwota_wolna_od_potracen = 2715.48
elif czy_koszty_zwiekszone == "n":
    kwota_wolna_od_potracen = 2709.48

if czy_komornik == "t":
    czy_alimenty = input("""
Czy jest to potrącenie alimentacyjne?
t = tak
n = nie
""")
    if czy_alimenty == "t":
        komornik = round((komornik_alimenty_procent * netto), 2)
    else:
        komornik = netto - kwota_wolna_od_potracen
elif czy_komornik == "n":
    komornik = 0
else:
    print("Błąd potrącenia komorniczego")


# obliczenie ubezpiecznia
czy_ubezpieczenie_grupowe = input("""
Czy jesteś ubezpieczony w ubezpieczeniu grupowym u pracodawcy?
t = tak
n = nie
""")

if czy_ubezpieczenie_grupowe == "t":
    ubezpieczenie = float(input("Podaj kwotę miesięcznej składki (jako separatora dziesiętnego użyj kropki): "))
elif czy_ubezpieczenie_grupowe == "n":
    ubezpieczenie = 0
else:
    print("Błąd ubezpieczenia")


# obliczenie raty pożyczki
czy_pozyczka = input("""
Czy masz zaciągniętą pożyczkę u pracodawcy?
t = tak
n = nie
""")

if czy_pozyczka == "t":
    rata_pozyczki = float(input("Podaj kwotę miesięcznej raty (jako separatora dziesiętnego użyj kropki): "))
elif czy_pozyczka == "n":
    rata_pozyczki = 0
else:
    print("Błąd pożyczki")


# obliczenie innych potrąceń
czy_inne_potracenia = input("""
Czy masz jakieś inne potrącenia u pracodawcy?
t = tak
n = nie
""")

if czy_inne_potracenia == "t":
    inne_potracenia = float(
        input("Podaj kwotę jednomiesięcznego potrącenia (jako separatora dziesiętnego użyj kropki): "))
elif czy_inne_potracenia == "n":
    inne_potracenia = 0
else:
    print("Błąd innych potrąceń")


# obliczenie potrąceń
potracenia = round((ubezpieczenie + komornik + rata_pozyczki + inne_potracenia), 2)
przelew = round((netto - potracenia), 2)

print(f"""
netto: {netto}
potrącenia razem: {potracenia}
kwota przelewu na konto: {przelew}
""")