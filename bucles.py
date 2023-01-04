edad = 0


while edad <= 20:

    if edad == 15:
        edad = edad + 1
        continue

    print("You are " + str(edad) + "years old")
    edad = edad + 1


lista = ["Elemento 1", "Elemento 2", "Elemento 3"]

for elemento in lista:
    print(elemento)
