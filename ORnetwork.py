#======================================================#
#  Definition of variables || Definição das variaveis  #
#======================================================#
#       |bias|x1|x2| 
matriz = [[1, 0, 0],           
          [1, 0, 1],           
          [1, 1, 0],           
          [1, 1, 1]]           

respostaMatriz = [0, 1, 1, 1]  # Answers            || Respostas da matriz
pesos = [0.0, 0.0, 0.0]        # weights            || Pesos dos neuronios
taxa_aprendizado = 0.5         # Learning rate      || Taxa de aprendizagem
resposta = ("")                # Auxiliary Variable || Variavel auxiliar
saida = 0                      # Activation Function|| Função de ativação
erro = 0                       # Auxiliary Variable || Variavel auxiliar
soma= 0                        # Sum function       || Função de soma

#======================================================#
#======================================================#

# Max of 20 iterations  || 20 iterações
for i in range(1, 21):  
      acertos = 0     
      print("#==============| 0{} |=================#\n".format(i))  

    #======================================================#
    # The following two fors will traverse the matrix      #
    # making the sum (weight * input)                      #
    #======================================================#
    # Os dois seguintes "fors" irão percorer a matriz      #
    # fazendo a somatoria (peso*entrada)                   #
    #======================================================#
      for j in range(0,4):     
            soma= 0   
            for k in range(0,3):  
                soma+= matriz[j][k] * pesos[k]  
             #======================================================#
             # Activation Function  =  step function                #
             #======================================================#             
             # Função de ativação  =  step function                 #
             #======================================================#
            if soma> 0:  
              saida = 1    
            else:  
              saida = 0
               #======================================================#
               # Compare answers and update weights if output does    #
               # not match with the expected value.                   #
               #======================================================#               
               # Compara as respostas e atualiza os pesos caso a      #
               # saida nao corresponda ao valor esperado              #
               #======================================================#             
            if saida == respostaMatriz[j]:  
              resposta = "✓"  
              acertos += 1  
              erro = 0       
            else:  
              resposta = "x"     
              erro = respostaMatriz[j] - saida
              #======================================================#
              # Updating weights                                     #
              # 0-- up to the amount of elements in weights          #
              #======================================================#
              # atualizando os pesos                                 #
              #0-- até a quantidade de elementos em pesos            #
              #======================================================#
            for k in range (0,3):  
                  pesos[k] = pesos[k] + (taxa_aprendizado * erro * matriz[j][k])     
            print("     {} {} || {}     {}   {} ".format(matriz[j][k-1],matriz[j][k], saida, resposta, pesos))
      if acertos == 4:    
          break;  

