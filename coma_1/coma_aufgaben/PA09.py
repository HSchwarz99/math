def evaluate(s):
  s = list(s) # string als Liste
  K = [] # Klammer liste
  T = 0 # max Tiefe
  t = 0 # aktuelle Tiefe
  FS = '' # finaler String
  l = '+' # letztes Element
  KA = ['(', '[', '{']
  KZ = [')', ']', '}']
  while len(s) > 0:
    a = s.pop(0)
    if a in '0123456789' and l in '([{+*0123456789':
      FS += a
    elif a in '+*' and l in ')]}0123456789':
      FS += a
    elif a in '([{' and l in '([{+*':
      FS += '('
      if T == t:
        T += 1
      t += 1
      K.append(a)
    elif a in ')}]' and l in ')}]0123456789':
      FS += ')'
      if KZ.index(a) != KA.index(K[-1]):
        raise Exception("syntaktisch inkorrekt")
      K.pop()
      t -= 1
    else:
      raise Exception("syntaktisch inkorrekt")
    l = a
  if K:
    raise Exception("syntaktisch inkorrekt")
  return (eval(FS), T)

# print(evaluate("1+(1+1)*(1+1)"))
# print(evaluate("{1+1}*[1+1]+38"))
# print(evaluate("[{1}+5]*({2}+[{1*(3)}+2])"))
# print(evaluate("{3+2)+1"))
