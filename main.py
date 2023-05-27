def start():
    print("""
    *** KALKULATOR WYNAGRODZENIA NETTO DO UMOWY O PRACĘ W 2023 ROKU ***
""")


def pobranie_brutto():
    wartosc_brutto = input("    Podaj wynagrodzenie brutto: ")

    while wartosc_brutto.isalpha() == True or float(wartosc_brutto) <= 0:
        print("     Błąd! Podaj dodatnią wartość liczbową.")
        wartosc_brutto = input("    Podaj wynagrodzenie brutto: ")

    return float(wartosc_brutto)


def obliczenie_skladki(procent, podstawa):
    return round((procent * podstawa), 2)


def obliczenie_kosztow_uzyskania_przychodu():
    czy_koszty_zwiekszone = input("""
    Czy Twój zakład pracy znajduje się poza miejscowością, w której mieszkasz?
    t = tak
    n = nie
    """)

    while czy_koszty_zwiekszone.lower() not in ("t", "n"):
        print("    Wybrano nieistniejącą opcję.")
        czy_koszty_zwiekszone = input("    Wprowadź t lub n: ")

    if czy_koszty_zwiekszone.lower() == "t":
        return 300
    elif czy_koszty_zwiekszone.lower() == "n":
        return 250


def obliczenie_ulgi_podatkowej():
    czy_ulga_podatkowa = input("""
    Czy przysługuje Ci ulga podatkowa?
    t = tak
    n = nie
    """)

    while czy_ulga_podatkowa.lower() not in ("t", "n"):
        print("    Wybrano nieistniejącą opcję.")
        czy_ulga_podatkowa = input("    Wprowadź t lub n: ")

    if czy_ulga_podatkowa.lower() == "t":
        return 300
    elif czy_ulga_podatkowa.lower() == "n":
        return 0


def obliczenie_komornika():
    czy_komornik = input("""
    Czy masz zajęcie komornicze?
    t = tak
    n = nie
    """)

    while czy_komornik.lower() not in ("t", "n"):
        print("    Wybrano nieistniejącą opcję.")
        czy_komornik = input("    Wprowadź t lub n: ")

    if czy_komornik.lower() == "t":
        czy_alimenty = input("""
    Czy jest to potrącenie alimentacyjne?
    t = tak
    n = nie
    """)
        while czy_alimenty.lower() not in ("t", "n"):
            print("    Wybrano nieistniejącą opcję.")
            czy_alimenty = input("    Wprowadź t lub n: ")

        if czy_alimenty.lower() == "t":
            komornik_alimenty_procent = 60 / 100
            return round((komornik_alimenty_procent * netto), 2)
        else:
            if koszty_uzyskania_przychodu == 300:
                kwota_wolna_od_potracen = 2715.48
                return netto - kwota_wolna_od_potracen
            elif koszty_uzyskania_przychodu == 250:
                kwota_wolna_od_potracen = 2709.48
                return netto - kwota_wolna_od_potracen

    elif czy_komornik.lower() == "n":
        return 0


def obliczenie_ubezpiecznia():
    czy_ubezpieczenie_grupowe = input("""
    Czy jesteś ubezpieczony w ubezpieczeniu grupowym u pracodawcy?
    t = tak
    n = nie
    """)

    while czy_ubezpieczenie_grupowe.lower() not in ("t", "n"):
        print("    Wybrano nieistniejącą opcję.")
        czy_ubezpieczenie_grupowe = input("    Wprowadź t lub n: ")

    if czy_ubezpieczenie_grupowe.lower() == "t":
        kwota_ubezpieczenia = input("    Podaj kwotę miesięcznej składki (jako separatora dziesiętnego użyj kropki): ")

        while kwota_ubezpieczenia.isalpha() == True or float(kwota_ubezpieczenia) <= 0:
            print("    Błąd!")
            kwota_ubezpieczenia = input("    Podaj dodatnią wartość liczbową: ")

        return float(kwota_ubezpieczenia)

    elif czy_ubezpieczenie_grupowe.lower() == "n":
        return 0


def obliczenie_raty_pozyczki():
    czy_pozyczka = input("""
    Czy masz zaciągniętą pożyczkę u pracodawcy?
    t = tak
    n = nie
    """)

    while czy_pozyczka.lower() not in ("t", "n"):
        print("    Wybrano nieistniejącą opcję.")
        czy_pozyczka = input("    Wprowadź t lub n: ")

    if czy_pozyczka.lower() == "t":
        rata = input("    Podaj kwotę miesięcznej raty (jako separatora dziesiętnego użyj kropki): ")

        while rata.isalpha() == True or float(rata) <= 0:
            print("    Błąd!")
            rata = input("    Podaj dodatnią wartość liczbową: ")

        return float(rata)

    elif czy_pozyczka.lower() == "n":
        return 0


def obliczenie_innych_potracen():
    czy_inne_potracenia = input("""
    Czy masz jakieś inne potrącenia u pracodawcy?
    t = tak
    n = nie
    """)

    while czy_inne_potracenia.lower() not in ("t", "n"):
        print("    Wybrano nieistniejącą opcję.")
        czy_inne_potracenia = input("    Wprowadź t lub n: ")

    if czy_inne_potracenia.lower() == "t":
        inne = input("    Podaj kwotę jednomiesięcznego potrącenia (jako separatora dziesiętnego użyj kropki): ")

        while inne.isalpha() == True or float(inne) <= 0:
            print("    Błąd!")
            inne = input("    Podaj dodatnią wartość liczbową: ")

        return float(inne)

    elif czy_inne_potracenia.lower() == "n":
        return 0


# uruchomienie programu
start()
brutto = pobranie_brutto()

# procent składek
skladka_emerytalna_procent = 9.76 / 100
skladka_rentowa_procent = 1.5 / 100
skladka_chorobowa_procent = 2.45 / 100
skladka_zdrowotna_procent = 9 / 100

# obliczenie składek
skladka_emerytalna = obliczenie_skladki(skladka_emerytalna_procent, brutto)
skladka_rentowa = obliczenie_skladki(skladka_rentowa_procent, brutto)
skladka_chorobowa = obliczenie_skladki(skladka_chorobowa_procent, brutto)
skladki = round((skladka_emerytalna + skladka_rentowa + skladka_chorobowa), 2)
skladka_zdrowotna = obliczenie_skladki(skladka_zdrowotna_procent, (brutto - skladki))

# obliczenie dochodu
koszty_uzyskania_przychodu = obliczenie_kosztow_uzyskania_przychodu()
dochod = round(brutto - skladki - koszty_uzyskania_przychodu)

# obliczenie podatku
procent_podatku = 12 / 100
podatek = round((procent_podatku * dochod), 2)
ulga_podatkowa = obliczenie_ulgi_podatkowej()
zaliczka_na_podatek = round(podatek - ulga_podatkowa)

# obliczenie kwoty netto
netto = round((brutto - skladki - skladka_zdrowotna - zaliczka_na_podatek), 2)

# obliczenie potrąceń
komornik = obliczenie_komornika()
ubezpieczenie = obliczenie_ubezpiecznia()
rata_pozyczki = obliczenie_raty_pozyczki()
inne_potracenia = obliczenie_innych_potracen()
potracenia = round((komornik + ubezpieczenie + rata_pozyczki + inne_potracenia), 2)

# obliczenie przelewu na konto
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
wyjscie = input("    Wciśnij Enter, aby wyjść z programu.")
