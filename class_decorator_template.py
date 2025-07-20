import functools

# ===  UNIWERSALNY TEMPLATE – klasa jako dekorator funkcji lub klasy ===

class NazwaDekoratora:
    def __init__(self, obiekt):
        functools.update_wrapper(self, obiekt)  # Zachowaj __name__, __doc__ itd. functools.update_wrapper stosujemy tylko wtedy, gdy dekorujemy funkcje lub metody,
        # a zależy nam na zachowaniu ich metadanych (np. __name__, __doc__, __annotations__).

        self.obiekt = obiekt

    def __call__(self, *args, **kwargs):
        # Działanie przed
        print("Przed wywołaniem")

        wynik = self.obiekt(*args, **kwargs)

        # Działanie po
        print("Po wywołaniu")

        return wynik


# ===  __call__ – co to? ===

# __call__ to metoda specjalna w Pythonie, która pozwala wywołać obiekt jak funkcję.

class A:
    def __call__(self):
        print("Obiekt A został wywołany!")

a = A()
a()  # <-- Wywołuje a.__call__()


# === ✅ PRZYKŁAD 1 – dekorowanie funkcji ===

class Loguj:
    def __init__(self, funkcja):
        functools.update_wrapper(self, funkcja)
        self.funkcja = funkcja

    def __call__(self, *args, **kwargs):
        print(f"[LOG] Wywołanie funkcji: {self.funkcja.__name__}")
        return self.funkcja(*args, **kwargs)

@Loguj
def przywitaj(imie):
    """Funkcja witająca użytkownika"""
    print(f"Cześć, {imie}!")

przywitaj("Kuba")  # działa jak zwykła funkcja, ale z logiem


# === ✅ PRZYKŁAD 2 – dekorowanie klasy ===

class DodajOpis:
    def __init__(self, klasa):
        self.klasa = klasa  # przekazujemy dekorowaną klasę

    def __call__(self, *args, **kwargs):
        instancja = self.klasa(*args, **kwargs)
        instancja.opis = "Jestem udekorowany!"
        return instancja

@DodajOpis
class Produkt:
    def __init__(self):
        self.nazwa = "Jabłko"

p = Produkt()
print(p.nazwa)  # Jabłko
print(p.opis)   # Jestem udekorowany!
