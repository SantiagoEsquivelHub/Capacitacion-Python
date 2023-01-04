def suma(num1=0, num2=0):
    print(num1 + num2)


def duplicarCadena(cadena="", veces=1, *algomas):
    print(cadena*veces)
    for cadena in algomas:
        print(cadena*veces)

suma(3)
duplicarCadena("Hola", 2, "Santiago", "Sanchez")
