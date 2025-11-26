"""Leia uma linha com vários números. Conte quantos números distintos existem."""

numeros = [int(x) for x in input().split()]
numeros_distintos = set(numeros)
print(f"{len(numeros_distintos)}")