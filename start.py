import random 

def jogo_adivinhacao():
    print("Bem-vindo ao Jogo da Adivinhação!")
    print("Tente adivinhar o número entre 1 e 100.")

    numero_secreto = random.randint(1, 100)
    tentativas = 0

    while True:
        try:
            chute = int(input("Digite seu palpite: "))
            tentativas += 1

            if chute < 1 or chute > 100:
                print("Por favor, escolha um número entre 1 e 100.")
                continue

            if chute < numero_secreto:
                print("Muito baixo!")
            elif chute > numero_secreto:
                print("Muito alto!")
            else:
                print(f"Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas.")
                break
        except ValueError:
            print("Por favor, insira um número válido.")

if __name__ == "__main__":
    jogo_adivinhacao()

    flo
