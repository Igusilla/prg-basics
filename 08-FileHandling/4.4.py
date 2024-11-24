def wyswietl_linie_z_csv(sciezka_pliku, ilosc_linii=5):
    try:
        with open(sciezka_pliku, 'r') as plik:
            while True:
                linie = [next(plik, None) for _ in range(ilosc_linii)]
                if not any(linie):
                    print("Koniec pliku.")
                    break
                
                for linia in linie:
                    if linia:
                        print(linia.strip())
                input("Naciśnij klawisz Enter, aby zobaczyć kolejne linie...")
    except FileNotFoundError:
        print(f"Błąd: Plik '{sciezka_pliku}' nie został znaleziony.")
    except StopIteration:
        print("Koniec pliku.")

sciezka_pliku = 'it_company.csv'       
wyswietl_linie_z_csv(sciezka_pliku)