"A generator does not have any data stored in anywhere, it generates the data in the way its needed"
lista = [1, 2, 3, -1, 4]
cadena = ["H", "O", "L", "A"]

l3 = list(c * num for c in cadena
          for num in lista
          if num > 0)

print(l3)


def factorial(n):
    i = 1

    while n > 1:
        i = n*i
        "iterate over a sequence, dont store the entire sequence"
        yield i
        n -= 1


for e in factorial(5):
    print(e)
