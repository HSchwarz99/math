import random
import time

print(u"\u001b[2J")
print(u"\u001b[;H")
print("hi")
time.sleep(2)
def create_field(n):
  a = ["o"] * n
  f = []
  i = 0
  while i < n:
    f.append(a[:])
    i += 1
  starting_x = random.randint(0, n - 1)
  starting_y = random.randint(0, n - 1)
  f[starting_x][starting_y] = "F"
  ending_x = random.randint(0, n - 1)
  ending_y = random.randint(0, n - 1)
  while starting_x == ending_x and starting_y == ending_y:
    ending_x = random.randint(0, n - 1)
    ending_y = random.randint(0, n - 1)
  f[ending_x][ending_y] = "Z"
  return f

def find_field(l, string):
  first_index = 0
  second_index = 0
  for i, x in enumerate(l):
    if string in x:
      second_index = x.index(string)
      first_index = i
      return [first_index, second_index]

def move_random(field):
  n = len(field)
  p = find_field(field, "F")
  r = random.randint(0, 3)
  field[p[0]][p[1]] = o
  if r == 1:


def random_walk(n):
  field = create_field(n)
  z = find_field(f, "Z")
  print(field)
  # while f

f = create_field(3)
for c in f:
  print(c)
print(find_field(f, "F"))
