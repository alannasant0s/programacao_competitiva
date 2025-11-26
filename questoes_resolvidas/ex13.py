"""Numa corrida, você recebe a lista de tempos dos pilotos.
Você precisa dizer QUAL foi o maior tempo e EM QUAL POSIÇÃO (índice) ele está.
(Lembre-se: a contagem começa do 0).

>> Missão:
Leia uma lista de números. Imprima o maior valor e o índice dele."""

lista = [int(x) for x in input().split()]
maior = max(lista)

for numero in lista:
    if numero == maior:
        print(f"Maior: {maior}")
        print(f"Posição: {lista.index(maior)}")
        