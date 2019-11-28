def maximum(a, b):
  if a >= b:
    return a
  return b

def minimum(a, b):
  if a<= b:
    return a
  return b

def convert_to_standard(a1, a2, b1, b2):
  return (minimum(a1, b1), minimum(a2, b2), maximum(b1, a1), maximum(a2, b2))

def intersects(h, a1, a2, b1, b2):
  if h < 0:
    return False
  r = convert_to_standard(a1, a2, b1, b2)
  if ((r[0] <= 6) and (r[2] >= 0) and (r[1] <= h) and (r[3] >= 0)):
    return True
  return False

def get_delta_x1(a1,b1):
  x1 = 6
  if minimum(a1, b1) > 0:
    x1 -= minimum(a1, b1)
  if maximum(a1, b1) < 6:
    x1 -= (6 - maximum(a1, b1))
  return x1

def get_delta_x2(h, a2, b2):
  x2 = h
  if maximum(a2, b2) < h:
    x2 -= (h - maximum(a2, b2))
  if minimum(a2, b2) > 0:
    x2 -= minimum(a2, b2)
  return x2

def get_lattice_point_number(h,a1,a2,b1,b2):
  if h < 0:
    return "Die Eingabe ist fehlerhaft."
  if intersects(h, a1, a2, b1, b2):
    s = (get_delta_x1(a1, b1) + 1) * (get_delta_x2(h, a2, b2) + 1)
    return ("Die Zahl der Gitterpunkte im resultierenden Rechteck betraegt %i." %(s))
  else:
    return "Der Schnitt der gegebenen Rechtecke ist leer."


# print(get_delta_x2(6, 2, 3))
# print(get_lattice_point_number(5,-2,5,0,9))
# print(get_lattice_point_number(5,-2,4,1,9))

# print(intersects(5, 1, 1, 4, 4))
# print(intersects(5, -1,-1,1,1))
# print(intersects(5, 1, 1, 8, 8))
# print(intersects(5, 6,5,7,7))
