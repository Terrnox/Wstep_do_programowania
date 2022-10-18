zadanie = int(input("Podaj numer zadania (1-7):\n"))
print("\n")
match zadanie:

#1. Napisz program wyznaczania wartości funkcji określonych wzorami dla argumentów rzeczywistych podawanych przez użytkownika:
    case 1:
#a) a(x) 2x dla x>0, 0 dla x=0, -3x dla x<0

        def funkcja_a(x):
            if x>0:
                return 2*x
            elif x==0:
                return 0
            elif x<0:
                return -3*x

        x = float(input("Podaj argument funkcji a:\n"))
        wynik = funkcja_a(x)
        print("Wynik funkcji wynosi: "+str(wynik)+"\n")

#b) b(x) x^2 dla x>=1, x dla x<1

        def funkcja_b(x):
            if x>=1:
                return x**2
            elif x<1:
                return x

        x = float(input("Podaj argument funkcji b:\n"))
        wynik_b = funkcja_b(x)
        print("Wynik funkcji wynosi: "+str(wynik_b)+"\n")

#c) c(x) 2+x dla x>2, 8 dla x=2, x-4 dla x<2 

        def funkcja_c(x):
            if x>2:
                return 2+x
            elif x==2:
                return 8
            elif x<2:
                return x-4

        x = float(input("Podaj argument funkcji c:\n"))
        wynik_c = funkcja_c(x)
        print("Wynik funkcji wynosi: "+str(wynik_c)+"\n")

#2. Napisz program rozwiązywania równania liniowego ax + b = 0, gdzie a i b są współczynnikami podawanymi przez użytkownika.
    case 2:

        def rowlin(a,b):
            if(a!=0):
                return -b/a

        a = float(input("Podaj współczynik a funkcji liniowej:\n"))
        b = float(input("Podaj współczynik b funkcji liniowej:\n"))
        wynik_lin = rowlin(a,b)
        print("Miejsce zerowe funkcji wynosi: "+str(wynik_lin)+"\n")

#3. Napisz program rozwiązywania równania kwadratowego ax^2 + bx + c =, gdzie a, b i c są współczynnikami podawanymi przez użytkownika.
    case 3:
        import math as m

        def rowkwa(a,b,c):
            delta = b**2-4*a*c
            if delta > 0:
                x1 = (-b-m.sqrt(delta))/(2*a)
                x2 = (-b+m.sqrt(delta))/(2*a)
                t = [x1, x2]
                return t
            elif delta ==0:
                x1 = -b/(2*a)
                x2 = x1 #odbicie
                t = [x1, x2]
                return t
        '''    elif delta < 0: #dla zbioru liczb nierzeczywistych i = sqrt(-1)
                x1 = (-b-(m.sqrt(delta)))/(2*a)
                x2 = (-b+(m.sqrt(delta)))/(2*a)
                t = [x1, x2]
                return t
        '''
        a = float(input("Podaj współczynik a funkcji kwadratowej:\n"))
        b = float(input("Podaj współczynik b funkcji kwadratowej:\n"))
        c = float(input("Podaj współczynik c funkcji kwadratowej:\n"))
        wynik_kwa = rowkwa(a,b,c)
        print("Miejsca zerowe funkcji wynoszą:\n")
        for i in range (0,2):
            print(wynik_kwa[i])
    
#4. Napisz program porządkowania trzech liczb x, y i z. Od najmniejszej do największej, bez użycia wbudowanych funkcji.
    case 4:
        def sortuj(T,dl):
            k = 0
            pom = 0
            i = 0
            while i < dl - 1:
                k = i
                j = i + 1
                while j < dl:
                    if T[j] < T[k]:
                        k = j
                    j = j + 1
                pom = T[k]
                T[k] = T[i]
                T[i] = pom
                i += 1
            for it in range(0, dl):
                print(str(T[it]) + "\n")

        x = float(input("Wprowadź liczbę x:\n"))
        y = float(input("Wprowadź liczbę y:\n"))
        z = float(input("Wprowadź liczbę z:\n"))
        print("\n")
        T = [x,y,z]
        dl = len(T)
        print("Posortowana tablica:\n")
        sortuj(T,dl)

