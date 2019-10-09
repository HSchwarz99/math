# 15. Anfangsbuchstaben

# Die Funktion soll Strings grob in Listen einteilen.
# Dabei soll der Anfangsbuchstabe entscheiden,
# in welcher Liste er eingeteilt wird. Zurueckgegeben
# soll eine Liste mit allen Listen werden.

def weird_sorted_lists(string_liste):
  first_letters = []
  output = []
  # creating a list of all the first letters
  for s in string_liste:
    # making all letters in the list lower case to have
    # not upper and lowercase in different lists
    first_letters.append(s[0].lower())
  # making the first_letter list a set to have no duplicates
  # and iterating over each of the letters
  for c in set(first_letters):
    # creating a temporary list for each letter to store
    # all corresponding words in
    l = []
    for s in string_liste:
      # appending all strings with the same first letter to the temporary list
      if s[0].lower() == c:
        l.append(s)
    # appending the temporary list to the output
    output.append(l)
  # returning the list with all the sub lists for each letter
  return output

# Test

print("Testing weird_sorted_lists\n----------")
l = "Die Funktion soll Strings grob in Listen einteilen. Dabei soll der \
Anfangsbuchstabe entscheiden, in welche Liste er eingeteilt wird. \
Zurueckgegeben soll eine Liste mit allen nicht Listen werden.".split(" ")
print("Before:\n----------")
print(l)
print("After:\n----------")
for sl in weird_sorted_lists(l):
  print(sl)
