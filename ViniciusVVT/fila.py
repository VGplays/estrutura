import random


class EmptyQueueError(Exception):
    ...


class No():
    def __init__(self, valor: int):
        self.valor = valor
        self.prox = No


class Fila():
    def __init__(self):
        self.primeiro: No = None
        self.ultimo: No = None
        self.contador = 0

    def push(self, No_valor: int):
        novo_No = No(No_valor)
        if not self.primeiro:
            self.primeiro = novo_No
        if not self.ultimo:
            self.ultimo = novo_No
        else:
            self.ultimo.prox = novo_No
            self.ultimo = novo_No
        self.contador += 1

    def pop(self):
        if not self.primeiro:
            raise EnvironmentError("fila vazia")

        primeiro = self.primeiro

        if hasattr(self.primeiro, "proximo"):
            self.primeiro = self.primeiro.prox
        else:
            self.primeiro = None

        self.contador -= 1


fila = Fila()
fila.push(2)
print(fila)
fila.push(5)
print(fila)
fila.pop()
print(fila)