#5. Z wykorzystaniem operatorów logicznych not (negacja) oraz and (koniunkcja) napisz program, który w zależności od spełnienia pewnych warunków wyświetla odpowiednie komunikaty:
#• Jeśli pada deszcz i jest autobus na przystanku, to „Weź parasol”, „Dostaniesz się na uczelnie”;
#• Jeśli pada deszcz i nie ma autobusu, to „Nie dostaniesz się na uczelnię”;
#• Jeśli nie pada deszcz i jest autobus na przystanku, to „Dostaniesz się na uczelnie”, „Miłego dnia i pięknej pogody”.
# Użytkownik podaje informacje o tym czy pada i czy jest autobus.
    case 5:
        def logika(p,a):
            if p and a:
                print("Weź parasol, Dostaniesz się na uczelnie\n")
            elif p and not a:
                print("Nie dostaniesz się na uczelnię\n")
            elif not p and a:
                print("Dostaniesz się na uczelnie, Miłego dnia i pięknej pogody.\n")

        p = int(input("Czy pada deszcz? 1/0 \n"))
        a = int(input("Czy jest autobus? 1/0\n"))

        logika(p,a)

#6. Napisz program działający jak prosty kalkulator, który potrafi dodawać, odejmować, mnożyć, dzielić i obliczać resztę z dzielenia
    case 6:
        print("Wybierz działanie: (1-6)\n")
        print("1. Dodawanie\n")
        print("2. Odejmowanie\n")
        print("3. Mnożenie\n")
        print("4. Dzielenie\n")
        print("5. Reszta z dzielenia\n")
        print("6. Koniec\n")
        stan = int(input())
        print("\n")
        if stan==1:
            print("Wprowadź liczby\n")
            a = int(input("Wprowadź pierwszą liczbę:\n"))
            b = int(input("Wprowadź drugą liczbę:\n"))
            wynik = a + b
            print("Wynik dodawania wynosi:"+str(wynik))
        if stan==2:
            print("Wprowadź liczby\n")
            a = int(input("Wprowadź pierwszą liczbę:\n"))
            b = int(input("Wprowadź drugą liczbę:\n"))
            wynik = a - b
            print("Wynik odejmowania wynosi:"+str(wynik))
        if stan==3:
            print("Wprowadź liczby\n")
            a = int(input("Wprowadź pierwszą liczbę:\n"))
            b = int(input("Wprowadź drugą liczbę:\n"))
            wynik = a * b
            print("Wynik mnożenia wynosi:"+str(wynik))
        if stan==4:
            print("Wprowadź liczby\n")
            a = int(input("Wprowadź pierwszą liczbę:\n"))
            b = int(input("Wprowadź drugą liczbę:\n"))
            wynik = a / b
            print("Wynik dzielenia wynosi:"+str(wynik))
        if stan==5:
            print("Wprowadź liczby\n")
            a = int(input("Wprowadź pierwszą liczbę:\n"))
            b = int(input("Wprowadź drugą liczbę:\n"))
            wynik = a % b
            print("Reszta z dzielenia wynosi:"+str(wynik)+"\n")

#7. Napisz program (funkcję), który zamieni małą literę na dużą lub odwrotnie – dużą na małą
    case 7:
        def zamiana():
            zdanie = str(input("Podaj zdanie do konwesji:\n"))
            print("\n")
            typ_kon = int(input("Podaj typ konwersji (duża = 1, mała = 0):\n"))
            print("\n")
            if typ_kon == 0:
                zm_zdanie = zdanie.lower()
            if typ_kon == 1:
                zm_zdanie = zdanie.upper()
            print(str(zm_zdanie))

        zamiana()
    case other:
        print("Nie ma takiego zadania.\n")