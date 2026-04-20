"""
Matura Übungsaufgabe_009 (3 Punkte)

Angabe:
Schreiben Sie ein Programm, welches den Durchschnitt von beliebig vielen 
Zahlen ermittelt und ausgibt.

Der User soll integer Zahlen eingeben können, oder mit der 
Eingabe "end" die Eingabe beenden können.
Weiters soll die Eingabe mittels try/except abgesichert sein. 
Wenn der User z.B. einen String wie "Wurstsemmel" anstelle
einer Zahl eingibt, soll er erneut aufgefordert werden die Zahl einzugeben. 
Die eingegebenen Zahlen sollen in einer Liste gespeichert werden.

Wenn die Eingabe abgeschlossen ist ("end"), soll der Durchschnitt 
der Zahlen ermittelt werden und mittels print() Funktion auf zwei
Stellen hinter dem Komma ausgegeben werden.

Achtung: Alle Texte innerhalb des Programms sollen in Englisch sein!

Ausführungsbeispiel:
Please enter the 1. number or 'end' to quit -> 4
Please enter the 2. number or 'end' to quit -> 5
Please enter the 3. number or 'end' to quit -> semmel
This was not a number, please try again!
Please enter the 3. number or 'end' to quit -> 7
Please enter the 4. number or 'end' to quit -> 12
Please enter the 5. number or 'end' to quit -> 3
Please enter the 6. number or 'end' to quit -> end
The average number is: 6.20


Erreichbare Punkte: 3
Aufteilung der Punkte:  
1 Punkt für prinzipielle Funktionalität (User-Eingabe, 
  Durchschnittsberechnung und -Ausgabe) 
1 Punkt für die Fehlerbehandlung der User-Eingabe 
1 Punkt für das korrekte Beenden der User-Eingabe
"""

import numpy as np

inputs = []
counter = 1

while True:
	try:
		u = input(f"Please enter the {counter}. number or 'end' to quit -> ")
		if u == "end":
			break
		else:
			inputs.append(int(u))
			counter = counter + 1
	except:
		print("This was not a number, please try again!")
		continue


print(f"{np.mean(inputs):.2F}")
