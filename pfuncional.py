"Return the execution of a function"


""" def test(f):
    return f()


def toSend():
    return 2+2


print(test(toSend)) """


def selection(operation):

    def add(num1, num2):
        return num1+num2

    def multiply(num1, num2):
        return num1*num2

    if operation == "add":
        return add
    elif operation == "multiply":
        return multiply


keepedFunction = selection("add")
print(keepedFunction(5, 5))

keepedFunction2 = selection("multiply")
print(keepedFunction2(5, 5))