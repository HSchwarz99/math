import random

def updatePosition(n,m,pos,rnd):
  if rnd < 0.25:
    pos = (((pos // m) * m) + ((pos + 1) % m))
  elif rnd < 0.5:
    pos = (((pos // m) * m) + ((pos - 1) % m))
  elif rnd < 0.75:
    pos = ((pos % m) + ((((pos // m) + 1) % n) * m))
  elif rnd < 1:
    pos = ((pos % m) + ((((pos // m) - 1) % n) * m))
  return pos

def updatePositions(n, m, positions):
  for x in positions:
    r = random.random()
    x[1] = updatePosition(n, m, x[1], r)

def sortPositions(positions):
  positions.sort(key= lambda x: x[1])

def extractSquare(positions):
  l = []
  l.append(positions.pop())
  while positions and positions[-1][1] == l[0][1]:
    l.append(positions.pop())
  return l

def giftExchange(square):
  if ['ZH', square[0][1]] in square:
    for x in square:
      if x[0] == 'H':
        x[0] = 'HH'
  h = 0
  hh = 0
  z = 0
  for x in square:
    if x[0] == 'HH':
      h += 1
      hh += 1
    elif x[0] == 'H':
      h += 1
    elif x[0] == 'Z':
      z += 1
  # print(z, h, square)
  if z > 0 and h > 0:
    # print(z,h,hh)
    if z < (2 * hh):
      for x in square:
        if x[0] == 'Z':
          x[0] = 'ZH'
    elif z >= (2 * hh):
      for x in square:
        if x[0][0] == 'H':
          x[0] = 'Z'

def christmasFated(positions):
  a = True
  b = True
  c1 = 0
  c2 = 0
  for x in positions:
    if x[0] == 'Z':
      a = False
      c1 += 1
    elif x[0] == 'H' or x[0] == 'HH':
      b = False
      c2 += 1
  return a or b

def mergeSquare(square,intermediate):
  intermediate.extend(square)

def christmasFate(positions):
  a = True
  for x in positions:
    if x[0] == 'Z':
      a = False
  if a:
    return 'Ho, ho, ho, and a merry Zombie-Christmas!'
  return 'Zombies ate my Christmas!'

def zombieChristmas(n, m, positions):
  while not christmasFated(positions):
    updatePositions(n, m, positions)
    sortPositions(positions)
    l = []
    while positions:
      s = extractSquare(positions)
      giftExchange(s)
      mergeSquare(s, l)
    positions.extend(l)
  print(christmasFate(positions))

# n = 9
# while True:
#   l = []
#   for i in range(20):
#     s = random.sample(['Z', 'ZH', 'H'], 1)
#     l.append([s[0], random.randint(0, 110)])
#   zombieChristmas(n, n, l)

