def rownanie_kwadratowe(a, b, c):
    #Funkcja oblicza pierwiastki dla równania kwadratowego.
    #input: float, x^2
    #input: float, x
    #input: float, wyraz wolny
    #return: pierwiastki równania

    delta = b ** 2 - 4 * a * c
    if delta < 0:
        return "Brak rozwiązań rzeczywistych"
    elif delta == 0:
        x = -b / (2 * a)
        return x,
    else:
        x1 = (-b + delta ** 0.5) / (2 * a)
        x2 = (-b - delta ** 0.5) / (2 * a)
        return x1, x2

def oblicz_silnie(n):
    #Funkcja oblicza silnię dla podanej liczby.
    #input n: int, liczba do obliczenia silni
    #return: int, silnia liczby

    if n < 0:
        raise ValueError("Liczba musi być nieujemna")
    if n == 0 or n == 1:
        return 1
    wynik = 1
    for i in range(2, n + 1):
        wynik *= i
    return wynik
