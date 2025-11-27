"""O professor pediu para somar apenas os números PARES de uma lista.
Os ímpares devem ser ignorados.

>> Missão:
Leia uma lista de números inteiros. Some apenas os pares."""

lista = [int(x) for x in input().split()]
soma = 0

for i in lista:
    if i % 2 == 0:
        soma += i

print(soma)