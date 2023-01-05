"List compression in python is based on creating lists from other lists, tuples and any iterable"
lista = [1, 2, 3, -1, 4]
cadena = ["H", "O", "L", "A"]
l2 = [num for num in lista if num > 0]

"[1,2,3,4]"
print(l2)

l3 = [c * num for c in cadena
      for num in lista
      if num > 0]

print(l3)
