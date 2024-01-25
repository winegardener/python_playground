
class WrapAroundZaehler:
    #Ein Zaehler der nach einem bestimmten Wert "WrapWert" wieder bei 0 beginnt
    def __init__(self, wrapvalue = 10):
        self.zaehler = 0
        self.wrap = wrapvalue

    def reset(self):
        self.zaehler = 0
    
    def set(self, wert):
        self.zaehler = wert
    
    def count(self):
        if self.zaehler >= self.wrap:
            self.zaehler = 0
        else:
            self.zaehler += 1
        return self.zaehler

# Beispiel für die Verwendung der Klasse
mein_zaehler = WrapAroundZaehler(100)
mein_50_zaehler = WrapAroundZaehler(50)
mein_normallo_zaehler = WrapAroundZaehler() #wenn nichts angegeben wird, wird der Standardwert 10 verwendet

print("Aktueller Stand:", mein_zaehler.count())  # Ausgabe: Aktueller Stand: 1
mein_zaehler.set(5)
print("Aktueller Stand nach Setzen auf 5:", mein_zaehler.count())  # Ausgabe: Aktueller Stand nach Setzen auf 5: 6
mein_zaehler.reset()
print("Aktueller Stand nach Zurücksetzen:", mein_zaehler.count())  # Ausgabe: Aktueller Stand nach Zurücksetzen: 1
mein_zaehler.set(98)
print("99 = ", mein_zaehler.count())
print("100 = ", mein_zaehler.count())
print("0 = ", mein_zaehler.count())
print("Mein 50er Zähler:")
mein_50_zaehler.set(48)
print(mein_50_zaehler.count())
print(mein_50_zaehler.count())
print(mein_50_zaehler.count())