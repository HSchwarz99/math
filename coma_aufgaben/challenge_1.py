def roots(a_2, a_1, a_0, b_2, b_1, b_0):
  coef = []
  for x in range(4, -1,-1):
    new_c = 0
    for y in range(2, -1, -1):
      if x - y <= 2 and x - y >= 0:
        new_c += eval("a_%s * b_%s" %(y, x - y))
    coef.append(new_c)
  last_c = 1
  changes = 0
  for x in coef:
    if x * last_c < 0:
      changes += 1
      last_c = x
  if changes % 2 == 0:
    return("Das Polynom hat eine gerade Anzahl von positiven reellen Wurzeln.")
  return("Das Polynom hat eine ungerade Anzahl von positiven reellen Wurzeln.")

