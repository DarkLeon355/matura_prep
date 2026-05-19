'''
Matura Übungsaufgabe_016 (4 Punkte)

Schreiben Sie eine Python Klasse, welche ein Fahrzeug beschreibt!
Die Klasse Fahrzeug soll folgende Attribute haben:
# Marke
# Name
# Fuehrerscheintyp
# PS
# Listenpreis
PS und Listenpreis sollen optionale Parameter in der init-Methode sein. Wenn sie beim Erzeugen 
des Objekts nicht übergeben werden, sollen sie einen default Wert von 0 haben! Implementieren Sie 
eine Methode 'cruise()' welche abhängig von den PS unterschiedliche print-statements liefert. z.B.:
PS - 0-9 -> Ausgabe: "slowly slowly!"
PS 10-99 -> Ausgabe: "come on..."
PS >=100 -> Ausgabe: "let's go:-)"
Implementieren Sie auch eine __str__(self) Methode, welche die String Repräsentation eines
Objekts darstellt. Alle Attribute sollen in einer Formatierung Ihrer Wahl dargestellt
werden.
Erstellen Sie dann ein paar Fahrzeug Objekte (mindestens drei mit unterschiedlichen PS)
Speichern Sie diese in einer Liste. Iterieren Sie über die Liste und rufen Sie jeweils
die cruise() Methode auf. Nutzen Sie weiters die print() Funktion um die Werte der Objekte
auszugeben.
Achtung: Alle Texte innerhalb des Programms sollen in Englisch sein!

Ausführungsbeispiel:
Audi, R8, B, power 300, price: 3,000,000EUR.
let's go:-)
Mistral, Citybike, NONE, power 9, price: 200EUR.
slowly slowly!
Triumph, 3R, A, power 90, price: 10,000EUR.
come on...

Erreichbare Punkte: 4
Aufteilung der Punkte:
1 Punkt für die Definition der Klasse inklusive 'Konstruktor'
1 Punkt für die korrekte Implementierung der __str__() und cruise() Methoden
1 Punkt für die Erstellung und Speicherung der Objekte
1 Punkt für die korrekte Darstellung der Objekte und der Methodenaufrufe
'''
