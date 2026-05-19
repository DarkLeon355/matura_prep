'''
Matura Übungsaufgabe_010 (3 Punkte)

Angabe:
Schreiben Sie ein Python Commandline Programm, welches
den User um die Eingabe eines beliebigen Satzes (ohne Satz- 
und Sonderzeichen) bittet.
Es soll dann ausgegeben werden aus wie vielen Wörtern er besteht und
im Anschluss daran sollen die Wörter in umgekehrter Reihenfolge
ausgegeben werden.

Vorgaben:
Die zwei Aufgaben sollen in eigenen Funktionen bearbeitet werden und
ihre Ergebnisse an das Hauptprogramm zurück geben.

Die Ausgabe der Ergebnisse soll mittels print Funktion in der Form:
"your string consists of #-words and backwards it looks like this:" erfolgen.
Achtung: Alle Texte innerhalb des Programms sollen in Englisch sein!

Ausführungsbeispiel:
Please enter a string containing multiple words ->roger the rabbit runs fast
Your string contains 5 words and backwards it looks like this:
 fast runs rabbit the roger
 
 Erreichbare Punkte: 3
Aufteilung der Punkte:  
1 Punkt für prinzipielle Funktionalität (User-Eingabe, Ermittlung
  von Wort- und Zeichenanzahl und Ausgabe)
1 Punkt für die Funktionsdefinitionen und -Aufruf (mit Übergabeparameter)
1 Punkt für den korrekten Rückgabewert
'''

def get_words(input):
    word_list = input.split(" ")
    return len(word_list), word_list

def words_backwards(lenght, words):
    counter = lenght - 1
    while counter >= 0:
        print(words[counter], end=" ")
        counter -= 1

sentence = str(input("Please enter a string containing multiple words ->"))
lenght, word_list = get_words(sentence)
print(f"Your string contains {lenght} words and backwards it looks like this:")
words_backwards(lenght, word_list)