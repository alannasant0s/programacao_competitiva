""">> Missão:
Leia uma matriz 3x3. Encontre o número 7 (ou 007).
Imprima: "Espiao encontrado na Linha X Coluna Y".
(Assuma que sempre haverá um número 7).
"""

matriz = []
numero_espiao = False
for i in range(3):
    linha = [int(x)for x in input().split()]
    matriz.append(linha)

for i in range(3):
    for j in range(3):
        if matriz[i][j] == 7:
            numero_espiao = True
            print(f"Espião encontrado na linha {i} e coluna {j}")
            break
    if numero_espiao:
        break
    
if not numero_espiao:
    print("Nenhum espião encontrado")


