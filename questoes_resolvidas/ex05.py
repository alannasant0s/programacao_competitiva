""">> Missão:
Leia uma matriz 3x3. Conte quantas Pedras (número 1) existem no total.
Depois, diga se o robô consegue passar (menos de 5 pedras) ou se está bloqueado
(5 ou mais pedras)."""
pedras = 0
matriz = []

for i in range(3):
    linha = [int(x) for x in input().split()]
    matriz.append(linha)

for i in range(3):
    for j in range(3):
        if matriz[i][j] == 1:
            pedras += 1

if pedras < 5:
        print("consegue passar")
else:
        print("bloqueado")
