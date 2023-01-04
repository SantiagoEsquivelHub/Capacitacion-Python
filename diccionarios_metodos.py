diccionario = {
    "redes_sociales": ["twitter", "facebook", "linkedin"],
    3: "Tres",
    "Hola": "Mundo"
}

"has_key"
print("Hola" in diccionario)

"lista con tuplas (clave, valor)"
print(diccionario.items())

"lista con las claves del diccionario"
print(diccionario.keys())

"lista con los valores del diccionario"
print(diccionario.values())

"diccionario.pop(valor,valorSiNoSeEncuentra)"
print(diccionario.pop(4, -1))
print(diccionario)

diccionario2 = diccionario.copy()
print(diccionario2)

del diccionario[3]
print(diccionario)

diccionario.clear()
print(diccionario)

