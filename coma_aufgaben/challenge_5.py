from math import sqrt, floor

def sieve(n):
  # selbsterklaerend wenn der Algorithmus klar ist
  if n < 2:
    return None
  p = list(range(2, n +1))
  i = 0
  limit = floor(sqrt(p[-1]))
  while limit >= p[i]:
    k = len(p) - 1
    while k > i:
      if p[k] % p[i] == 0:
        p.pop(k)
      k -= 1
    i += 1
  return p

def isprime(p):
  # checkes erst ob p < 2 dann None, wenn 2 oder drei true, wenn durch zwei
  # teilbar false, wenn p = 5,7 true
  # alle Primzahlen > 3 befinden sich bei 6n +-1 also wird p nur fuer diese
  # Zahlen auf teilbarkeit ueberprueft
  if p < 2:
    return None
  if p < 4:
    return True
  if p % 2 == 0:
    return False
  limit = floor(sqrt(p))
  d = 5
  while d <= limit:
    if (p % d == 0) or (p % (d + 2) == 0):
      return False
    d += 6
  return True

def factorization(l):
  # checked fuer alle in dem Comment der function isprime beschriebenen zahlen
  # ob diese factoren sind.
  # wenn eine zahl teilbar is wird l durch diese zahl geteilt so lange sie durch
  # diese Zahl teilbar ist.
  if l < 2:
    return None
  pf = []
  d = 2
  while l > 1:
    for i in range(2):
      p = [d + (i *2), 0]
      while l % (d + (i * 2)) == 0:
        l = l / (d + (i * 2))
        p[1] += 1
      if p[1] != 0:
        pf.append(p)
    if d > 4:
      d += 6
    else:
      d += 1
  return pf

def divisornumber(l):
  # ergibt sich aus den Gleichungen, welche der Aufagebe beiliegen
  if l < 1:
    return None
  p = 1
  f = factorization(l)
  if f:
    for i in f:
      p *= (i[1] + 1)
  return p

def iscoprime(n,m):
  # ergibt sich aus der Gleichung mit der wir das machen sollten.
  if (n < 1) or (m < 1):
    return None
  return divisornumber(n * m) == (divisornumber(n) * divisornumber(m))


