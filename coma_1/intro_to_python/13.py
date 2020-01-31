# 13. Umkehr Funktion

# gegeben ist ein String oder eine Liste,
# Ziel ist es das Object umzudrehen
# und auszugeben per print()

def reverse(input):
  # returning the input list or string from the back to the forth
  return input[::-1]

# Tests
print("Testing with List")
l = [1, 2, 3, 4, 5, 6]
print("-------------\nnormal")
print(l)
print("-------------\nreversed")
print(reverse(l))

print("Testing with String")
s = "Hallo Welt"
print("-------------\nnormal")
print(s)
print("-------------\nreversed")
print(reverse(s))
