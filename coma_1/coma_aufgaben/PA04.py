import time
import random

class KnotenKlassen(dict):
  # Klasse die das die Eigeschaften der dict Klasse erbt, aber anders als die
  # dict Klasse bei einem nicht bekannten key eine leere liste zurueck gibt
  def __missing__(self, key):
    return list()

def get_classes(n, E):
  # alle reflexiven Elemente auf Vn x Vn
  idk = []
  for i in range(n):
    idk.append((i,i))
  # mergen von knoten
  knoten = idk + E
  # Nachbarschaften von k = {0, ... , n - 1}
  # erstellen eines neuen Knoten objects
  k = KnotenKlassen()
  for x in knoten:
    # fuegt zur liste vom key x[0] ein den korespondierenden wert x[1] des
    # tupples x hinzu
    k[x[0]] = k[x[0]] + [x[1]]
  return list(k.values())

def are_equal(list1, list2):
  return set(list1) == set(list2)

def are_disjoint(list1, list2):
  return set(list1).isdisjoint(list2)

def get_eqclasses(n, E):
  l = get_classes(n, E)
  partitions = list()
  while len(l) >= 1:
    # nimmt immer das letzte Element packt es in die partitions liste und
    # loescht das element aus der Liste
    partitions.append(l[-1])
    l.pop(-1)
    i = len(l)
    while i >= 1:
      # testet alle elemente in der Liste auf gleichheit mit dem letzten El. der
      # partitions Liste und loescht sie fals sie gleich sind.
      # wenn die elemente nicht gleich sind, wird geprueft ob die Listen
      # disjunkt sind um zu testen ob es sich wirklich um eine Aequivalenz-
      # klassenrelation handelt.
      # wenn es sich um keine Aequivalenzklassenrelation handelt wird eine
      # leere Liste returnt
      # sonst wird die partitions liste returned.
      i -= 1
      if are_equal(l[i], partitions[-1]):
        l.pop(i)
      elif not (are_disjoint(l[i], partitions[-1])):
        return []
  return partitions

# for x in range(1000000)[100:-1:1000]:
#   l = []
#   for k in range(x):
#     l.append((random.randint(1, x - 1), random.randint(1, x - 1)))
#   s = time.time()
#   get_eqclasses(x, l)
#   e = time.time()
#   print(e - s, " secs for:", x)

# print(get_eqclasses(4,[(1,2),(2,1),(3,1),(1,3),(2,3),(3,2)]))
# print(get_eqclasses(4,[(1,2),(3,1),(1,3),(2,3),(3,2)]))
# print(get_eqclasses(4,[(1,2),(2,1),(2,3),(3,2)]))
# print(get_eqclasses(4,[(1,2),(2,1)]))


