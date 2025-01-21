import random

nsorteado = random.randint(0,10)
chaces = 5
again = True
while again == True:
    if chaces == 0:
        print("suas chances acabaram \n ")
        restart = str(input("digita y pra tentar novamente ou n para finalizar"))
        while True:
            if restart == "y":
                chaces = 5
                break
            else:
                again = False
                break
        
    elif chaces > 0:
        print(f"voce tem : {chaces} chaces")
        ninserido = int(input("qual foi o numero sorteado ? \n :"))

        if nsorteado == ninserido:
            print("acertou!")
            print(f"o numero sorteado foi: {nsorteado}")
            break

        else:
            chaces-= 1
            print("errou")
        

print("partida finalizada")


