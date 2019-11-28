# 19. Generator Function

# Eure Aufgabe ist es, ein Programm generate.py zu schreiben,
# welches eine Funktion generate beinhalten soll,
# welche eine Kombination aus Zahlen und Operatoren als einen String ausgeben soll.
# Dabei soll die Anzahl an Zahlen von der Eingabe abhaengen.
# Die Zahlen sollen zufaellig sein und zwischen 0 und 9 liegen.
# Die Operatoren sollen zufaellig + oder - sein.
#   Tipp: Es gibt das Modul random, welches die Funktion randint hat.
# Beispiel Ausgabe:
#   generate(3) erzeugt den String "3+2-5"
import random

def generate(x):
  string = ""
  o = ["+", "-", "*"]
  while x > 1:
    operator = random.randint(0, 2)
    string += str(random.randint(0, 9)) + o[operator]
    x -= 1
  string += str(random.randint(0, 9))
  return string

# # Test

# print(generate(10))
