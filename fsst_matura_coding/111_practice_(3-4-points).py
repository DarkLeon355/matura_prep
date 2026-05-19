'''
Matura Übungsaufgabe_011 (3 Punkte)

Angabe:
Schreiben Sie ein Python Commandline Programm, welches
den User um die Eingabe eines File-Namens bittet.
Im File befinden sich integer Zahlen (jeweils 4 Zahlen pro Zeile durch
Leerzeichen getrennt und eine unbekannte Anzahl von Zeilen)

Sie sollen Ausgeben wie viele Zahlen sie gefunden habe und wie
die Summe aller Zahlen lautet.

Ausführungsbeispiel:
File content:
3 4 5 6
7 8 9 10
11 12 13 14
15 16 17 18

Please enter the name of the file -> file.txt
Found 16 numbers in the file. The sum of all numbers = 168

Achten Sie auf sauberes Schliessen des file-streams!
Achten Sie auf Absicherung von möglichen Fehlern z.B. falscher Filename.
Ausgabe, falls Datei nicht gelesen werden kann: File could not be opened.

Achtung: Alle Texte innerhalb des Programms sollen in Englisch sein!

Erreichbare Punkte: 3
Aufteilung der Punkte:  
1 Punkt für prinzipielle Funktionalität (User-Eingabe, öffnen des File, Berechnung) 
1 Punkt für die Absicherung der Usereingabe (z.B. falscher Filename)
1 Punkt für das korrekte Schliessen des File.
'''

total_len = 0
total_sum = 0



with open("111.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip("\n")
        line = line.split(" ")
        total_len += len(line)
        buffer_sum = 0
        for n in line:
            n = int(n)
            buffer_sum += n
        total_sum += buffer_sum
        
print(total_sum)
print(total_len)



