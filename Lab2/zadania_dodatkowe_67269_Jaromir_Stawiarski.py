#Zadanie 1. Wyznaczanie wartości liczby zapisanej w systemie pozycyjnym o podstawie 𝑝 ∈ {2, … ,10}. Wartość
#liczby – liczba zapisana w systemie dziesiętnym. Na wejściu podajemy liczbę jako string, na wyjściu – liczbę
#dziesiętną typu int.
nr_zadania = int(input("Podaj numer zadania:\n"))
match nr_zadania:
    case 1:
        def konwersja_1():
            liczba = str(input("Wprowadź wartość liczby:\n"))
            p = int(input("Podaj podstawę systemu:\n"))
            dl = len(liczba)
            nowa_liczba = 0
            i = 0
            j = dl - 1
            while i <= (dl - 1):
                nowa_liczba = nowa_liczba + int(liczba[j])*(p**i)
                i = i + 1
                j = j - 1

            print(f"Wartość przekonwertowanej liczby wynosi:\n{nowa_liczba}")

        konwersja_1()

#Zadanie 2. Wyznaczanie wartości liczby podanej w systemie pozycyjnym o podstawie 𝑝 ∈ {2, … ,10} przy użyciu
#algorytmu Horner’a. Na wejściu podajemy liczbę jako string, na wyjściu - liczbę dziesiętną typu int.

    case 2:
        def Horner():
            liczba = str(input("Podaj liczbę:\n"))
            p = int(input("Podaj podstawę systemu:\n"))

            dl = len(liczba)
            hor_liczba = int(liczba[0])
            i = 1
            while i <= (dl - 1):
                hor_liczba = hor_liczba * p + int(liczba[i])
                i = i + 1
            print(f"Wartość liczby po konwersji wynosi:\n{hor_liczba}\n")

        Horner()


#Zadanie 3. Wyznaczanie zapisu podanej liczby dziesiętnej w systemie pozycyjnym o podstawie 𝑝 ∈ {2, … ,10, 16}.
#Na wejściu podajemy liczbę całkowitą, na wyjściu - liczbę zapisaną jako string.
    case 3:
        def konwersja(p, liczba):
            l = liczba
            T = []
            if p == 2:
                while l!=0:
                    r = liczba % 2
                    l = liczba // 2
                    liczba = l
                    T.append(r)
            if p == 4:
                while l!=0:
                    r = liczba % 4
                    l = liczba // 4
                    liczba = l
                    T.append(r)
            if p == 8:
                while l!=0:
                    r = liczba % 8
                    l = liczba // 8
                    liczba = l
                    T.append(r)
            if p == 16:
                while l!=0:
                    r = liczba % 16
                    l = liczba // 16
                    liczba = l
                    if r >= 0 and r < 10:
                        T.append(r)
                    else:
                        match r:
                            case 10:
                                T.append('A')
                            case 11:
                                T.append('B')
                            case 12:
                                T.append('C')
                            case 13:
                                T.append('D')
                            case 14:
                                T.append('E')
                            case 15:
                                T.append('F')

            nT = T[::-1]
            return nT

        liczba = int(input("Podaj liczbę całkowitą:\n"))
        p = int(input("Podaj podstawę systemu:\n"))

        tab = konwersja(p,liczba)
        wart_liczby = ""
        dl = len(tab)
        for i in range (0,dl):
            wart_liczby = wart_liczby + str(tab[i])

        print(f"Wartość liczby wynosi:\n{wart_liczby}")
    case other:
        print("Nie ma takiego zadania\n")