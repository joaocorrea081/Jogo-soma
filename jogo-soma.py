"""print("Estudo Pyton, programa 1")
print(" Objetivo: Textar conhecimento de funções matematicas")
print(" caso o jogador erre sera lhe oferecida uma dica, caso persista no erro um video e o jogo fecha")
print("Objetivo é ter 3 questãoes para cada uma das principais funções matematicas com diversos ")
print("niveis de dificuldade")
print("******************")
print("Ola caro jogador!")
print("******************")
print("vamos textar seus conhecimentos matematicos?", end="\n")
print("primeiramente me diga:")"""

nome = input("Qual seu nome? ")
print(" Olá {}, seja bem vindo!".format(nome), "\n Agora que comecem os jogos :-P")
resposta = int(input("Quanto é 2+2? "))
resposta_correta = 4
tentativas = 3
#rodada = 1

#while(rodada <= tentativas):
for rodada in range (1, tentativas +1):
    
    acertou = resposta == resposta_correta
    errou = resposta != resposta_correta
    p_dica = resposta > 5
    s_dica = resposta <= 3 
    if(acertou):
        print("Incrivel você acertou 2+2={}".format(resposta_correta), "\n Fim de Jogo :)")
        break
    else:
        if (p_dica):
            print("Você errou, não é o numero correto, você tem mais uma chance")
            
        elif(s_dica):
            print("Ola")
    
    

            
#rodada = rodada +1
"""else:
        if (errou):
            print(nome, "você errou ", errou ,"não é a resposta correta")
        elif (errou):
            print("vamos tentar novamente"," 2+2 =","(1+1)+(1+1)")
            
print("Que é igual a 1+1+1+1")
        print("vamos tentar novamente:")

    soma1c = input("Olhe para sua mão e contes os dedos e me diga: Quanto é 2+2? ")
    print("você falou que 2+2=" , soma1c)
    soma1 = int(soma1c)

    if(soma1c == soma1):
        print("**Parabens", nome,"!**", "você acertou 2+2=4")
    else:
        print("você é fraco, lhe falta exercicios e estudo!")
        print("copie o link:"," https://www.youtube.com/watch?v=kq0kh0XvT9c&ab_channel=Ensinandomeufilho ")
        print(" veja o video e tente novamente mais tarde")"""