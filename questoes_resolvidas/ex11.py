"""O sistema do jogo mostra o tempo jogado apenas em MINUTOS (ex: 130 min).
Você precisa converter isso para o formato HORAS:MINUTOS para o placar.

>> Missão:
Leia um número inteiro (minutos totais).
Imprima quantas horas e quantos minutos isso representa."""

minutos_total = int(input())
hora = minutos_total // 60
minutos = minutos_total % 60

print(f"{hora}h:{minutos}min")