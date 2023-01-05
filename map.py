def operator(n, m):

    if n == None or m == None:
        return 0

    return n+m


l1 = [1, 2, 3, 4]
t1 = (9, 8, 7, 6)

"Return an iterator that applies function to every item of iterable, yielding the results."
lr = list(map(operator, l1, t1))

"[10,10,10,10]"
print(lr)

s1 = "Hola"
s2 = "Mundo"
lr2 = list(map(operator, s1, s2))

"[HM,ou,ln,ad]"
print(lr2)


"Python functions with labmda, if we dont wh"
list_numbers = [1, 2, 3, 4]

map_iterator = list(map(lambda x: x * 2, list_numbers))
print(map_iterator)
