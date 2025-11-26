"""Em matrizes, a "Diagonal Principal" é formada pelos números onde a Linha é igual
à Coluna (0,0), (1,1), (2,2)...

>> Missão:
Leia uma matriz 3x3. Some APENAS os números que estão na diagonal principal."""



matriz = []
soma_diagonal = 0

for i in range(3):
    linha = [int(x) for x in input().split()]
    matriz.append(linha)

for i in range(3):
    for j in range(3):
        if i == j:
            soma_diagonal += matriz[i][j]
print(soma_diagonal)