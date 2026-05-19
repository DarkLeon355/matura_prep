'''
Matura Übungsaufgabe_014 (3 Punkte)
Angabe:
Schreiben Sie ein Python Commandline Programm, welches
den User um die Eingabe zweier ganzzahliger Zahlenlimits bittet.
Zählen Sie in einer vom Benutzer gewählten Schrittweite nach oben und
schreiben Sie die Zahlen durch : getrennt in eine Datei test.csv
je 2 Zahlen pro Zeile, das obere Limit soll in jedem Fall in die Datei 
geschrieben werden. Bei einer ungeraden Anzahl an Zahlen, soll die 
letzte Zahl ohne Doppelpunkt in der letzten Zeile stehen.

Ausführungsbeispiel:
Please enter the lower limit ->0
Please enter the upper limit ->19
Please enter offset -> 3
File content:
0:3 
6:9
12:15
18:19

Achten Sie auf sauberes Schließen des file-streams!
Achtung: Alle Texte innerhalb des Programms sollen in Englisch sein!

Erreichbare Punkte: 3
Aufteilung der Punkte:
1 Punkt für prinzipielle Funktionalität (User-Eingabe, Schreiben der Zahlen ins File)
1 Punkt für die Formatierung innerhalb des Files
1 Punkt für das korrekte Schließen des File.
'''

lower = int(input("Please enter the lower limit ->"))
upper = int(input("Please enter the upper limit ->"))
offset = int(input("Please enter offset -> "))
numbers = []
counter = 1

with open("114.csv", "w", newline='') as csvfile:
    for i in range(lower, upper, offset):
        numbers.append(i)

    if not upper in numbers:
        numbers.append(upper)
    
    list_max_idx = len(numbers)-1
    counter = 0

    while counter <= list_max_idx:
        first = numbers[counter]
        counter += 1
        if counter > list_max_idx:
            string = f"{first}\n"
        else:
            second = numbers[counter]
            counter += 1
            string = f"{first}:{second}\n"
        csvfile.write(string)




        

