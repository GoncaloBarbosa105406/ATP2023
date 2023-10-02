modo=int(input("Selecione o modo de jogo. Quer adivinhar o número que eu escolho (1), ou quer que eu adivinhe o número em que está a pensar (2)?"))

if modo==1 :
    import random
    n = random.randrange(1,100)
    tentativas=1
    palpite = int(input("Diga a primeira tentativa."))
    while n!= palpite:
        if palpite < n:
            palpite = int(input("Muito baixo. Diga outro número."))
            tentativas=tentativas+1
        elif palpite > n:
            palpite = int(input("Muito alto. Diga outro número."))
            tentativas=tentativas+1
    print("Parabéns, adivinhou o número em "+str(tentativas)+" tentativas.")

else:
    import random
    minimo=1
    maximo=100
    print("Pense num número entre 0 e 100")
    numero=random.randrange(1,100)
    print(numero)
    tentativas=1
    resultado=0
    while resultado != 3:
        resultado=int(input("Este número é muito grande(1), muito pequeno (2), ou correto (3)?"))
        print(resultado)
        if resultado==2:
            if numero>minimo:
                 minimo=numero+1
            numero=random.randint(minimo,maximo)
            print(numero)
        if resultado==1:
            if numero<maximo:
                 maximo=numero-1
            numero=random.randint(minimo,maximo)
            print(numero)
        tentativas=tentativas+1
    print("Já está! Acertei em "+str(tentativas)+" tentativas.")
