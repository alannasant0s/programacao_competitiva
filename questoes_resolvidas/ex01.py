"""Leia o valor total (float) e o número de pessoas (int). Imprima quanto cada um paga,
formatado com DUAS casas decimais.
"""

valor = input().split()
valor_total = float(valor[0])
qtd_pessoas = int(valor[1])

print(f"Cada um paga: {valor_total / qtd_pessoas:.2f}")