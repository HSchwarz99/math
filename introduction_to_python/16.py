# 16. Inverser Ackermann

# Fuer die Aufgabe benoetigt ihr das math package,
# welches ihr mit import math importieren koennt.
# gegeben ist eine Zahl x, berechnet:
#   if x < 2, f(x) = 0
#   if x >= 2, f(x) = f(log2(int(x))) + 1
# findet ausserdem herraus, was die kleinste Zahl
# f(x) = 1 bzw. f(x) = 2, f(x) = 3, f(x) = 4.
# Ohne es mit dem Computer zu berechnen, was ist die kleinste
# Zahl f(x) = 5. falls ihr es doch versucht mit STR + C koennt
# koennt ihr eine Schleife abbrechen

import math

def inverse_ackermann(x):
  if x < 2:
    return 0
  return inverse_ackermann(math.log(int(x), 2)) + 1

def lower_limit(x):
  i = 0
  r = 0
  while r < x:
    i += 1
    r = inverse_ackermann(i)
  return i
# Test

print("Testing inverse Ackermann function for x = 0..20")

i = 0
while i <= 20:
  print(i)
  print(inverse_ackermann(i))
  print("-------------")
  i += 1

print("Testing function lower_limit for values 1..4")
l = [1,2,3,4]
for i in l:
  print(i)
  print(lower_limit(i))
  print("-------------")
