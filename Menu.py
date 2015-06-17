#encoding: utf-8


print "\t        ─▄▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▄─ "
print "\t         █░░░█░░░░░░░░░░▄▄░██░█ "
print "\t         █░▀▀█▀▀░▄▀░▄▀░░▀▀░▄▄░█ "
print "\t         █░░░▀░░░▄▄▄▄▄░░██░▀▀░█"
print "\t        ─▀▄▄▄▄▄▀─────▀▄▄▄▄▄▄▀─"

opcao=input ("\n\n\t\tSelecione o jogo desejado: \n\t\t1-Jogo da Velha \n\t\t2-Jokenpô \n\t\t3-Par ou Impar \n\t\t4-Quiz \n\t\t5-Sobre \n\t\t6-Sair\n\n")

#os.system(['clear','cls'][os.name == 'nt'])
if opcao==1:
	matriz = [['-','-','-'],
                      ['-','-','-'],
                      ['-','-','-']] 

            print('\n\n\tJOGO DA VELHA \n\n\n')
            print('\n')
            print('\t  0   1   2')
            print'\t0 %s | %s | %s ' % (matriz[0][0], matriz[0][1], matriz[0][2])
            print'\t  ---------- '
            print'\t1 %s | %s | %s ' % (matriz[1][0], matriz[1][1], matriz[1][2])
            print'\t  ----------'
            print'\t2 %s | %s | %s ' % (matriz[2][0], matriz[2][1], matriz[2][2])
            print'\n'

            print 'Jogador 1 = X e Jogador 2 = O'
            vez=2
            op = 'S'
            velha=0

            if op=='S':
                for i in range(100):
                    if vez%2==0:
            
                            print 'Jogador 1, digite as coordenadas da sua jogada'
                            linha = input ('Linha: ')
                            coluna = input ('Coluna: ')
                            if (matriz[linha][coluna]=='-'):
                                matriz[linha][coluna]='X'
                                    
                            else:
                                while (matriz[linha][coluna]!='-'):
                                    print 'Jogada inválida, digite novamente'
                                    linha = input ('Linha: ')
                                    coluna = input ('Coluna: ')
                                    matriz[linha][coluna]='X'
                            
                            print '\n' * 100
                            print'\n'
                            print'\t  0   1   2'
                            print'\t0 %s | %s | %s ' % (matriz[0][0], matriz[0][1], matriz[0][2])
                            print'\t  ---------- '
                            print'\t1 %s | %s | %s ' % (matriz[1][0], matriz[1][1], matriz[1][2])
                            print'\t  ----------'
                            print'\t2 %s | %s | %s ' % (matriz[2][0], matriz[2][1], matriz[2][2])
                            print'\n'

                    else:
                        print 'Jogador 2, digite as coordenadas da sua jogada'
                        linha = input ('Linha: ')
                        coluna = input ('Coluna: ')
                        if matriz[linha][coluna]=='-':
                            matriz[linha][coluna]='O'
                        else:
                            while (matriz[linha][coluna]!='-'):
                                print 'Jogada inválida, digite novamente'
                                linha = input ('Linha: ')
                                coluna = input ('Coluna: ')
                                matriz[linha][coluna]='X'
                            
                            print '\n' * 100 
                            print'\n'
                            print'\t  0   1   2'
                            print'\t0 %s | %s | %s ' % (matriz[0][0], matriz[0][1], matriz[0][2])
                            print'\t  ---------- '
                            print'\t1 %s | %s | %s ' % (matriz[1][0], matriz[1][1], matriz[1][2])
                            print'\t  ----------'
                            print'\t2 %s | %s | %s ' % (matriz[2][0], matriz[2][1], matriz[2][2])
                            print'\n'
                    vez+=1
                    
                    #verificando as linhas
                    if(matriz[0][0]=='X' and matriz[0][1]=='X' and matriz[0][2]=='X'):
                        print "\nJogador 1, Venceu !!"
                        break
                    else:
                        velha+=1

                    if(matriz[1][0]=='X' and matriz[1][1]=='X' and matriz[1][2]=='X'):
                        print "\nJogador 1, Venceu !!"
                        break
                    else:
                        velha+=1

                    if(matriz[2][0]=='X' and matriz[2][1]=='X' and matriz[2][2]=='X'):
                        print "\nJogador 1, Venceu !!"
                        break
                    else:
                        velha+=1

                    if(matriz[0][0]=='O' and matriz[0][1]=='O' and matriz[0][2]=='O'):
        
                        print "\nJogador 2, Venceu !!"
                        break
                    else:
                        velha+=1

                    if(matriz[1][0]=='O' and matriz[1][1]=='O' and matriz[1][2]=='O'):
                        print "\nJogador 2, Venceu !!"
                        break
                    else:
                        velha+=1

                    if(matriz[2][0]=='O' and matriz[2][1]=='O' and matriz[2][2]=='O'):
                        print "\nJogador 2, Venceu !!"
                        break
                    else:
                        velha+=1

                    #verificando as colunas
                    if(matriz[0][0]=='X' and matriz[1][0]=='X' and matriz[2][0]=='X'):
                        print "\nJogador 1, Venceu !!"
                        break
                    else:
                        velha+=1

                    if(matriz[0][1]=='X' and matriz[1][1]=='X' and matriz[2][1]=='X'):
                        print "\nJogador 1, Venceu !!"
                        break
                    else:
                        velha+=1

                    if(matriz[0][2]=='X' and matriz[1][2]=='X' and matriz[2][2]=='X'):
                        print "\nJogador 1, Venceu !!"
                        break
                    else:
                        velha+=1

                    if(matriz[0][0]=='O' and matriz[1][0]=='O' and matriz[2][0]=='O'):
                        print "\nJogador 2, Venceu !!"
                        break
                    else:
                        velha+=1

                    if(matriz[0][1]=='O' and matriz[1][1]=='O' and matriz[2][1]=='O'):
                        print "\nJogador 2, Venceu !!"
                        break
                    else:
                        velha+=1

                    if(matriz[0][2]=='O' and matriz[1][2]=='O' and matriz[2][2]=='O'):
                        print "\nJogador 2, Venceu !!"
                        break
                    else:
                        velha+=1

                    #verificando as diagonais
                    if(matriz[0][0]=='X' and matriz[1][1]=='X' and matriz[2][2]=='X'):
                        print "\nJogador 1, Venceu !!"
                        break
                    else:
                        velha+=1

                    if(matriz[0][2]=='X' and matriz[1][1]=='X' and matriz[2][0]=='X'):
                        print "\nJogador 1, Venceu !!"
                        break
                    else:
                        velha+=1

                    if(matriz[0][0]=='O' and matriz[1][1]=='O' and matriz[2][2]=='O'):
                        print "\nJogador 2, Venceu !!"
                        break
                    else:
                        velha+=1

                    if(matriz[0][2]=='O' and matriz[1][1]=='O' and matriz[2][0]=='O'):
                        print "\nJogador 2, Venceu !!"
                        break
                    else:
                        velha+=1

                    if(velha==144):
                        print "\nDeu Velha !!  "
                        break	

            op = raw_input ('Deseja jogar novamente ? "S"-sim ou "N"-não : ')
            if op == 'S':
                matriz = [['-','-','-'],
                          ['-','-','-'],
                          ['-','-','-']]
                print'\n'
                print'\t  0   1   2'
                print'\t0 %s | %s | %s ' % (matriz[0][0], matriz[0][1], matriz[0][2])
                print'\t  ---------- '
                print'\t1 %s | %s | %s ' % (matriz[1][0], matriz[1][1], matriz[1][2])
                print'\t  ----------'
                print'\t2 %s | %s | %s ' % (matriz[2][0], matriz[2][1], matriz[2][2])
                print'\n'

            if op == 'N':
                opcao=input ('\n\n\t\t Selecione o jogo desejado: \n\t\t 1-Jogo da Velha \n\t\t 2-Jokenpô \n\t\t 3-Par ou I')
