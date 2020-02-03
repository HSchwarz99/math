def maxunimod(L):
  m = 1
  i = 1
  while i < len(L):
    a = 1
    while i < len(L) and L[i - 1] <= L[i]:
      a += 1
      i += 1
    while i < len(L) and L[i - 1] >= L[i]:
      a += 1
      i += 1
    if m < a:
      m = a
    while i != len(L) and i >= 0 and L[i - 1] == L[i - 2]:
      i -= 1
  return m
