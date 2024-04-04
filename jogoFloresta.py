print("Você está em uma floresta e precisa escolher um caminho para seguir.")
escolha_caminho = input("Você quer seguir o caminho da esquerda ou da direita? (esquerda/direita): ")
if escolha_caminho == "esquerda":
    decisao_rio = input("Você encontrou um rio. Deseja tentar atravessá-lo? (sim/não): ")
    if decisao_rio == "sim":
        print("Você tentou atravessar o rio, mas foi arrastado pela correnteza. Fim de jogo!")
    else:
        print("Você decidiu não atravessar o rio. Parabéns, você escapou com segurança!")
elif escolha_caminho == "direita":
    decisao_montanha = input("Você encontrou uma montanha. Deseja subi-la? (sim/não): ")
    if decisao_montanha == "sim":
        print("Você subiu a montanha e avistou um belo panorama. Parabéns, você conseguiu!")
    else:
        print("Você decidiu não subir a montanha. Infelizmente, você se perdeu na floresta. Fim de jogo!")
else:
    print("Opção inválida. Você se perdeu na floresta. Fim de jogo!")