elif opcao==2:
    	
        #variaveis
        vitorias1 =0
        vitorias2 =0
        empates=0
        derrotas1 =0
        derrotas2 =0
        jg1 = 1
        jg2 = 1
        
  
        #variaveis

        #menu
        print("\t***JOKENPO***\n")
        print("1.Jogar\n2.Instrucoes\n0.Sair")
        jg1 = input(": ")
        while(jg1 == 2):
            print("\nComo jogar:\nPara jogadas voce tem\n1 para pedra\n2 para tesoura\n3 para papel.\n A jogada do computador eh aleatoria para evitar qualquer tipo de desconfianca.")
            print("Para sair basta digitar 0 nos momentos em que lhe eh cedida a jogada. Voce eh o jogador 1.")
            print("Esse eh um jogo com foco academico apenas para o aprendizado\nna liguagem Python aplicado com controle de versao (Git)")
            jg1 = input(": ")
        while(jg1 != 0 and jg1 != 1 and jg1 != 2):
            jg1 = input(": ")
        #menu	

        #jogando
        while(jg1 != 0 ):
	
                print("\n1. Pedra  2. Tesoura  3. Papel")
                jg1 = input(":   ")
                jg1 = int(jg1)
                while(jg1 > 3):
                    jg1 = input(":   ")
                    jg1 = int(jg1)
                import random
                random.random()
                jg2 = random.randint(1,3)
                jg2 = int(jg2)
                if(jg1 != 0):
                    print 'PC:',jg2
	
                if(jg1 == jg2):
                    empates+=1
                print("Empate")

                if(jg1 == 1 and jg2 == 2):
                        vitorias1+=1
                        derrotas2+=1
                        print("J1 venceu")
                if(jg2 == 1 and jg1 == 2):
                        vitorias2+=1
                        derrotas1+=1
                        print("PC venceu")
                if(jg1 == 2 and jg2 == 3):
                        vitorias1+=1
                        derrotas2+=1
                        print("J1 venceu")
                if(jg2 == 2 and jg1 == 3):
                        vitorias2+=1
                        derrotas1+=1
                        print("PC venceu")
                if(jg1 == 3 and jg2 == 1):
                        vitorias1+=1
                        derrotas2+=1
                        print("J1 venceu")
                if(jg2 == 3 and jg1 == 1):
                        vitorias2+=15
                        derrotas1+=1
                        print("PC venceu")
	
        #jogando

        #estatisticas finais
        if(vitorias1 > vitorias2):
            print("\n\nJogador 1 venceu o jogo")
        if(vitorias1 < vitorias2):
            print("\n\nJogador 1 perdeu o jogo")
        if(vitorias1 == vitorias2):
            print("\n\nEMPATE")

        print("\nJogador 1: ")
        print 'Vitorias: ',vitorias1
        print 'Derrotas: ',derrotas1

        print("\nPC: ")
        print'Vitorias: ',vitorias2
        print'Derrotas: ',derrotas2

        print'\nEmpates: ',empates

        print("FIM DE JOGO\n")

