a = 2
b = 3
c = a + b
print(c)  # Gibt 5 aus

def c():
    return a * b

a = 2
b = 3
ergebnis = c()  # Jetzt ist c() ein gültiger Funktionsaufruf
print(ergebnis)  # Gibt 5 aus

a = 90
b = 3
c = a * b
c  # Die Zahl wird automatisch angezeigt
print(c) 

# 1. List Comprehension (Listen-Verständnis)
# Erstellt eine neue Liste durch Transformation einer bestehenden Liste
zahlen = [1, 2, 3, 4, 5]
quadrate = [x**2 for x in zahlen]  # Ergebnis: [1, 4, 9, 16, 25]
# Rechenbeispiel: Preise mit 19% Mehrwertsteuer
preise = [10, 20, 30, 40, 50]
preise_mit_mwst = [preis * 1.19 for preis in preise]  # [11.9, 23.8, 35.7, 47.6, 59.5]

# 2. Dictionary Comprehension (Wörterbuch-Verständnis)
# Erstellt ein Wörterbuch aus einer Liste von Werten
waren = ['Apfel', 'Banane', 'Orange']
warenpreise = {ware: len(ware) * 2 for ware in waren}  
# Ergebnis: {'Apfel': 10, 'Banane': 12, 'Orange': 12}
# Rechenbeispiel: Quadratzahlen-Lookup
zahlen_quadrate = {x: x**2 for x in range(1, 6)}  
# Ergebnis: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# 3. Lambda Funktionen (Anonyme Funktionen)
# Kurze, einzeilige Funktionen für einfache Operationen
zahlen = [1, 2, 3, 4, 5]
# Verdoppeln aller Zahlen
verdoppelt = list(map(lambda x: x * 2, zahlen))  # [2, 4, 6, 8, 10]
# Rechenbeispiel: Mehrwertsteuer berechnen
mwst_berechnung = lambda preis: preis * 0.19
preise = [100, 200, 300]
mwst_betraege = list(map(mwst_berechnung, preise))  # [19.0, 38.0, 57.0]

# 4. Dateiverwaltung mit Kontextmanager
# Sicheres Schreiben und Lesen von Dateien
# Rechenbeispiel: Zahlen in Datei schreiben und Summe berechnen
with open('zahlen.txt', 'w') as datei:
    for i in range(1, 6):
        datei.write(f'{i}\n')  # Schreibt Zahlen 1 bis 5

with open('zahlen.txt', 'r') as datei:
    summe = sum(int(zeile) for zeile in datei)  # Summe: 15

# 5. Exception Handling (Fehlerbehandlung)
# Sichere Durchführung von Berechnungen
def division_mit_fehlerbehandlung(a, b):
    try:
        ergebnis = a / b
        return f"Ergebnis: {ergebnis}"
    except ZeroDivisionError:
        return "Division durch Null nicht möglich!"
    except TypeError:
        return "Bitte nur Zahlen eingeben!"

# Rechenbeispiele:
print(division_mit_fehlerbehandlung(10, 2))    # Ergebnis: 5.0
print(division_mit_fehlerbehandlung(10, 0))    # Division durch Null nicht möglich!

# 6. Dekoratoren für Berechnungen
# Misst die Ausführungszeit von Berechnungen
import time

def zeitmessung(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        ergebnis = func(*args, **kwargs)
        ende = time.time()
        print(f"Berechnung dauerte {ende - start:.4f} Sekunden")
        return ergebnis
    return wrapper

@zeitmessung
def komplexe_berechnung(n):
    # Simuliert eine zeitaufwändige Berechnung
    return sum(i**2 for i in range(n))

# Rechenbeispiel:
ergebnis = komplexe_berechnung(1000000)  # Berechnet Summe der Quadratzahlen

# 7. Klassen für mathematische Operationen
class Taschenrechner:
    def __init__(self):
        self.verlauf = []
    
    def addiere(self, a, b):
        ergebnis = a + b
        self.verlauf.append(f"{a} + {b} = {ergebnis}")
        return ergebnis
    
    def multipliziere(self, a, b):
        ergebnis = a * b
        self.verlauf.append(f"{a} × {b} = {ergebnis}")
        return ergebnis

# Rechenbeispiel:
rechner = Taschenrechner()
print(rechner.addiere(5, 3))      # 8
print(rechner.multipliziere(4, 2)) # 8

# 8. Generator für mathematische Folgen
def fibonacci_generator(max_wert):
    """Erzeugt Fibonacci-Zahlen bis zum angegebenen Maximalwert"""
    a, b = 0, 1
    while a <= max_wert:
        yield a
        a, b = b, a + b

# Rechenbeispiel:
fib_zahlen = list(fibonacci_generator(100))
# Ergebnis: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# 9. f-Strings für Berechnungen und Formatierung
temperatur = 25.6789
luftfeuchtigkeit = 0.8234
print(f"Temperatur: {temperatur:.1f}°C")  # 25.7°C
print(f"Luftfeuchtigkeit: {luftfeuchtigkeit:.1%}")  # 82.3%

# 10. Type Hints mit Berechnungsbeispielen
from typing import List, Dict

def statistik(zahlen: List[float]) -> Dict[str, float]:
    """Berechnet statistische Kennzahlen für eine Liste von Zahlen"""
    return {
        "Summe": sum(zahlen),
        "Mittelwert": sum(zahlen) / len(zahlen),
        "Maximum": max(zahlen),
        "Minimum": min(zahlen)
    }

# Rechenbeispiel:
messwerte = [1.5, 2.7, 3.2, 4.8, 9.1]
stats = statistik(messwerte)
# Ergebnis: {'Summe': 17.3, 'Mittelwert': 3.46, 'Maximum': 5.1, 'Minimum': 1.5}