import random
numero_secreto =random.randint(1,100)
tentativas=0
while True:
    palpite=int(input("Advinhe o número inteiro de 1 a 100:"))
    tentativas+=1

    if palpite==numero_secreto:
        print(f"Parabéns, você acertou o número em {tentativas} tentativas!")
        break
    elif palpite > numero_secreto:
        print("Errado. Tente um número menor.")
    else:
        if palpite ==0:
            print("Errado. Tente outro número.")
        else:
            print('Errado, tente um número maior.')



