import random
def jogar():

 print("##################################")
 print("Bem Vindo ao jogo  de advinhação!")
 print("##################################")

 numero_secreto = (random.randrange(1, 101))
 total_rodadas = 0
 tentativa_atual = 1
 total_pontos = 100
 print ("você tem {} pontos".format(total_pontos))
 print("selecione o nivel 1(facil), 2 (medio), 3(dificil)")
 nivel = int(input ('digite aqui: '))

 if (nivel == 1):
    total_rodadas = 15 
 elif(nivel == 2):
   total_rodadas = 10
 else:
    total_rodadas = 5




 for tentativa_atual in range (1, total_rodadas + 1):
     print("tentativa {} de {}".format(tentativa_atual, total_rodadas))
 
     chute_stg = input("qual o numero secreto(ele esta entre 1 e 100)?")
     print("seu chute foi", chute_stg)
     chute = int(chute_stg)
     acertou = numero_secreto == chute
     maior = numero_secreto > chute
     menor = numero_secreto < chute
  
     if (chute < 1 or chute > 100 ):
         print("seu chute deve estar entre 1 e 100!")
         continue  
 
     if (acertou):
        print("Acerto mizeravi!")
        print ("você terminou com {} pontos".format(total_pontos))
        break
     else:
      if (maior):
         print('você errou, o numero secreto é maior')
         pontos_perdidos = abs(numero_secreto - chute)
         total_pontos = total_pontos - pontos_perdidos
         
      elif (menor):
         print("você errou, o numero secreto é menor")
         pontos_perdidos = abs(numero_secreto - chute)
         total_pontos = total_pontos - pontos_perdidos
         

 print("esse era o numero secreto:", numero_secreto)   
 print("fim de jogo")

if (__name__ == "__main__"):
   jogar()