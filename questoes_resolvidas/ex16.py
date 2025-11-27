"""Você precisa pintar uma parede. Sabe-se que cada litro de tinta pinta 2 metros quadrados.
Você recebe a Largura e a Altura da parede.
Quantos litros de tinta são necessários?

>> Missão:
Leia Largura e Altura (floats). Calcule a Área (Largura x Altura).
Divida por 2 para achar os litros.
Imprima formatado com 1 casa decimal."""

medidas = [float(x) for x in input().split()]
largura = medidas[0]
altura = medidas[1]

area = largura * altura
qtd_litros = area / 2
print(f"{qtd_litros:.1f} litros")
