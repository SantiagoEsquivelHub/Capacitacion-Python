# encoding utf-8
edad = 18
m_edad = 18

""" if edad >= m_edad:
    print("You're an adult")
    if True:
        print("This run as long as you are of legal age")
else:
    print("You are not an adult")

print("This always run") """


if edad >= 0 and edad < 18:
    print("You're a child")
elif edad >= 18 and edad < 27:
    print("You're a teen")
elif edad >= 27 and edad < 60:
    print("You're an adult")
