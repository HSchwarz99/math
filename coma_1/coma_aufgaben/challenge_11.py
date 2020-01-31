def LR_decomposition(M):
  M = [[int(x) for x in y.split(' ')] for y in M.split(', ')]
  FS = '' # Finaler String
  R = [] # liste der Rechenoperationen
  # erstellt R Matrix
  for i in range(0, len(M) - 1):
    for j in range(i + 1, len(M)):
      R.append(M[j][i] / M[i][i])
      for k in range(0, len(M)):
        M[j][k] = M[j][k] - (M[i][k] * R[-1])
  # fuegt eintraege fuer L in die Liste ein
  c = 0
  for i in range(0, len(M) - 1):
    for j in range(i + 1, len(M)):
      M[j][i] = R[c]
      c += 1
  return ", ".join([" ".join([ str(int(x)) for x in y]) for y in M ])



# def getMatrix(A):
#     a = A.split(", ")
#     A=[]
#     for i in a:
#         A.append(list(map(int, i.split(" "))))
#     return A

# def getString(A):
#     E=""
#     for i in A:
#         E+=" ".join(map(str, i)) + ", "
#     return E[0:-2]

# def addZeile(m, z2, z1):
#     i = 0
#     while i < len(z1):
#         z1[i] = z1[i] + m * z2[i]
#         i += 1

# def LR_decomposition1(M):
#     M = getMatrix(M)
#     L = []
#     j = 0
#     while j < len(M[0]):
#         i = j+1
#         while i < len(M):
#             L.append(int(M[i][j]/M[j][j]))
#             addZeile(int(-M[i][j]/M[j][j]), M[j], M[i])
#             i += 1
#         j += 1
#     p = 0
#     for i in range(0,len(M)):
#         for j in range(i+1,len(M)):
#             M[j][i] = L[p]
#             p += 1
#     #print("\nErgebnis:")
#     #show(M)
#     return(getString(M))

# def multiply(A,B):
#     E=[]
#     for i in range(0,len(A)):
#         c=[]
#         for j in range(0,len(B[0])):
#             m=0
#             for l in range(0,len(B)):
#                 m += A[i][l] * B[l][j]
#             c.append(m)
#         E.append(c)
#     return E

# # def make_L(n):


# # print((LR_decomposition('3 6 4 1, 6 14 12 10, 21 48 48 33, 30 78 132 97')))

# # L = []
# # inp = open('test_in.txt', 'r')
# # out = open('test_out.txt', 'r')
# # a = inp.readlines()
# # b = out.readlines()
# # inp.close()
# # out.close()
# # h = 0

# # if LR_decomposition(a[-1]) != LR_decomposition1(a[-1]):
# #   print(LR_decomposition1(a[-1]), LR_decomposition(a[-1]))
# # while h < len(a) - 1:
# #   a[h] ="".join(list(a[h])[:-1])
# #   # print(a[h])
# #   b[h] ="".join(list(b[h])[:-1])
# #   if LR_decomposition(a[h]) != LR_decomposition1(a[h]):
# #     print(LR_decomposition1(a[h]))
# #     print(LR_decomposition(a[h]))
# #   h += 1
# import random
# def make_randm(n):
#   L = [[0] * n for x in range(n)]
#   for i in range(n):
#     for j in range(n):
#       if i == j:
#         L[i][j] = 1
#       elif i > j:
#         L[i][j] = random.randint(-15, 15)
#   R = [[0] * n for x in range(n)]
#   for i in range(n):
#     for j in range(n):
#       if i < j:
#         R[i][j] = random.randint(-15, 15)
#       elif i==j:
#         R[i][j] = random.randint(1, 15) * random.sample([1,-1], 1)[0]
#   return getString(multiply(L,R))

# for i in range(1, 100):
#   M = make_randm(i)
#   if LR_decomposition1(M) != LR_decomposition(M):
#     print('Matrix: ',M)
#     print('My: ' ,LR_decomposition(M))
#     print('JU: ', LR_decomposition1(M))



