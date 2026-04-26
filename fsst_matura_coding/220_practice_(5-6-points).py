'''
Matura Übungsaufgabe_020 (4 Punkte)

Angabe:
OOP-Beispiel: Schreiben Sie eine Python Klasse, welche ein Auto (Car) beschreibt!
Die Klasse soll folgende Attribute haben:
# Hersteller (manufacturer)
# Name (name)
# Leistung (power) in PS
# Verbrauch (fuel consumption) in l/100km
# Allrad (all wheel drive) (True/False)

Der Verbrauch und Allrad sollen optionale Parameter in der init-Methode sein.
Wenn sie beim Erzeugen des Objekts nicht übergeben werden, sollen sie einen default Wert von 10l/100km und False haben!

Implementieren Sie eine Methode 'drive' welche abhängig von der Leistung unterschiedliche print-statements ausgibt. z.B.:
 Leistung 0 - 50PS -> Ausgabe: "slowly, slowly!"
 Leistung 51 - 100PS -> Ausgabe: "Juhu, that is fun!"
 Leistung größer 100PS -> Ausgabe: "Too much power - I am scared :/"

Implementieren Sie auch eine __str__(self) Methode, welche die String Repräsentation eines Objekts darstellt. Alle Attribute sollen in einer Formatierung Ihrer Wahl dargestellt werden.

Erstellen Sie dann ein paar Auto Objekte (mindestens drei mit unterschiedlichen Leistungen)
Speichern Sie diese in einer Liste. Iterieren Sie über die Liste und rufen Sie jeweils die object.drive() Methode und die print(object) Funktion auf (welche ihrerseits die __str__(self) Methode aufruft um einen String zu erzeugen).
Achtung: Alle Texte innerhalb des Programms sollen in Englisch sein!

Ausführungsbeispiel:
Skoda, Fabia, 49 PS and 7 l/100km fuel consumption. All wheel drive = False
slowly, slowly!

BMW, X5, 120 PS and 10 l/100km fuel consumption. All wheel drive = True
Too much power - I am scared :/

Audi, A4, 75 PS and 10 l/100km fuel consumption. All wheel drive = False
Juhu, that is fun!


Erreichbare Punkte: 4
Aufteilung der Punkte:  
1 Punkt für die Definition der Klasse inklusive 'Konstruktor'
1 Punkt für die korrekte Implementierung der __str__ und fahren Methoden
1 Punkt für die Erstellung und Speicherung der Objekte
1 Punkt für die korrekte Darstellung der Objekte und des Methodenaufrufes
'''

class Car:
    def __init__(self, manufacturer, name, power, fuel_consumption = 10, awd = False):
        self.manufacturer = manufacturer
        self.name = name
        self.power = power
        self.fuel_consumption = fuel_consumption
        self.awd = awd

    def drive(self):
        if self.power <= 50:
            print("slowly, slowly!")
        elif self.power <= 100:
            print("Juhu, that is fun!")
        else:
            print("Too much power - I am scared :/")
    
    def __str__(self):
        return f"{self.manufacturer}, {self.name}, {self.power} PS and {self.fuel_consumption} l/100km fuel consumption. All wheel drive = {self.awd}"
    

car1 = Car("Skoda", "Fabia", 49)
car2 = Car("BMW", "X5", 120, 12, True)
car3 = Car("Opel", "Meriva", 90, 8, False)

garage = [car1, car2, car3]

for car in garage:
    print(car)
    car.drive()

        