"""Leia 5 números inteiros na mesma linha. Imprima os 3 maiores, do maior para o menor.
"""

numeros = [int(x) for x in input().split()]
numeros.sort(reverse = True)

print(f"{numeros[0]}")
print(f"{numeros[1]}")
print(f"{numeros[2]}")