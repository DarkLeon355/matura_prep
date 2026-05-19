'''
Name:

Übungsbeispiel für Matura 2025 Aufgabe_04 (3 Punkte)
Angabe:
Schreiben Sie ein Python Commandline Programm, welches Zahlen (Gleitkomma- sowie Ganzzahlen)
aus der Datei 024_practice.txt liest. Es können beliebig viele Zahlen pro Zeile 
im File sein. Die erste Zahl ist durch einen Hashtag (#) von den anderen Zahlen getrennt.
Alle weiteren Zahlen innerhalb einer Zeile sind durch eine Welle (~) 
voneinander getrennt. Im File können beliebig viele Zeilen sein.
Pro Zeile ist die Differenz aus der ersten Zahl (getrennt durch #) und der Summe der 
weiteren Zahlen zu berechnen. Das Ergebnis der Summe ist 
pro Zeile auszugeben. Weiters soll die Gesamtsumme aller Ergebnisse berechnet
und am Ende ausgegeben werden. Die Zahlen sollen alle rechtsbündig und auf zwei Kommastelle gerundet
ausgegeben werden, damit das Komma bei allen Zahlen genau untereinander ist.

Ausführungsbeispiel:

File content:
123#4.5~5
15.4#7.1~3
9#10~11~12~13
32#14~15.3~0.23~1.12 

Ausgabe:
Difference line 1:   113.50
Difference line 2:     5.30
Difference line 3:   -37.00
Difference line 4:     1.35
Overall difference:   83.15


Achten Sie auf sauberes Schliessen des file-streams!

Achtung: Alle Texte innerhalb des Programms sollen in Englisch sein!

Erreichbare Punkte: 3
Aufteilung der Punkte:  
1 Punkt für das korrekte Arbeiten mit dem File (Öffnen, Schließen) 
1 Punkt für die richtige Berechnung der Summen
1 Punkt für die korrekte Formatierung bei der Ausgabe.
'''
# Lösung bitte ab hier!



with open('124_practice.txt', 'r') as f:

    content = f.readlines()
    diffs = []
    
    for text in content:
        diffrence_sum = 0
        text = text.strip('\n')
        text = text.split(sep='#')
        text[1] = text[1].split(sep='~')

        for i in text[1]:
            try:
                i = int(i)
            except:
                i = float(i)
        

            diffrence_sum += i
        
        try:
            diff = int(text[0]) - diffrence_sum
        except:
            diff = float(text[0]) - diffrence_sum
        
        diff = round(diff, 2)
        diffs.append(diff)

f.close()

#Print the results:
h = 0
while h < len(diffs):
    res = diffs[h]
    h += 1
    print(f"Difference line {h}:{res:10.2F}")

print(f"Overall difference:{sum(diffs):9.2F}")
    




