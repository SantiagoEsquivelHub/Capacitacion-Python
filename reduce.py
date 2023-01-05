import functools

lista = ("H", "e", "l", "l", "o", "_", "W", "o", "r", "l", "d")
numeros = (1, 2, 3, 10)

sr = functools.reduce(lambda x, y: x+y, lista)
"Hello_World"
print(sr)

sr = functools.reduce(lambda x, y: x+y, numeros)
"3,3"
print(sr)
