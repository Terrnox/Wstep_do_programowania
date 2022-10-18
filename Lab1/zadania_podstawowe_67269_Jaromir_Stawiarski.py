import random

nr_zadania = int(input("Podaj numer zadania:\n"))

match nr_zadania:

#Zadanie 1 (1.py) Napisz skrypt, który pobiera długości boków prostokąta, a następnie oblicza jego pole i obwód oraz wyświetla wyniki na ekranie. (Wykorzystaj f-stringi do wyświetlenia wyników)
    case 1:

        def prostokat():
            a = float(input("Podaj bok a prostokąta:\n"))
            b = float(input("Podaj bok b prostokąta:\n"))
            obw = 2*a + 2*b
            P = a*b
            print(f"Obwód prostokąta wynosi {obw}, a jego pole jest równe {P}.\n")

        prostokat()

#Zadanie 2 (2.py) Napisz skrypt, który pobiera od użytkownika drogę pokonaną przez samochód oraz średnie spalanie (w litrach na 100 km) i wyświetli informację o przewidywanym zużyciu paliwa oraz o szacowanych kosztach podróży (cena paliwa 6.5 zł/l).(Zmodyfikuj skrypt tak, aby długość przejechanej drogi była generowana losowo (liczba całkowita z zakresu <1, 1000>).)
    case 2:
        def ben_auto():
        #    trasa = float(input("Podaj przejechaną trasę:\n")) # trasa podawana przez użytkownika
            trasa = random.randint(1,1000)
            spalanie = float(input("Podaj średnie spalanie na 100km:\n"))
            z_paliwo = spalanie*trasa/100
            jcena_paliwa = 6.5
            cena_paliwa = z_paliwo * jcena_paliwa
            print(f"Przewidywane zużycie paliwa to {z_paliwo},a cena tej podróży wyniesie {cena_paliwa} zł\n")

        ben_auto()

#Zadanie 3 (3.py):
#• Dla osób poniżej 4 roku życia wstęp jest bezpłatny.
#• Dla osób w wieku od 4 do 18 lat bilet kosztuje 10zł.
#• Dla osób powyżej 18 roku życia bilet kosztuje 20zł.
    case 3:
        def bilet():
            wiek = int(input("Podaj wiek klienta:\n"))
            if wiek < 4:
                print("Wstęp jest bezpłatny:\n")
            elif wiek >=4 and wiek <18:
                print("Cena biletu: 10 zł\n")
            else:
                print("Cena biletu: 20 zł:\n")

        bilet()
#Zadanie 4 (4.py) Napisz skrypt, który sprawdzi czy litera wprowadzona przez użytkownika jest duża czy mała.
    case 4:
        litera = str(input("Wprowadź literę:\n"))
        if litera.isupper():
            print("Duża litera\n")
        elif litera.islower():
            print("Mała litera\n")
#Zadanie 5(5.py) Napisz program działający jak prosty kalkulator, który potrafi dodawać, odejmować, mnożyć, dzielić oraz obliczać potęgę.
    case 5:
        print("Jaką operację chcesz wykonać:\n")
        print("1. Dodawanie\n")
        print("2. Odejmowanie\n")
        print("3. Mnożenie\n")
        print("4. Dzielenie\n")
        print("5. Potęgowanie\n")
        operacja = int(input())
        match operacja:
            case 1:
                print("Dodawanie:\n")
                a = float(input("Podaj pierwszą liczbę:\n"))
                b = float(input("Podaj drugą liczbę:\n"))
                wynik = a + b
                print("Wynik operacji wynosi: "+str(wynik)+"\n")
            case 2:
                print("Odejmowanie:\n")
                a = float(input("Podaj pierwszą liczbę:\n"))
                b = float(input("Podaj drugą liczbę:\n"))
                wynik = a - b
                print("Wynik operacji wynosi: " + str(wynik) + "\n")
            case 3:
                print("Mnożenie:\n")
                a = float(input("Podaj pierwszą liczbę:\n"))
                b = float(input("Podaj drugą liczbę:\n"))
                wynik = a * b
                print("Wynik operacji wynosi: " + str(wynik) + "\n")
            case 4:
                print("Dzielenie:\n")
                a = float(input("Podaj pierwszą liczbę:\n"))
                b = float(input("Podaj drugą liczbę:\n"))
                wynik = a / b
                print("Wynik operacji wynosi: " + str(wynik) + "\n")
            case 5:
                print("Potęgowanie:\n")
                a = float(input("Podaj pierwszą liczbę:\n"))
                b = float(input("Podaj drugą liczbę:\n"))
                wynik = a ** b
                print("Wynik operacji wynosi: " + str(wynik) + "\n")
            case other:
                print("Kalkulator nie posiada takiej opcji:\n")
    case other:
        print|("Nie ma takiego zadanie:\n")
