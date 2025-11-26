"""Leia uma frase. Imprima as palavras de trás para frente.
Atenção: Não é inverter as letras (ovO), é inverter a ordem das palavras!"""

frase = input().split()
frase_invertida = frase[::-1]
print(f"{" ".join(frase_invertida)}")


