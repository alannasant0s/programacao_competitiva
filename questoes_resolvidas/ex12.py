"""O professor pediu para contar quantas vogais existem numa frase para uma análise
criptográfica. As vogais são: a, e, i, o, u.

>> Missão:
Leia uma frase (tudo minúsculo). Conte quantas vogais ela tem no total."""


frase = input().lower()
vogais = "aeiou"
contador = 0

for i in frase:
    if i in vogais:
        contador += 1
print(contador)

