"""
Matura Übungsaufgabe_004 (2 Punkte)
Angabe:
Schreiben Sie ein Python Commandline Programm, welches
dem User hilft ein beliebiges 1x1 zu berechnen.

Der User soll die Integer Zahl des gewünschte 1x1 eingeben und dann soll
das berechnete 1x1 angezeigt werden (Mutlipliziert von 1 bis 10).
Die Formatierung der Ausgabe im Ausführungsbeispiel ist optional, aber
einen der möglichen Punkte wert!

Ausführungsbeispiel:
Please enter base -> 5
				 5 *  1 =  5
                 5 *  2 = 10
				 5 *  3 = 15
				 5 *  4 = 20
				 5 *  5 = 25
				 5 *  6 = 30
				 5 *  7 = 35
				 5 *  8 = 40
				 5 *  9 = 45
				 5 * 10 = 50


Für Hilfe zur Formatierung siehe "Format Specification Mini-Language" im
"string" (nicht "str"!) Kapitel der Python Doc.

Erreichbare Punkte: 2
Aufteilung der Punkte:  
1 Punkt für prinzipielle Funktionalität 
1 Punkt für die korrekte Formatierung der Ausgabe.
"""

ui = int(input("Please enter base -> "))
for x in range(10):
    print(f"				 {ui} * {(x+1):>2} = {((x+1)*ui):>2}")

