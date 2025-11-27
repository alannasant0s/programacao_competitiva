"""O chat do jogo não permite a palavra "noob".
Sempre que alguém escreve "noob", o sistema deve trocar por "****".

>> Missão:
Leia uma frase. Substitua TODAS as aparições de "noob" por "****".
(Dica: O Python tem uma ferramenta chamada .replace("velho", "novo"))."""

frase = input()
frase_nova = frase.replace("noob", "****")
print(frase_nova)
    