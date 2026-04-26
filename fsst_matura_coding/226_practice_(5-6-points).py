'''
Name:

Übungsbeispiel für Matura 2025 Aufgabe_06 (5 Punkte)
Angabe:
Erstellen Sie ein Programm für eine Werkzeugverleih. 
Bereits implementiert ist die Klasse Tool, welche einen Werkzeug im Verleih
repräsentiert, welches ausgeliehen werden kann. 

Implementieren Sie folgende Klassen mit den angegebenen Eigenschaften unter Verwendung der Klasse Tool:
* MotorSaw:        Marke (brand), Typ (type), Seriennummer (id), Leistung (power)
                   Kettenlänge (length_of_saw)
* Shovel:          Marke (brand), Identifikationsnummer (id), Länge (length), maximales Gewicht (max_weight)
* DrillingMachine: Marke (brand), Seriennummer (id)
                   max. Drehzahl (max_drive), Futtergröße (chuck_size)

Vergessen Sie nicht, einen sinnvollen Konstruktor bei den Klassen zu erstellen und die 
Methode _get_attributes() zu überschreiben.

Die Klasse Tool darf nicht verändert werden!!!

Erzeugen Sie folgenden Objekte.
Objekte:
* MotorSaw: Husqvarna, 120 Mark II, AC1982364, 1.9, 35cm
* MotorSaw: STIHL, MS 170, XY098123, 1.6, 30cm
* Shovel: Cemo, SCH10, 130, 20
* Shovel: Nölle, SCH11, 140, 15
* DrillingMachine: Bosch, AB112233, 2800, 13
* DrillingMachine: Makita, CD556677, 3400, 10

Leihen Sie einige der Gegenstände aus (checkout()-Methode). Geben Sie zwei der ausgeliehenen Gegenstände wieder zurück (return_item()-Methode).
Speichern Sie alle Gegenstände in einer Liste. Iterieren Sie anschließend 
über die Liste und geben Sie die Objektinformation wie unten angegeben mittels print() aus. 
Achtung print() ruft im Hintergrund __str__() auf. Diese Methode ruft wiederum _get_attributes() auf.

Erwartetet Ausgabe:
AC1982364 has been borrowed.
SCH10 has been borrowed.
AB112233 has been borrowed.
CD556677 has been borrowed.
SCH10 been returned.

Husqvarna, 120 Mark II (AC1982364) borrowed
STIHL, MS 170 (XY098123) in stock
Cemo (SCH10) in stock
Nölle (SCH11) in stock
Bosch (AB112233, drive=2800, chuck=13) borrowed
Makita (CD556677, drive=3400, chuck=10) borrowed


Achtung: Alle Texte innerhalb des Programms sollen in Englisch sein!

Erreichbare Punkte: 5
Aufteilung der Punkte:  
1 Punkt für die Kettensäge-Klasse 
1 Punkt für die Schaufel-Klasse
1 Punkt für die Bohrmaschine-Klasse
1 Punkt für die Erstellung der Objekte
1 Punkt für die richtige Verwendung der _get_attributes() Methode
'''
# Base class for stock item - NICHT VERÄNDERN !!!!!!!!!
class Tool:
    def __init__(self, id, brand):
        self.__id = id
        self.__brand = brand
        self.__is_borrowed = False

    def checkout(self):
        if not self.__is_borrowed:
            self.__is_borrowed = True
            print(f"{self.__id} has been borrowed.")
        else:
            print(f"{self.__id} is already borrowed.")

    def return_item(self):
        if self.__is_borrowed:
            self.__is_borrowed = False
            print(f"{self.__id} has been returned.")
        else:
            print(f"{self.__id} has not been borrowed.")

    def _get_attributes(self):
        return f"{self.__id}"

    def __str__(self):
        if self.__is_borrowed:
            return f"{self.__brand} ({self._get_attributes()}) borrowed"
        else:
            return f"{self.__brand} ({self._get_attributes()}) in stock"

# Lösung bitte ab hier!

# MotorSaw: Marke (brand), Typ (type), Seriennummer (id), Leistung (power) Kettenlänge (length_of_saw)

class MotorSaw(Tool):
    def __init__(self, brand, type, id, power, length_of_saw):
        super().__init__(id, f"{brand}, {type}")
    
    def _get_attributes(self):
        return super()._get_attributes()

# Shovel: Marke (brand), Identifikationsnummer (id), Länge (length), maximales Gewicht (max_weight)

class Shovel(Tool):
    def __init__(self, brand, id, length, max_weight):
        super().__init__(id, brand)
        self.__is_borrowed = False

# DrillingMachine: Marke (brand), Seriennummer (id) max. Drehzahl (max_drive), Futtergröße (chuck_size)

class DrillingMachine(Tool):
    def __init__(self, brand, id, max_drive, chuck_size):
        super().__init__(f"{id}, drive={max_drive}, chuck={chuck_size}", brand)
        self.__is_borrowed = False

"""
Objekte:
* MotorSaw: Husqvarna, 120 Mark II, AC1982364, 1.9, 35cm
* MotorSaw: STIHL, MS 170, XY098123, 1.6, 30cm
* Shovel: Cemo, SCH10, 130, 20
* Shovel: Nölle, SCH11, 140, 15
* DrillingMachine: Bosch, AB112233, 2800, 13
* DrillingMachine: Makita, CD556677, 3400, 10

Erwartetet Ausgabe:
AC1982364 has been borrowed.
SCH10 has been borrowed.
AB112233 has been borrowed.
CD556677 has been borrowed.
SCH10 been returned.

Husqvarna, 120 Mark II (AC1982364) borrowed
STIHL, MS 170 (XY098123) in stock
Cemo (SCH10) in stock
Nölle (SCH11) in stock
Bosch (AB112233, drive=2800, chuck=13) borrowed
Makita (CD556677, drive=3400, chuck=10) borrowed
"""

if __name__ == "__main__":
    saw1 = MotorSaw("Husqvarna", "120 Mark II", "AC1982364",1.9, 35)
    saw2 = MotorSaw("STIHL", "MS 170", "XY098123", 1.6, 30 )
    shovel1 = Shovel("Cemo", "SCH10", 130, 20)
    shovel2 = Shovel("Nölle", "SCH11", 140, 15)
    drill1 = DrillingMachine("Bosch", "AB112233", 2800, 13)
    drill2= DrillingMachine("Makita", "CD556677", 3400, 10 )

    saw1.checkout()
    shovel1.checkout()
    drill1.checkout()
    drill2.checkout()
    shovel1.return_item()

    print(f"\n{saw1}")
    print(saw2)
    print(shovel1)
    print(shovel2)
    print(drill1)
    print(drill2)