elif opcao==3:
	print "Coloque seu codigo aqui"
elif opcao==4:
	print ('')
    print('		??????????')
    print('		??	??')
    print('		??	??')
    print('		??	??')
    print('			??')
    print('			??  BEM VINDO AO QUIZ')
    print('		       ?? ')
    print('		      ??  ')
    print('		     ??   ')
    print('                    ?? ')
    print('                    ?? ')
    print('                    ?? ')
    print('                    ?? ')
    print('')                  
    print('                    ??')			
    print ('\n\nAo final das perguntas, digite a resposta que achar correta, sempre com letras minúsculas.' )
    print('\nCaso queira abandonar o jogo, digite s, quando for solicitado algo para continuar.')
	
       
    a= raw_input ('Digite algo para começar ' )
    os.system('cls')
    while a!= 's':
        cont=0
        print('		***************')
        print('		 Seus pontos:')
        print('		             ')
        print('		    %d        '%cont)
        print('                             ')
        print('		***************')
        print('O comando para escrever algo na tela usando python é:')
        print('a)print')
        print('b)write')
        print('c)printf')
        op=raw_input('d)raw_input\n')

        if op=='a':
            cont+=10
            print('Resposta correta. Você ganhou mais 10 pontos!!!')
        else:
            print('Resposta errada')
        a= raw_input ('Digite algo para continuar e s caso queira sair ' )
        if a=='s':
            if cont<=100:
                print('\tVocê fez %d pontos. Pode ser melhor!!!'%cont)
            elif (cont>100 and cont<=140):
                print('\tVocê fez %d pontos. Isto foi bom!!!'%cont)
            elif (cont>140 and cont<=180):
                print('\tVocê fez %d pontos. Parabéns!!!'%cont)
            elif (cont>180 and cont<=200):
                print('\tVocê fez %d pontos. Excelente!!!'%cont)
            cont=0
            print('\tObrigado por jogar!!!')
            break
        os.system('cls')
        print('		***************')
        print('		 Seus pontos:')
        print('		             ')
        print('		    %d        '%cont)
        print('                             ')
        print('		***************')
        print('São cursos relativos à informática, exceto: ')
        print('a)Sistemas de Informação')
        print('b)Engenharia de Sistemas')
        print('c)Administração')
        op=raw_input('d)NDA \n')
        if op== 'c':
            cont+=10
            print('Resposta correta. Você ganhou mais 10 pontos!!!')
        else:
            print('Resposta errada')
        a= raw_input ('Digite algo para continuar e s caso queira sair ' )
        if a=='s':
            if cont<=100:
                print('\tVocê fez %d pontos. Pode ser melhor!!!'%cont)
            elif (cont>100 and cont<=140):
                print('\tVocê fez %d pontos. Isto foi bom!!!'%cont)
            elif (cont>140 and cont<=180):
                print('\tVocê fez %d pontos. Parabéns!!!'%cont)
            elif (cont>180 and cont<=200):
                print('\tVocê fez %d pontos. Excelente!!!'%cont)
            cont=0
            print('\tObrigado por jogar!!!')
            break
        os.system('cls')
        print('		***************')
        print('		 Seus pontos:')
        print('		             ')
        print('		    %d        '%cont)
        print('                             ')
        print('		***************')
        print('São áreas de atuação dos profissionais de informática, exceto: ')
        print('a)Suporte Técnico')
        print('b)Programação')
        print('c)Web Designer')
        op=raw_input('d)Medicina \n')
        if op== 'd':
            cont+=10
            print('Resposta correta. Você ganhou mais 10 pontos!!!')
        else:
            print('Resposta errada')
        a= raw_input ('Digite algo para continuar e s caso queira sair ' )
        if a=='s':
            if cont<=100:
                print('\tVocê fez %d pontos. Pode ser melhor!!!'%cont)
            elif (cont>100 and cont<=140):
                print('\tVocê fez %d pontos. Isto foi bom!!!'%cont)
            elif (cont>140 and cont<=180):
                print('\tVocê fez %d pontos. Parabéns!!!'%cont)
            elif (cont>180 and cont<=200):
                print('\tVocê fez %d pontos. Excelente!!!'%cont)
            cont=0
            print('\tObrigado por jogar!!!')
            break
        os.system('cls')
        print('		***************')
        print('		 Seus pontos:')
        print('		             ')
        print('		    %d        '%cont)
        print('                             ')
        print('		***************')
        print('A sigla BI, significa: ')
        print('a)Better Input')
        print('b)Byte issue')
        print('c)Business Intelligence')
        op=raw_input('d)NDA \n')
        if op== 'c':
            cont+=10
            print('Resposta correta. Você ganhou mais 10 pontos!!!')
        else:
            print('Resposta errada')
        a= raw_input ('Digite algo para continuar e s caso queira sair ' )
        if a=='s':
            if cont<=100:
                print('\tVocê fez %d pontos. Pode ser melhor!!!'%cont)
            elif (cont>100 and cont<=140):
                print('\tVocê fez %d pontos. Isto foi bom!!!'%cont)
            elif (cont>140 and cont<=180):
                print('\tVocê fez %d pontos. Parabéns!!!'%cont)
            elif (cont>180 and cont<=200):
                print('\tVocê fez %d pontos. Excelente!!!'%cont)
            cont=0
            print('\tObrigado por jogar!!!')
            break
        os.system('cls')
        print('		***************')
        print('		 Seus pontos:')
        print('		             ')
        print('		    %d        '%cont)
        print('                             ')
        print('		***************')
        print('MatLab é uma linguagem mais voltada para:')
        print('a)Programar para internet')
        print('b)Funções matemáticas')
        print('c)Programar para celulares')
        op=raw_input('d)NDA \n')
        if op== 'b':
            cont+=10
            print('Resposta correta. Você ganhou mais 10 pontos!!!')
        else:
            print('Resposta errada')
        a= raw_input ('Digite algo para continuar e s caso queira sair ' )
        if a=='s':
            if cont<=100:
                print('\tVocê fez %d pontos. Pode ser melhor!!!'%cont)
            elif (cont>100 and cont<=140):
                print('\tVocê fez %d pontos. Isto foi bom!!!'%cont)
            elif (cont>140 and cont<=180):
                print('\tVocê fez %d pontos. Parabéns!!!'%cont)
            elif (cont>180 and cont<=200):
                print('\tVocê fez %d pontos. Excelente!!!'%cont)
            cont=0
            print('\tObrigado por jogar!!!')
            break
        os.system('cls')
        print('		***************')
        print('		 Seus pontos:')
        print('		             ')
        print('		    %d        '%cont)
        print('                             ')
        print('		***************')
        print('Sobre a função recursiva, é correto afirmar: ')
        print('a)Ela invoca a função principal')
        print('b)Ela é capaz de refazer ações feitas anteriormente em outra função')
        print('c)Ela pode reexecutar o programa a partir daquele ponto')
        op=raw_input('d)NDA \n')
        if op== 'd':
            cont+=10
            print('Resposta correta. Você ganhou mais 10 pontos!!!')
        else:
            print('Resposta errada')
        a= raw_input ('Digite algo para continuar e s caso queira sair ' )
        if a=='s':
            if cont<=100:
                print('\tVocê fez %d pontos. Pode ser melhor!!!'%cont)
            elif (cont>100 and cont<=140):
                print('\tVocê fez %d pontos. Isto foi bom!!!'%cont)
            elif (cont>140 and cont<=180):
                print('\tVocê fez %d pontos. Parabéns!!!'%cont)
            elif (cont>180 and cont<=200):
                print('\tVocê fez %d pontos. Excelente!!!'%cont)
            cont=0
            print('\tObrigado por jogar!!!')
            break
        os.system('cls')
        print('		***************')
        print('		 Seus pontos:')
        print('		             ')
        print('		    %d        '%cont)
        print('                             ')
        print('		***************')
        print('Sobre o servidor DNS, é correto afirmar: ')
        print('a)Possibilita que usuários de computadores clientes usem nomes, ao invés de IPs, para identificar hosts remotos')
        print('b)Ele é capaz de devolver o endereço IP ao cliente que o requisitou')
        print('c)a e b estão corretas')
        op=raw_input('d)a e b estão incorretas \n')
        if op=='c' :
            cont+=10
            print('Resposta correta. Você ganhou mais 10 pontos!!!')
        else:
            print('Resposta errada')
        a= raw_input ('Digite algo para continuar e s caso queira sair ' )
        if a=='s':
            if cont<=100:
                print('\tVocê fez %d pontos. Pode ser melhor!!!'%cont)
            elif (cont>100 and cont<=140):
                print('\tVocê fez %d pontos. Isto foi bom!!!'%cont)
            elif (cont>140 and cont<=180):
                print('\tVocê fez %d pontos. Parabéns!!!'%cont)
            elif (cont>180 and cont<=200):
                print('\tVocê fez %d pontos. Excelente!!!'%cont)
            cont=0
            print('\tObrigado por jogar!!!')
            break
        os.system('cls')
        print('		***************')
        print('		 Seus pontos:')
        print('		             ')
        print('		    %d        '%cont)
        print('                             ')
        print('		***************')
        print('Sobre o Android, pode-se afirmar: ')
        print('a)Roda apenas em celulares LG')
        print('b)Foi baseado no Kernel Linux')
        print('c)Tem o código fechado')
        op=raw_input('d)NDA \n')
        if op== 'b':
            cont+=10
            print('Resposta correta. Você ganhou mais 10 pontos!!!')
        else:
            print('Resposta errada')
        a= raw_input ('Digite algo para continuar e s caso queira sair ' )
        if a=='s':
            if cont<=100:
                print('\tVocê fez %d pontos. Pode ser melhor!!!'%cont)
            elif (cont>100 and cont<=140):
                print('\tVocê fez %d pontos. Isto foi bom!!!'%cont)
            elif (cont>140 and cont<=180):
                print('\tVocê fez %d pontos. Parabéns!!!'%cont)
            elif (cont>180 and cont<=200):
                print('\tVocê fez %d pontos. Excelente!!!'%cont)
            cont=0
            print('\tObrigado por jogar!!!')
            break
        os.system('cls')
        print('		***************')
        print('		 Seus pontos:')
        print('		             ')
        print('		    %d        '%cont)
        print('                             ')
        print('		***************')
        print('É algo comum ao Windows 8, Ubuntu e ao Mac Os')
        print('a)Tem código fechado')
        print('b)Foram criados pela mesma empresa')
        print('c)Tem código aberto')
        op=raw_input('d)São sistemas operacionais \n')
        if op== 'd':
            cont+=10
            print('Resposta correta. Você ganhou mais 10 pontos!!!')
        else:
            print('Resposta errada')
        a= raw_input ('Digite algo para continuar e s caso queira sair ' )
        if a=='s':
            if cont<=100:
                print('\tVocê fez %d pontos. Pode ser melhor!!!'%cont)
            elif (cont>100 and cont<=140):
                print('\tVocê fez %d pontos. Isto foi bom!!!'%cont)
            elif (cont>140 and cont<=180):
                print('\tVocê fez %d pontos. Parabéns!!!'%cont)
            elif (cont>180 and cont<=200):
                print('\tVocê fez %d pontos. Excelente!!!'%cont)
            cont=0
            print('\tObrigado por jogar!!!')
            break
        os.system('cls')
        print('		***************')
        print('		 Seus pontos:')
        print('		             ')
        print('		    %d        '%cont)
        print('                             ')
        print('		***************')
        print('O que é um banco de dados ?')
        print('a)Uma ferramenta que apenas guarda dados')
        print('b)Um livro que guarda dados')
        print('c)Um programa que guarda dados')
        op=raw_input('d)Um sistema que reúne e mantém organizada uma série de informações \n')

        if op=='d' :
            cont+=10
            print('Resposta correta. Você ganhou mais 10 pontos!!!')
        else:
            print('Resposta errada')
        a= raw_input ('Digite algo para continuar e s caso queira sair ' )
        if a=='s':
            if cont<=100:
                print('\tVocê fez %d pontos. Pode ser melhor!!!'%cont)
            elif (cont>100 and cont<=140):
                print('\tVocê fez %d pontos. Isto foi bom!!!'%cont)
            elif (cont>140 and cont<=180):
                print('\tVocê fez %d pontos. Parabéns!!!'%cont)
            elif (cont>180 and cont<=200):
                print('\tVocê fez %d pontos. Excelente!!!'%cont)
            cont=0
            print('\tObrigado por jogar!!!')
            break
        os.system('cls')
        print('		***************')
        print('		 Seus pontos:')
        print('		             ')
        print('		    %d        '%cont)
        print('                             ')
        print('		***************')
        print('A partir do Python 3, o seguinte comando não existe mais: ')
        print('a)input')
        print('b)raw_input')
        print('c)print')
        op=raw_input('d)elif \n')

        if op== 'b':
            cont+=10
            print('Resposta correta. Você ganhou mais 10 pontos!!!')
        else:
            print('Resposta errada')
        a= raw_input ('Digite algo para continuar e s caso queira sair ' )
        if a=='s':
            if cont<=100:
                print('\tVocê fez %d pontos. Pode ser melhor!!!'%cont)
            elif (cont>100 and cont<=140):
                print('\tVocê fez %d pontos. Isto foi bom!!!'%cont)
            elif (cont>140 and cont<=180):
                print('\tVocê fez %d pontos. Parabéns!!!'%cont)
            elif (cont>180 and cont<=200):
                print('\tVocê fez %d pontos. Excelente!!!'%cont)
            cont=0
            print('\tObrigado por jogar!!!')
            break
        os.system('cls')
        print('		***************')
        print('		 Seus pontos:')
        print('		             ')
        print('		    %d        '%cont)
        print('                             ')
        print('		***************')
        print('Na linguagem Python, se declarada uma string= ''abcdefg'', a posição string[-3] é a letra: ')
        print('a)c')
        print('b)f')
        print('c)e')
        op=raw_input('d)Não existe \n') 

        if op== 'c':
            cont+=10
            print('Resposta correta. Você ganhou mais 10 pontos!!!')
        else:
            print('Resposta errada')
        a= raw_input ('Digite algo para continuar e s caso queira sair ' )
        if a=='s':
            if cont<=100:
                print('\tVocê fez %d pontos. Pode ser melhor!!!'%cont)
            elif (cont>100 and cont<=140):
                print('\tVocê fez %d pontos. Isto foi bom!!!'%cont)
            elif (cont>140 and cont<=180):
                print('\tVocê fez %d pontos. Parabéns!!!'%cont)
            elif (cont>180 and cont<=200):
                print('\tVocê fez %d pontos. Excelente!!!'%cont)
            cont=0
            print('\tObrigado por jogar!!!')
            break
        os.system('cls')
        print('		***************')
        print('		 Seus pontos:')
        print('		             ')
        print('		    %d        '%cont)
        print('                             ')
        print('		***************')
        print('Com relação ao Raid 0, é correto afirmar: ')
        print('a)Ele divide os arquivos entre os HDs')
        print('b)Caso um dos HDs do sistema seja danificado, ele é capaz de continuar os processos')
        print('c)Ele copia um HD para outro')
        op=raw_input('d)NDA \n') 
       
        if op== 'a':
            cont+=10
            print('Resposta correta. Você ganhou mais 10 pontos!!!')
        else:
            print('Resposta errada')
        a= raw_input ('Digite algo para continuar e s caso queira sair ' )
        if a=='s':
            if cont<=100:
                print('\tVocê fez %d pontos. Pode ser melhor!!!'%cont)
            elif (cont>100 and cont<=140):
                print('\tVocê fez %d pontos. Isto foi bom!!!'%cont)
            elif (cont>140 and cont<=180):
                print('\tVocê fez %d pontos. Parabéns!!!'%cont)
            elif (cont>180 and cont<=200):
                print('\tVocê fez %d pontos. Excelente!!!'%cont)
            cont=0
            print('\tObrigado por jogar!!!')
            break
        os.system('cls')
        print('		***************')
        print('		 Seus pontos:')
        print('		             ')
        print('		    %d        '%cont)
        print('                             ')
        print('		***************')
        print('Em Matlab, para se apagar as variáveis sendo usadas, é usado o comando:')
        print('a)clc')
        print('b)clear all')
        print('c)clean')
        op=raw_input('d)erase \n') 
       
        if op== 'b':
            cont+=10
            print('Resposta correta. Você ganhou mais 10 pontos!!!')
        else:
            print('Resposta errada')
        a= raw_input ('Digite algo para continuar e s caso queira sair ' )
        if a=='s':
            if cont<=100:
                print('\tVocê fez %d pontos. Pode ser melhor!!!'%cont)
            elif (cont>100 and cont<=140):
                print('\tVocê fez %d pontos. Isto foi bom!!!'%cont)
            elif (cont>140 and cont<=180):
                print('\tVocê fez %d pontos. Parabéns!!!'%cont)
            elif (cont>180 and cont<=200):
                print('\tVocê fez %d pontos. Excelente!!!'%cont)
            cont=0
            print('\tObrigado por jogar!!!')
            break
        os.system('cls')
        print('		***************')
        print('		 Seus pontos:')
        print('		             ')
        print('		    %d        '%cont)
        print('                             ')
        print('		***************')
        print('Em Matlab, ao final do if é necessário: ')
        print('a)else')
        print('b)elif')
        print('c)end')
        op=raw_input('d)NDA \n')

        if op== 'c':
            cont+=10
            print('Resposta correta. Você ganhou mais 10 pontos!!!')
        else:
            print('Resposta errada')
        a= raw_input ('Digite algo para continuar e s caso queira sair ' )
        if a=='s':
            if cont<=100:
                print('\tVocê fez %d pontos. Pode ser melhor!!!'%cont)
            elif (cont>100 and cont<=140):
                print('\tVocê fez %d pontos. Isto foi bom!!!'%cont)
            elif (cont>140 and cont<=180):
                print('\tVocê fez %d pontos. Parabéns!!!'%cont)
            elif (cont>180 and cont<=200):
                print('\tVocê fez %d pontos. Excelente!!!'%cont)
            cont=0
            print('\tObrigado por jogar!!!')
            break
        os.system('cls')
        print('		***************')
        print('		 Seus pontos:')
        print('		             ')
        print('		    %d        '%cont)
        print('                             ')
        print('		***************')
        print('O que é o Git?')
        print('a)Um sistema de controle de versão')
        print('b)Uma linguagem de programação')
        print('c)Um sistema operacional')
        op=raw_input('d)NDA \n')

        if op== 'a':
            cont+=10
            print('Resposta correta. Você ganhou mais 10 pontos!!!')
        else:
            print('Resposta errada')
        a= raw_input ('Digite algo para continuar e s caso queira sair ' )
        if a=='s':
            if cont<=100:
                print('\tVocê fez %d pontos. Pode ser melhor!!!'%cont)
            elif (cont>100 and cont<=140):
                print('\tVocê fez %d pontos. Isto foi bom!!!'%cont)
            elif (cont>140 and cont<=180):
                print('\tVocê fez %d pontos. Parabéns!!!'%cont)
            elif (cont>180 and cont<=200):
                print('\tVocê fez %d pontos. Excelente!!!'%cont)
            cont=0
            print('\tObrigado por jogar!!!')
            break
        os.system('cls')
        print('		***************')
        print('		 Seus pontos:')
        print('		             ')
        print('		    %d        '%cont)
        print('                             ')
        print('		***************')
        print('O comando para se definir uma nova versão em Python é:')
        print('a)fnc')
        print('b)function')
        print('c)def')
        op=raw_input('d)NDA \n') 
       
        if op== 'b':
            cont+=10
            print('Resposta correta. Você ganhou mais 10 pontos!!!')
        else:
            print('Resposta errada')
        a= raw_input ('Digite algo para continuar e s caso queira sair ' )
        if a=='s':
            if cont<=100:
                print('\tVocê fez %d pontos. Pode ser melhor!!!'%cont)
            elif (cont>100 and cont<=140):
                print('\tVocê fez %d pontos. Isto foi bom!!!'%cont)
            elif (cont>140 and cont<=180):
                print('\tVocê fez %d pontos. Parabéns!!!'%cont)
            elif (cont>180 and cont<=200):
                print('\tVocê fez %d pontos. Excelente!!!'%cont)
            cont=0
            print('\tObrigado por jogar!!!')
            break
        os.system('cls')
        print('		***************')
        print('		 Seus pontos:')
        print('		             ')
        print('		    %d        '%cont)
        print('                             ')
        print('		***************')
        print('Em Python, para se ver os atributos de uma variável é necessário o comando:')
        print('a)atrib')
        print('b)list')
        print('c)show')
        op=raw_input('d)dir \n') 
       
        if op== 'd':
            cont+=10
            print('Resposta correta. Você ganhou mais 10 pontos!!!')
        else:
            print('Resposta errada')
        a= raw_input ('Digite algo para continuar e s caso queira sair ' )
        if a=='s':
            if cont<=100:
                print('\tVocê fez %d pontos. Pode ser melhor!!!'%cont)
            elif (cont>100 and cont<=140):
                print('\tVocê fez %d pontos. Isto foi bom!!!'%cont)
            elif (cont>140 and cont<=180):
                print('\tVocê fez %d pontos. Parabéns!!!'%cont)
            elif (cont>180 and cont<=200):
                print('\tVocê fez %d pontos. Excelente!!!'%cont)
            cont=0
            print('\tObrigado por jogar!!!')
            break
        os.system('cls')
        print('		***************')
        print('		 Seus pontos:')
        print('		             ')
        print('		    %d        '%cont)
        print('                             ')
        print('		***************')
        print('O que é o Proxy?')
        print('a)É uma linguagem de programação')
        print('b)É o nome do 1º computador')
        print('c)É o nome de um firewall')
        print('d)NDA')
        op=raw_input('d)NDA \n') 
       
        if op== 'd':
            cont+=10
            print('Resposta correta. Você ganhou mais 10 pontos!!!')
        else:
            print('Resposta errada')
        a= raw_input ('Digite algo para continuar e s caso queira sair ' )
        if a=='s':
            if cont<=100:
                print('\tVocê fez %d pontos. Pode ser melhor!!!'%cont)
            elif (cont>100 and cont<=140):
                print('\tVocê fez %d pontos. Isto foi bom!!!'%cont)
            elif (cont>140 and cont<=180):
                print('\tVocê fez %d pontos. Parabéns!!!'%cont)
            elif (cont>180 and cont<=200):
                print('\tVocê fez %d pontos. Excelente!!!'%cont)
            cont=0
            print('\tObrigado por jogar!!!')
            break
        os.system('cls')
        print('		***************')
        print('		 Seus pontos:')
        print('		             ')
        print('		    %d        '%cont)
        print('                             ')
        print('		***************')
        print('Em python, dado o vetor frase=''abcd'',se dado o comando frase[1::2](no Python Shell), aparecerão as letras')
        print('a)ad')
        print('b)ac')
        print('c)cd')
        op=raw_input('d)bc \n')
       
        if op== 'd':
            cont+=10
            print('Resposta correta. Você ganhou mais 10 pontos!!!')
        else:
            print('Resposta errada')
        a= raw_input ('Digite algo para continuar ' )
        os.system('cls')
       
        if cont<=100:
            print('\tVocê fez %d pontos. Pode ser melhor!!!'%cont)
        elif (cont>100 and cont<=140):
            print('\tVocê fez %d pontos. Isto foi bom!!!'%cont)
        elif (cont>140 and cont<=180):
            print('\tVocê fez %d pontos. Parabéns!!!'%cont)
        elif (cont>180 and cont<=200):
            print('\tVocê fez %d pontos. Excelente!!!'%cont)
        cont=0
        print('\tObrigado por jogar!!!')

elif opcao==5:
	print "Coloque seu codigo aqui"
else:
	print "Encerrando..."
