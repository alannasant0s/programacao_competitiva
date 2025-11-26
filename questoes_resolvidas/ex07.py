"""O chat do jogo só permite mensagens curtas. Se a mensagem tiver mais de 20 letras,
ela deve ser cortada e receber "..." no final. Se for curta, imprime normal.

>> Missão:
Leia uma frase.
- Se tamanho > 20: Imprima os primeiros 20 caracteres + "..."
- Se tamanho <= 20: Imprima a frase original."""

frase = input()

tamanho = len(frase)
if tamanho <= 20:
    print(frase)
else:
    print(f"{frase[:20:]} ...")