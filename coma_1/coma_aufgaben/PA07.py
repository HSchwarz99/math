def parse_lab(dateiname):
  l = open(dateiname, 'r').read().split("\n")
  l = [x for x in l if len(x) > 0]
  ll = []
  for i in range(len(l)):
    for k in range(len(l[0])):
      if l[i][k] == "P":
        ll.append((i, k))
  return ll

def abstand(s, t, dateiname="labyrinth.dat"):
  if s == t:
    return 0
  lab = parse_lab(dateiname)
  q = [[s, 0]]
  lab.remove(s)
  while len(q) > 0:
    a = q.pop(0)
    for x in [(a[0][0] + 1, a[0][1]), (a[0][0] - 1, a[0][1]), (a[0][0], a[0][1] + 1), (a[0][0], a[0][1] - 1)]:
      if x == t:
        return a[1] + 1
      if x in lab:
        lab.remove(x)
        q.append([x, a[1] + 1])
  return -1
