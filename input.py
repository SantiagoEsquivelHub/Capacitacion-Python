""" 
%s string (20s add spaces to left, -20s add spaces to right)
%d int
%f float, .numero (number of digits to take)
"""
age = 19
name = "Santiago Sanchez"
print("I'm %s and I'm %d years old" % (name, age))

try:
    valor = input()
    valor = int(valor)
except:
    print("This is not a number")
else:
    print(valor)
