'''
Matura Übungsaufgabe_012 (3 Punkte)
Angabe:
Schreiben Sie ein Python Commandline Programm, welches
den User um die Eingabe zweier ganzzahliger Zahlenlimits bittet.
Berechnen Sie ein bestimmte Menge an Zufallszahlen in diesem Bereich.
Die Anzahl der Zufallszahlen soll ebenfalls vom Benutzer eingegeben werden.
Schreiben Sie dann alle Zahlen durch , getrennt in eine Datei numbers.txt
je 3 Zahlen pro Zeile
keine Sortierung

Ausführungsbeispiel:
Please enter the lower limit -> 2
Please enter the upper limit -> 20
Please enter number of values -> 5
File content:
2,20,3
4,19
Achten Sie auf sauberes Schließen des file-streams!
Achtung: Alle Texte innerhalb des Programms sollen in Englisch sein!

Erreichbare Punkte: 3
Aufteilung der Punkte:
1 Punkt für prinzipielle Funktionalität (User-Eingabe, Schreiben der Zahlen ins File)
1 Punkt für die Formatierung innerhalb des Files
1 Punkt für das korrekte Schließen des File.
'''

import random as r

upper_limit = int(input("Please enter the upper limit -> "))
lower_limit = int(input("Please enter the lower limit -> "))
amount = int(input("Please enter number of values -> "))

file_name = "numbers.txt"

randoms = []

while len(randoms) < amount:
	randoms.append(r.randint(lower_limit, upper_limit))


counter = 0


f = open(file_name, "w")

for n in randoms:
	f.write(f"{n}")
	counter = counter + 1
	if counter % 3 == 0:
		f.write("\n")
	elif counter == len(randoms):
		break
	else:
		f.write(",")

