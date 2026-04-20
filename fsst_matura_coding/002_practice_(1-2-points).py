3'''
Matura Übungsaufgabe_002 (2 Punkte)

Angabe:
Schreiben Sie ein Python Commandline Programm, welches
dem User hilft das kleine "Einmal-Eins" (Malreihen) zu üben.

Der User soll die integer Zahl der Malreihe eingeben und dann sollen die
einzelnen Berechnungen in aufsteigender Reihenfolge (1-10) angezeigt werden.
Der User soll das Ergebnis der Berechnung eingeben. Im Hintergrund soll
mitgezählt werden, wie viele der Antworten richtig bzw. falsch waren.
Diese Werte sollen dem User am Ende der Übung angezeigt werden.

Die Formatierung der Ausgabe im Ausführungsbeispiel ist optional, aber
einen der möglichen Punkte wert!

Ausführungsbeispiel:
Please enter the starting number ->7
         7 *  1 = 7
         7 *  2 = 14
         7 *  3 = 20
         7 *  4 = 28
         7 *  5 = 35
         7 *  6 = 42
         7 *  7 = 48
         7 *  8 = 56
         7 *  9 = 63
         7 * 10 = 70
Well done, you got 8 right answers!

Für Hilfe zur Formatierung siehe "Format Specification Mini-Language" im
"string" (nicht "str"!) Kapitel der Python Doc.

Erreichbare Punkte: 2
Aufteilung der Punkte:  
1 Punkt für prinzipielle Funktionalität 
1 Punkt für die korrekte Formatierung der Ausgabe.
'''


correct = 0
x = 0
y = 0
inputs = []
results = []

u = int(input("Please enter the starting number ->"))

while x < 10:
	x = x + 1
	inputs.append(int(input(f"	{u} * {x:>2} = ")))
	results.append((u*x))



while y < len(inputs):
	if inputs[y] == results[y]:
		correct = correct + 1
	y = y+1	

print(f"Well done, you got {correct} right answers!")
