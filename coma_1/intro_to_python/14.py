# 14. Listen

# Als naechstes ist es eure Aufgabe mehrere Funktionen
# zu schreiben, welche auch miteinander arbeiten sollen

# 1. LISTEN APPENDEN. Die Funktion Anhaengen(Liste,
# Objekt) soll an die Liste das Objekt anhaengen.
# Als Tipp Listen haben eine append Funktion.
# Also [1, 2, 3].append(4) haengt die 4 an die Liste an.

def Anhaengen(Liste, Objekt):
  # just using the built in append function
  Liste.append(Objekt)
  return Liste

# Test
print("Testing Anhaengen")

l = [1, 2, 3, 4]
o = "hallo"
print("-----------\nObjekt:")
print(o)
print("-----------\nListe:")
print(l)
print("-----------\nResult:")
print(Anhaengen(l, o))
print("-----------\n\n")

# 2. LISTEN MERGEN. Aufgabe ist es an eine Liste
# alle Elemente einer anderen Liste anzufuegen.
# Die Funktion sollte Zusammenfassen(Liste1, Liste2)
# heissen und eine Liste zurueckgeben

def Zusammenfassen(Liste1, Liste2):
  # just using the built in + operator for the two Lists
  return Liste1 + Liste2

# Test
print("Testing Zusammenfassen")

l1 = [1, 2, 3, 4]
l2 = [2, 3, 5, 6]
print("-----------\nListe1:")
print(l1)
print("-----------\nListe1:")
print(l2)
print("-----------\nResult:")
print(Zusammenfassen(l1, l2))
print("-----------\n\n")

# 3. LISTEN INTERSECT. Als letztes soll die Funktion
# Schnitt(Liste1, Liste2) heissen und eine Liste zurueckgeben.

def Schnitt(Liste1, Liste2):
  # making a set out of each List to only have unique values in each List
  # and using the & operator of sets to return the common elements
  return list(set(Liste1) & set(Liste2))

# Test

l1 = [1, 2, 3, 4]
l2 = [2, 3, 5, 6]
print("-----------\nListe1:")
print(l1)
print("-----------\nListe1:")
print(l2)
print("-----------\nResult:")
print(Schnitt(l1, l2))
print("-----------")

