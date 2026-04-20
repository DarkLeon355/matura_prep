'''
Matura Übungsaufgabe_001 (2 Punkte)

Angabe:
Schreiben Sie ein Python Commandline Programm, welches
den User um die Eingabe von zwei integer Zahlen bittet.

Mit den zwei eingegeben Zahlen soll dann eine Division durchgeführt werden.
Gib das Ergebnis in der Form "Zahl1 / Zahl2 = Erg" aus, wobei
das Ergebnis mit zwei Nachkommastellen angezeigt werden soll.

Achtung! Es soll nicht auf zwei Nachkommastellen gerundet werden,
nur im print-command so angezeigt werden! 
Tipp: f-Strings und Formatanweisungen im f-String
Achtung: Alle Texte innerhalb des Programms sollen in Englisch sein!

Für Hilfe zur Formatierung siehe "Format Specification Mini-Language" im
"string" (nicht "str"!) Kapitel der Python Doc.

Ausführungsbeispiel:

Please enter the first number ->7
Please enter the second number ->27
7 / 27 = 0.26

Erreichbare Punkte: 2
Aufteilung der Punkte:  
1 Punkt für prinzipielle Funktionalität 
1 Punkt für die korrekte Formatierung der Ausgabe.
'''

in1 = int(input("Please enter the first number ->"))
in2 = int(input("Please enter the second number ->"))

print(f"{(in1/in2):.2F}")
