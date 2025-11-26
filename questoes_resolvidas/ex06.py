"""Vocês estão planejando a viagem para a competição. Precisam calcular se o carro
é econômico.

>> Missão:
Leia a distância percorrida (em Km) e o combustível gasto (em Litros).
Calcule o consumo médio (Km/l) e imprima formatado com 3 casas decimais."""

gasto = [float(x) for x in input().split()]
distancia = gasto[0]
combustivel = gasto[1]

print(f"{distancia / combustivel:.3f} km/l")