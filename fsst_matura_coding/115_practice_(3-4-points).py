'''
Matura Übungsaufgabe_015 (4 Punkte)

Schreiben Sie eine Python Klasse, welche ein Tier beschreibt!
Die Klasse Tier soll folgende Attribute haben:
# Gattung
# Name
# Unterarten (Anzahl der Subspezies)
# Lebensdauer (in Jahren)
# Population (als ganze Zahl)
Lebensdauer und Population sollen optionale Parameter in der init-Methode sein. Wenn sie beim Erzeugen 
des Objekts nicht übergeben werden, sollen sie einen default Wert von 0 haben! Implementieren Sie 
eine Methode 'is_vulnerable()' welche abhängig von der Population unterschiedliche print-statements liefert. z.B.:
Population - 0-9 -> Ausgabe: "dead end:-("
Population - 10-9999 -> Ausgabe: "help me!"
Population - >=10000 -> Ausgabe: "fine, thanx:-)"
Implementieren Sie auch eine __str__(self) Methode, welche die String Repräsentation eines
Objekts darstellt. Alle Attribute sollen in einer Formatierung Ihrer Wahl dargestellt
werden.
Erstellen Sie dann ein paar Tier Objekte (mindestens drei mit unterschiedlichen Populationen)
Speichern Sie diese in einer Liste. Iterieren Sie über die Liste und rufen Sie jeweils
die is_vulnerable() Methode auf. Nutzen Sie weiters die print() Funktion, 
um die Ausgaben der Object zu tätigen.
Achtung: Alle Texte innerhalb des Programms sollen in Englisch sein!

Ausführungsbeispiel:
Saeugetier, Pferd, 122 known subspecies and 10000000 known species.
fine, thanx:-)
Reptilien, Galpagosechse, 3 known subspecies and 500 known species.
help me!
Unbekannt, Dinosaurier, 1000 known subspecies and 0 known species.
dead end:-(

Erreichbare Punkte: 4
Aufteilung der Punkte:
1 Punkt für die Definition der Klasse inklusive 'Konstruktor'
1 Punkt für die korrekte Implementierung der __str__() und is_vulnerable() Methoden
1 Punkt für die Erstellung und Speicherung der Objekte
1 Punkt für die korrekte Darstellung der Objekte und der Methodenaufrufe
'''
