from math import sqrt, floor
# import time

def sieve(n):
  '''
  bekommt einen Integer als Argument, rechnet alle primezahlen von 2 bis n aus
  und returnt eine Liste mit allen diesen Primzahlen oder None wenn n < 2 ist
  '''
  if n < 2:
   return None
  l = list(range(n + 1)) # kreiert eine Liste mit allen Eintraegen 0..n
  i = 0 # unser index fuer die listenelemente, fuer die der index anfangs gleich
        # der Listeneintraege von l ist.
  limit = floor(sqrt(n)) # unsere obere Schranke der Divisoren userer Liste
  while i <= limit: # iteriert ueber alle i <= limit
    if not l[i]: # wenn der Wert von l[i] False ist geht es in die naechste
                 # iteration
      i += 1
      continue
    if i < 2: # Wenn i kleiner als 2 ist wird es auf False gesetzt
      l[i] = False
    else: # Wenn l[i] nicht False ist wird erst der groeste moegliche divisor
          # der i * eine Zahl aus der Liste die nicht False ist bestimmt
      k = n // i
      while not l[k]:
        k -= 1
      while k >= i: # der groeste Faktor von i mal einer reelen Zahl k wird
                    # um ein vielfaches von i zu eliminieren.
                    # dies  wird nur solange getann, solange k >= i ist.
        l[i * k] = False
        k -= 1
        while not l[k]: # der faktor k wird solange gesenkt, bis l[k] eine Zahl
                        # ist
          k -= 1
    i += 1
  return [x for x in l if x] # returned nur die nicht Falschen Elemente

def isprime(p):
  '''
  checked erst ob p < 2 dann None, wenn 2 oder 3 true, wenn durch zwei
  teilbar false, wenn p = 5,7 true
  alle Primzahlen > 3 befinden sich bei 6n +-1 also wird p nur fuer diese
  Zahlen auf teilbarkeit ueberprueft
  squrt(n)
  '''
  if p < 2:
    return None
  if p < 4:
    return True
  if p % 2 == 0 or p % 3 == 0:
    return False
  limit = floor(sqrt(p))
  d = 5
  while d <= limit:
    if (p % d == 0) or (p % (d + 2) == 0):
      return False
    d += 6
  return True

def factorization(l):
  '''
  checked fuer alle in dem Comment der function isprime beschriebenen zahlen
  ob diese factoren sind.
  wenn eine zahl teilbar is wird l durch diese zahl geteilt so lange sie durch
  diese Zahl teilbar ist.
  '''
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
  '''
  ergibt sich aus den Gleichungen, welche der Aufagebe beiliegen
  '''
  if l < 1:
    return None
  p = 1
  f = factorization(l)
  if f:
    for i in f:
      p *= (i[1] + 1)
  return p

def iscoprime(n,m):
  '''
  ergibt sich aus der Gleichung mit der wir das machen sollten.
  '''
  if (n < 1) or (m < 1):
    return None
  return divisornumber(n * m) == (divisornumber(n) * divisornumber(m))



# def sieve2(n):
#   # selbsterklaerend wenn der Algorithmus klar ist
#   # O(log(log(n)))
#   if n < 2:
#     return None
#   p = list(range(2, n +1))
#   i = 0
#   limit = floor(sqrt(p[-1]))
#   while limit >= p[i]:
#     k = len(p) - 1
#     while k > i:
#       if p[k] % p[i] == 0:
#         p.pop(k)
#       k -= 1
#     i += 1
#   return p

# def sieve2(n):
#   if n < 2:
#    return None
#   l = list(range(2, n + 1))
#   for i in range(n + 1):
#     if i < 2 or not l[i - 2]:
#       continue
#     j = l[i - 2] * 2
#     while j < n + 1:
#       l[j - 2] = False
#       j += l[i - 2]
#   return [x for x in l if x != False]

# times = []
# for i in list(range(1, 1_000_000))[::1_000]:
  # a = time.time()
  # sieve(i)
  # b = time.time()
  # sieve2(i)
  # c = time.time()
  # print(i, '1:', b - a, '2:', c - b)
  # times.append((c-b)/(b-a))
# v = 0
# for t in times:
#   print(t)
#   v += t
# print(v/len(times))
# i = 100_000_000
# a = time.time()
# sieve(i)
# b = time.time()
# sieve2(i)
# c = time.time()
# print(i, '1:', b - a, '2:', c - b)

# times = []
# for i in list(range(1_000, 1_000_000))[::10_000]:
#   t = []
#   for k in list(range(i, i + 1_000))[::100]:
#     a = time.time()
#     sieve(i)
#     b = time.time()
#     sieve2(i)
#     c = time.time()

#     t.append((c-b)/(b-a))
#   v = 0
#   for x in t:
#     v += x
#   times.append(v/len(t))
# print(times)
# for i in range(1, 100):
#   print(i * 1_000, times[i - 1])

# print(sieve(100_000_000))
