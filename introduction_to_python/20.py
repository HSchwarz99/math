from generate import generate

def calc(string):
  return eval(string)

s = generate(3)
print(s)
print(calc(s))
