"function that adds a funcionality to another function that is received as a parameter"

logged = True
usuario = "Santiago"


def decorator(functionn):
    def decoratedFunction(*args, **kwargs):
        print("Decorated executed " + functionn.__name__ + " " + str(args))
        functionn(*args, *kwargs)
    return decoratedFunction


def admin(f):
    def check(*args, **kwargs):
        if logged:
            f(*args, **kwargs)
        else:
            print("You do not have permissions to execute " + f.__name__)
    return check


@admin
@decorator
def subtraction(n, m):
    print(n-m)


subtraction(3, 2)
