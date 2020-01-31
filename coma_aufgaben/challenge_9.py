def evaluate(s):
  R = list() # geparste Liste
  I = 0 # index fuer die momentane Tiefe
  S = list() # Klammerliste
  C = [")", "}", "]"] # alle zugelassenen Klammerzu symbole
  O = ["(", "{", "["] # alle zugelassenen Klammerauf Symbole
  RO = ['+','*'] # alle zugelassenen rechenoperationen
  Z = ['0','1','2','3','4','5','6','7','8','9'] # alle zugelassenen Zahlen
  t = 0 # zahlt die maximale Tiefe
  L = list(s) # wandelt s in liste L um
  i = 0 # index des Elements aus L
  l = '+' # letztes Element fangt mit einem plus an, da Ausdruck mit Zahl oder Klammer auf starten sollte
  while i < len(L): # iteriert ueber L
    if L[i] in O: # guck ob das aktuelle Element eine offene Klammer ist
      if l not in O + RO: # guck ob das naechste Element valide ist
        raise Exception("syntaktisch inkorrekt")
      l = L[i] # aktualisiert letztes Element
      S.append(C[O.index(L[i])]) # fuegt die jeweilige Klammerzu zur Kalmmerauf zur Liste hinzu
      # geht in die aktuelle Liste rein
      k = I
      x = R
      while k > 0:
        k -= 1
        x = x[-1]
      # anfuegen einer leeren liste an der richtigen Stelle
      x.append(list())
      # aktuallisiert gegebenenfalls die maximale Tiefe
      if I == t:
        t += 1
      I += 1 # aktualisiert die aktuelle Tiefe
    elif S and L[i] == S[-1]: # guckt ob aktuelles Element das die Kalmmer ist durch die sie aktuelle Klammer wieder geschlossen wird
      if l not in Z + C:
        raise Exception("syntaktisch inkorrekt")
      l = L[i]
      I -= 1
      S.pop(-1)
    elif L[i] in C: # guck ob aktuelles Element eine nicht erwartete Klammer zu ist
      raise Exception("syntaktisch inkorrekt")
    else: # falls aktuelles Element ein anderes Zeichen ist
      if L[i] in Z: # falls aktuelles Element eine Zahl ist
        if l not in RO + O + Z: # falls aktuelles element nicht zu dem vorrigen element
          raise Exception("syntaktisch inkorrekt")
      elif L[i] in RO: # falls aktuelles Element eine Rechenoperation ist
        if l not in C + Z: # ueberprueft vorriges Element
          raise Exception("syntaktisch inkorrekt")
      else: # falls aktuelles Element ein nicht ueberprueftes Element ist
        raise Exception("syntaktisch inkorrekt")
      l = L[i] # neues letztes Element
      x = R
      k = I
      while k > 0:
        k -= 1
        x = x[-1]
      if x and type(x[-1]) == str:
        x[-1] = x[-1] + L[i]
      else:
        x.append(L[i])
    i += 1
  if S:
    raise Exception("syntaktisch inkorrekt")
  evalr(R)
  return (int(R[0], 10), t)

def evalr(R):
  if len(R) == 1 and type(R[0]) == str:
    t = R[0].split("+")
    i = 0
    y = 0
    while i < len(t):
      t[i] = t[i].split("*")
      k = 0
      x = 1
      while k < len(t[i]):
        try:
          int(t[i][k], 10)
        except Exception:
          raise Exception("syntaktisch inkorrekt")
        t[i][k] = int(t[i][k], 10)
        x *= t[i][k]
        k += 1
      t[i] = x
      y += t[i]
      i += 1
    R[0] = str(y)
  elif len(R) > 0:
    for x in R:
      if type(x) == list:
        evalr(x)
    y = ""
    for x in R:
      if type(x) == str:
        y += x
      else:
        y += x[0]
    R.clear()
    R.append(y)
    evalr(R)
  else:
    raise Exception("syntaktisch inkorrekt")

# print(evaluate("1+(1+1)*(1+1)"))
# print(evaluate("{1+1}*[1+1]+38"))
# print(evaluate("[{1}+5]*({2}+[{1*(3)}+2])"))
# print(evaluate("{3+2)+1"))
