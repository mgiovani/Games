#encoding: utf-8


print "\t        ─▄▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▄─ "
print "\t         █░░░█░░░░░░░░░░▄▄░██░█ "
print "\t         █░▀▀█▀▀░▄▀░▄▀░░▀▀░▄▄░█ "
print "\t         █░░░▀░░░▄▄▄▄▄░░██░▀▀░█"
print "\t        ─▀▄▄▄▄▄▀─────▀▄▄▄▄▄▄▀─"

opcao=input ("\n\n\t\tSelecione o jogo desejado: \n\t\t1-Jogo da Velha \n\t\t2-Jokenpô \n\t\t3-Par ou Impar \n\t\t4-Quiz \n\t\t5-Sobre \n\t\t6-Sair\n\n")

#os.system(['clear','cls'][os.name == 'nt'])
if opcao==1:
	print "Coloque seu codigo aqui";
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
                    'PC:',jg2
	
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
	print "Coloque seu codigo aqui"
elif opcao==5:
	print "Coloque seu codigo aqui"
else:
	print "Encerrando..."
