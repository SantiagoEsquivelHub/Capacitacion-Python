lista = [1, "Dos", 3, 3]

buscar = 5

if buscar in lista:
    print(lista.index(buscar))
else:
    print("The element has not found")

lista.append("new element")
print(lista)

print(lista.count(3))

lista.insert(3, "hi")
print(lista)

""" iterable = "cadena"
lista.extend(iterable)
print(lista) """

# Se elimina con indice
lista.pop(1)
print(lista)

# Se elimina con valor la primera ocurrencia
lista.remove(3)
print(lista)

lista.reverse()
print(lista)

