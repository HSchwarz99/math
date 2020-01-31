def get_min(int_list):
  if len(int_list) == 0:
    return None
  m = int_list[0]
  for i in int_list[1:]:
    if m > i:
      m = i
  return m

def get_linedistance(points, line):
  s = 0
  for x in points:
    s += (((line[0] * x[0]) + line[1] - x[1]) ** 2)
  return s

def linear_regression(points, lines):
  ls = list()
  for l in lines:
    ls.append(get_linedistance(points, l))
  return get_min(ls)
