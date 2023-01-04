class Humano:
    def __init__(self, edad):
        self.edad = edad

    def hablar(self, message):
        print(message)


class IngSistemas(Humano):
    def programar(self, language=""):
        print("I'm going to programe in " + language)


class LicDerecho(Humano):
    def estudiarCaso(self, case=""):
        print("I have to study the case of " + case)


class Estudioso(IngSistemas, LicDerecho):
    pass


pedro = IngSistemas(26)
raul = LicDerecho(21)
"pepe takes the init function from IngSistemas, because its on the first place of the heritage"
pepe = Estudioso(15)
""" print("I'm Pedro, and I'm " + str(pedro.edad) + " years old")
print("I'm Raul, and I'm " + str(raul.edad) + " years old") """


pedro.hablar("Hello")
raul.hablar("Hi, Pedro!")
pepe.hablar("Hey, I'm multiple heritage!")

pedro.programar("Python")
raul.estudiarCaso("Mr. Sánchez")
pepe.programar("C#")
pepe.estudiarCaso("Mr. Esquivel")
