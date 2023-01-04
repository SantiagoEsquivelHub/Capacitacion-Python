lista = [2, "tres", True, ["uno", 10]]
print(lista)

lista[1] = 4

"Desde el indice 0, copia los 3 elementos siguientes"
lista2 = lista[0:3]
print(lista2)

"Desde el indice 0, copia los 3 elementos siguientes y salta de 1 en 1"
lista2 = lista[0:3:2]
print(lista2)

"Desde el indice 0, copia todos los elementos siguientes y salta de 1 en 1"
lista2 = lista[0::2]
print(lista2)

"Asignar valores a posiciones de una lista"
lista[0:2] = [4]
print(lista)

"Indice negativo"
lista2 = lista[-1]
print(lista2)
