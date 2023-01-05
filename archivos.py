"""
r+ reading and writing the file.
w write
a append to the end
"""

""" try:
    file = open("ejemplo.txt", "r+")
except:
    print("Error opening file")
else:
    file.close()
    print(file) """

try:
    file = open("ejemplo.txt", "r")
except:
    print("Error opening file")
    exit()


"""file.write("hola soy santiago")
 file.seek(11)
file.write("INTRUSO") 
print(file.tell()) """

""" agregar = [" Hola Mundo\n", " \tHola Programadores"]
file.close()

if not file.closed:
    file.writelines(agregar) """

print(file.readline())

