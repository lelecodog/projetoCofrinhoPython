def obter_opcao(mensagem):
    while True:
        try:
            opcao = int(input(mensagem))
            return opcao
        except ValueError:
            print("Opção inválida. Por favor, insira um número.")

def obter_valor(mensagem):
    while True:
        try:
            opcao = float(input(mensagem))
            return opcao
        except ValueError:
            print("Opção inválida. Por favor, insira um número.")