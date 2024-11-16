def transpose_matrix(macierz):
    # Sprawdź, czy macierz jest wieloliniowa (pierwszy element to lista)
    if isinstance(macierz[0], list):
        return [[macierz[j][i] for j in range(len(macierz))] for i in range(len(macierz[0]))]
    else:
        # Dla macierzy jednoliniowej zamieniamy wiersz na kolumnę
        return [[macierz[i]] for i in range(len(macierz))]

def wypisanie(m):
    if isinstance(m[0], list):
        for row in m:
            print(row)
        print()
    else:
        print(m)
        print()

macierz1 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
wypisanie(macierz1)
wypisanie(transpose_matrix(macierz1))
macierz2 = [
    [1,2,3,4,5],
    [6,7,8,9,0]
]
wypisanie(macierz2)
wypisanie(transpose_matrix(macierz2))
macierz3 = [5,6,7,8]
wypisanie(macierz3)
wypisanie(transpose_matrix(macierz3))