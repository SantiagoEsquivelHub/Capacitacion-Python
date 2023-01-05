class Decorator(object):
    def __init__(self, function):
        self.function = function

    def __call__(self, *args: any, **kwds: any):
        print("Decorated executed " + self.function.__name__ + " " + str(args))
        self.function(*args, **kwds)


@Decorator
def subtraction(n, m):
    print(n-m)


subtraction(3, 2)
