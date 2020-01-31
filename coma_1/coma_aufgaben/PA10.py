def partition(L, lo, hi, pivotFunction):
  if hi - lo < 1:
    return
  p = pivotFunction(L, lo, hi)
  # putting pivot element to the first pos
  L[L.index(p)] = L[lo]
  L[lo] = p
  # sorting every Element before or after Pivotelement
  i = lo + 1
  while i <= hi:
    if L[i] < p:
      L[lo] = L[i]
      L[i] = L[lo + 1]
      L[lo + 1] = p
      lo += 1
    i += 1

# l = [2, 5, 3, 4]
# partition(l, 1, 3, 2)
# print(l)


def quicksort(L, pivotFunction, lo=0, hi=(-2)):
  if hi == (-2):
    hi = len(L) -1
  if hi -lo < 1:
    return
  p = pivotFunction(L, lo, hi)
  partition(L, lo, hi, pivotFunction)
  i = L.index(p)
  quicksort(L, pivotFunction, lo=lo, hi=i-1)
  quicksort(L, pivotFunction, lo=i+1, hi=hi)

# def p(L, hi, lo):
#   return L[lo]

# L = []
# # L=[48, 23, -11, -34, 47, -45, 24, -47, -33, 33, 41, -15, 13, 2, -23, 36, 28, 25, -16, 34, 37, 7, -17, -25, 22, -31, -46, 49, 17, 11, -36, -9, -43, 26, -39, 10, 38, -26, -42, -12, 14, -44, -41, 6, -28, 39, -4, -50, 15, 19, -18, -7, 16, -48, -40]; [33, -41, 14, -23, 37, 39, -12, 22, 23, -36, 47, 49, 11, -42, -18, -33, 19, -16, -48, -45, -9, -44, -17, 13, -11, 36, 10, -43, -47, -34, -26, 6, -7, 26, -40, -15, 17, -25, 15, -28, 28, -46, -31, -39, 25, -50, 7, 2, 24, 16, 48, 38, 34, -4, 41]
# quicksort(L, p)
# print(L)
