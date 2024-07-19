import random
def jogo_adivinhacao(numero_secreto, tentativas=1):
    tentativa1 = int(input("Digite um número entre 1 a 10: "))

    if tentativa1 < numero_secreto:
        print("Tente um número maior.")
        return jogo_adivinhacao(numero_secreto, tentativas + 1 )
    elif tentativa1 > numero_secreto:
        print("Tente um número menor.")
        return jogo_adivinhacao(numero_secreto, tentativas + 1)
    else:
        print(f"Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas.")

def iniciar_jogo_adivinhacao():
    numero_secreto = random.randint(1, 10)
    jogo_adivinhacao(numero_secreto)

iniciar_jogo_adivinhacao()
