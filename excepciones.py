""" try:
    print(n/0)
except (TypeError, NameError):
    print("Error in type or name")
except ZeroDivisionError:
    print("You cannot divide by cero")
else:
    print("There's not any error :)")
finally:
    print("I will always be executed")
"""


class UnoError(Exception):
    def __init__(self, value):
        self.valueError = value

    def __str__(self):
        return ("You cannot divide by cero the number: " + str(self.valueError))


print("Welcome")

n = -5

try:
    if n < 0:
        raise UnoError(n)
except UnoError:
    print("holaaa")


if n < 0:
    raise UnoError(n)

print("Bye")
