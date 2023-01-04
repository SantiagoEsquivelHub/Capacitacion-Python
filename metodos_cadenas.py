cad = "Hola mundo"
print(len(cad))

# Case
""" string.count(valor, inicio, fin) """
print(cad.count("0", 0, 3))

# Uppercase
print(cad.upper())
# Lowercase
print(cad.lower())

# Replace
""" string.replace(valor, nuevo, repeticiones) """
print(cad.replace("o", "x", 1))

# Split
""" string.split(separador, maxsplit) """
print(cad.split("o", 1))

# Find
""" string.find(valor, inicio, fin) """
print(cad.find("o"))

# Join
""" string.join(secuencia) """
cad2 = ["h", "o", "l", "a"]
s = ";"
print(s.join(cad2))
