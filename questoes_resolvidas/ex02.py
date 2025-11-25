"""Leia uma palavra. Se ela tiver algum número (0 a 9) no meio, imprima "ERRO" """

palavra = input()
numeros = "0123456789"

tem_numero = False

for i in palavra:
    if i in numeros:
        tem_numero = True
        break

if tem_numero == True:
    print("ERRO")
else:
    print("VALIDA")


