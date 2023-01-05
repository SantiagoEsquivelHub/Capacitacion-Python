def positiveNumbers(elem):
    return (elem > 0)


def oWords(elem):
    return (elem == "o")


lista = [1, -3, 2, -7, -8, -9, 10]
string = "Hello world"

lr = list(filter(positiveNumbers, lista))
lr2 = "".join(list(filter(oWords, string)))

"[1,2,10]"
print(lr)
"00"
print(lr2)
