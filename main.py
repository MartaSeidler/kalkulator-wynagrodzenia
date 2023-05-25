def start():
    print("""
    *** KALKULATOR WYNAGRODZENIA NETTO DO UMOWY O PRACĘ W 2023 ROKU ***
""")


def pobranie_brutto():
    brutto = int(input("    Podaj wynagrodzenie brutto: "))
    return brutto


def obliczenie_skladki(procent, podstawa):
    return round((procent * podstawa), 2)


def obliczenie_kosztow_uzyskania_przychodu():

    czy_koszty_zwiekszone = input("""
    Czy Twój zakład pracy znajduje się poza miejscowością, w której mieszkasz?
    t = tak
    n = nie
    """)

    if czy_koszty_zwiekszone == "t":
        return 300
    elif czy_koszty_zwiekszone == "n":
        return 250
    else:
        return print("Błąd kosztów uzyskania przychodu")


def obliczenie_ulgi_podatkowej():
    czy_ulga_podatkowa = input("""
    Czy przysługuje Ci ulga podatkowa?
    t = tak
    n = nie
    """)

    if czy_ulga_podatkowa == "t":
        return 300
    elif czy_ulga_podatkowa == "n":
        return 0
    else:
        return print("Błąd ulgi podatkowej")


def obliczenie_komornika(koszty_uzyskania_przychodu):

    czy_komornik = input("""
    Czy masz zajęcie komornicze?
    t = tak
    n = nie
    """)

    if czy_komornik == "t":
        czy_alimenty = input("""
    Czy jest to potrącenie alimentacyjne?
    t = tak
    n = nie
    """)
        if czy_alimenty == "t":
            komornik_alimenty_procent = 60 / 100
            return round((komornik_alimenty_procent * netto), 2)
        else:
            if koszty_uzyskania_przychodu == 300:
                kwota_wolna_od_potracen = 2715.48
            elif koszty_uzyskania_przychodu == 250:
                kwota_wolna_od_potracen = 2709.48
            return netto - kwota_wolna_od_potracen
    elif czy_komornik == "n":
        return 0
    else:
        return print("Błąd potrącenia komorniczego")


def obliczenie_ubezpiecznia():
    czy_ubezpieczenie_grupowe = input("""
    Czy jesteś ubezpieczony w ubezpieczeniu grupowym u pracodawcy?
    t = tak
    n = nie
    """)

    if czy_ubezpieczenie_grupowe == "t":
        return float(input("    Podaj kwotę miesięcznej składki (jako separatora dziesiętnego użyj kropki): "))
    elif czy_ubezpieczenie_grupowe == "n":
        return 0
    else:
        return print("Błąd ubezpieczenia")


def obliczenie_raty_pozyczki():
    czy_pozyczka = input("""
    Czy masz zaciągniętą pożyczkę u pracodawcy?
    t = tak
    n = nie
    """)

    if czy_pozyczka == "t":
        return float(input("    Podaj kwotę miesięcznej raty (jako separatora dziesiętnego użyj kropki): "))
    elif czy_pozyczka == "n":
        return 0
    else:
        return print("Błąd pożyczki")


def obliczenie_innych_potracen():
    czy_inne_potracenia = input("""
    Czy masz jakieś inne potrącenia u pracodawcy?
    t = tak
    n = nie
    """)

    if czy_inne_potracenia == "t":
        return float(
            input("    Podaj kwotę jednomiesięcznego potrącenia (jako separatora dziesiętnego użyj kropki): "))
    elif czy_inne_potracenia == "n":
        return 0
    else:
        return print("Błąd innych potrąceń")


skladka_emerytalna_procent = 9.76 / 100
skladka_rentowa_procent = 1.5 / 100
skladka_chorobowa_procent = 2.45 / 100
skladka_zdrowotna_procent = 9 / 100

start()
brutto = pobranie_brutto()

skladka_emerytalna = obliczenie_skladki(skladka_emerytalna_procent, brutto)
skladka_rentowa = obliczenie_skladki(skladka_rentowa_procent, brutto)
skladka_chorobowa = obliczenie_skladki(skladka_chorobowa_procent, brutto)
skladki = skladka_emerytalna + skladka_rentowa + skladka_chorobowa
skladka_zdrowotna = obliczenie_skladki(skladka_zdrowotna_procent, (brutto - skladki))

koszty_uzyskania_przychodu = obliczenie_kosztow_uzyskania_przychodu()
ulga_podatkowa = obliczenie_ulgi_podatkowej()

dochod = round(brutto - skladki - koszty_uzyskania_przychodu)
procent_podatku = 12 / 100
podatek = round((procent_podatku * dochod), 2)
zaliczka_na_podatek = round(podatek - ulga_podatkowa)


# obliczenie kwoty netto
netto = round((brutto - skladki - skladka_zdrowotna - zaliczka_na_podatek), 2)

# obliczenie potrąceń
komornik = obliczenie_komornika(koszty_uzyskania_przychodu)
ubezpieczenie = obliczenie_ubezpiecznia()
rata_pozyczki = obliczenie_raty_pozyczki()
inne_potracenia = obliczenie_innych_potracen()

potracenia = round((komornik + ubezpieczenie + rata_pozyczki + inne_potracenia), 2)
przelew = round((netto - potracenia), 2)

# wydruk wyników
print(f"""
            * * *
    
    wynagrodzenie brutto: {brutto}

    składka emerytalna: {skladka_emerytalna}
    składka rentowa: {skladka_rentowa}
    składka chorobowa: {skladka_chorobowa}
    razem składki ZUS: {skladki}

    podstawa składki zdrowotnej: {brutto - skladki}
    składka zdrowotna: {skladka_zdrowotna}

    koszty uzyskania przychodu: {koszty_uzyskania_przychodu}
    dochód: {dochod}
    obliczony podatek: {podatek}
    miesięczna ulga podatkowa: {ulga_podatkowa}
    zaliczka na podatek: {zaliczka_na_podatek}

    kwota netto: {netto}
      
    potrącenia razem: {potracenia}
    kwota przelewu na konto: {przelew}

            * * *
""")

# wyjście z programu
wyjscie = input("Wciśnij Enter, aby wyjść z programu.")
