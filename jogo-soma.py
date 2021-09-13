print("****************************************")
print("Testando seu conhecimento em matemática ")  
print("****************************************")

nome = input("Qual seu nome? ")
print(" Olá {}, seja bem vindo!".format(nome), "\n Agora que comecem os jogos :-P")

resposta_correta = 4
tentativas = 3

for rodada in range (1, tentativas +1):
    resposta = int(input("Quanto é 2+2? "))
    
    acertou = resposta == resposta_correta
    errou = resposta != resposta_correta
    p_dica = rodada == 1
    s_dica  = rodada == 2
    t_dica = rodada == 3

    if(acertou):
        print("Incrivel você acertou 2+2={}".format(resposta_correta), "\n Fim de Jogo :)")
        break
    else:
        if (p_dica):
            print("Você errou, {} não é a resposta correta, você tem mais uma chance." .format(resposta))
        elif (s_dica):
            print("Você errou de novo, {} não é a resposta correta, ultima chance presta baste atenção." .format(resposta))
        elif (t_dica):
            print("Você errou de novo, {} não é a resposta correta, você é fraco, lhe falta exercicios e estudo!.\nVeja o video e tente novamente mais tarde \nhttps://www.youtube.com/watch?v=kq0kh0XvT9c&ab_channel=Ensinandomeufilho" .format(resposta))
