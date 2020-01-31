def parse_stupid_string(s):
  l = []
  for o in s.split(", "):
    ll = []
    for p in o.split(" "):
      ll.append(int(p))
    l.append(ll)
  return l

def multiply(a, b):
  a = parse_stupid_string(a)
  b = parse_stupid_string(b)
  m = len(a) # zeilen in a
  r = len(b) # spalten in a und zeilen in b
  n = len(b[0])
  lll = []
  for i in range(m):
    ll = []
    for k in range(n):
      l = []
      for m in range(r):
        l.append(a[i][m] + b[m][k])
      ll.append(str(min(l)))
    lll.append(" ".join(ll))
  return ", ".join(lll)

def power(a, c):
  aa = a
  for i in range(c - 1):
    aa = multiply(aa, a)
  return aa

# print(multiply('4 3, 1 7', '2 5 9, 8 6 1'))
# print(power('4 3, 1 7', 3))
