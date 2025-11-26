# Leia uma lista de notas (float) na mesma linha. Conte quantas são >= 7.0

alunos = [float(x) for x in input().split()]

contagem = 0
for i in alunos:
    if i >= 7.0:
        contagem += 1

print(contagem)