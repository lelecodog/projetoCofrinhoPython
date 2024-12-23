from moedas import Moeda, Dolar, Euro, Cofrinho
from valueError import obter_opcao, obter_valor


cofrinho = Cofrinho()
cofrinho.carregar_moedas("cofrinho.json")
while True:
    print()
    print("----Menu----")
    print("Adicionar moeda  - [1]")
    print("Remover moeda    - [2]")
    print("Listar moedas    - [3]")
    print("Total convertido - [4]")
    print("Sair             - [0]")

    op = obter_opcao("Selecione uma opção: ")

    if op == 0:
        print("Finalizando...")
        #Salvar as moedas no arquivo antes de sair
        cofrinho.salvar_moedas("cofrinho.json")
        break

    elif op == 1:
        while True:
            print("----MENU----")
            print("Dolar - [1]")
            print("Euro  - [2]")
            print("Retornar - [0]")
            op_moeda = obter_opcao("Qual moeda deseja adicionar ao cofrinho: ")

            if op_moeda == 0:
                break

            if op_moeda not in [1, 2]:
                print("Opção inválida, digite 1 para Dolar ou 2 para Euro")
                continue

            valor = obter_valor("Qual o valor da moeda: ")
            if op_moeda == 1:
                newMoeda = Dolar(valor)
                cofrinho.adiciona_moeda(newMoeda)
                break

            if op_moeda == 2:
                newMoeda = Euro(valor)
                cofrinho.adiciona_moeda(newMoeda)
                break

            else:
                print("Opção inválida!")

    elif op == 2:
        while True:
            print("----MENU----")
            print("Dolar  - [1]")
            print("Euro   - [2]")
            print("Retornar - [0]")
            op_moeda = obter_opcao("Qual moeda deseja remover do cofrinho: ")

            if op_moeda == 0:
                break

            if op_moeda not in [1, 2]:
                print("Opção inválida, digite 1 para Dolar ou 2 para Euro")
                continue

            valor = obter_valor("Qual o valor da moeda: ")
            if op_moeda == 1:
                newMoeda = Dolar(valor)
                cofrinho.remover_moedas(newMoeda)
                break

            if op_moeda == 2:
                newMoeda = Euro(valor)
                cofrinho.remover_moedas(newMoeda)
                break

            else:
                print("Opção inválida!")

    elif op == 3:
        cofrinho.listar_moedas()

    elif op == 4:
        cofrinho.total_convertido()

    else:
        print("Opção inválida!")



