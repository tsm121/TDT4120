counter = 0


def funksjon3(n):
  global counter
  if n > 0:
    counter +=1
    funksjon3(n//2-2)
    funksjon3(n//2-3)


counter = 0
def funksjon2(n):
  global counter

  if n >= 1:
    counter += 1
    funksjon2(n//3)
    funksjon2(2*n//3)


for i in range(1000,100000,2000):
  counter = 0
  funksjon2(i)
  print(counter)
  counter = 0
  funksjon3(i)
  print(counter)
  print()