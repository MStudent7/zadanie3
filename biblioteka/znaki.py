def liczenie_wspolglosek(tekst):
    #Funkcja liczy liczbę współgłosek w podanym tekście.
    #input: str - tekst do analizy
    #return: int - liczba współgłosek

    wspolgloski = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    licznik = sum(1 for znak in tekst if znak in wspolgloski)
    return licznik

def liczenie_samoglosek(tekst):
    #Funkcja liczy liczbę samogłosek w podanym tekście.
    #input: str, tekst do analizy
    #return: int, liczba samogłosek

    samogloski = "aeiouyAEIOUY"
    licznik = sum(1 for znak in tekst if znak in samogloski)
    return licznik

def wielkie_litery(tekst):
    #Funkcja zamienia tekst na wielkie litery.
    #input: str, tekst do przekształcenia
    #return: str, tekst w wielkich literach

    return tekst.upper()

def male_litery(tekst):
    #Funkcja zamienia tekst na małe litery.
    #input: str, tekst do przekształcenia
    #return: str, tekst w małych literach

    return tekst.lower()
