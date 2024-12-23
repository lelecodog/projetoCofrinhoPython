from abc import ABC, abstractmethod
import json

class Moeda(ABC):
    def __init__(self, valor: float):
        self.valor = valor
    @abstractmethod
    def info(self):
        pass
    @abstractmethod
    def converter(self):
        pass

    # metodo para verificar se moeda escolhida para remoção é igual a moeda adicionada
    def __eq__(self, other):
        return self.valor == other.valor and self.__class__ == other.__class__

    # Converter a instancia de Moeda para um dicionario para ser lido em JSON
    def to_dict(self):
        return {"tipo": self.__class__.__name__, "valor": self.valor}

class Dolar(Moeda):
    def __init__(self, valor: float):
        super().__init__(valor)
    def converter(self):
        valorConvertido = self.valor * 6
        return valorConvertido
    def info(self):
        return f"Dolar: {self.valor}"

    def __str__(self):
        return f"Dolar com valor de {self.valor} USD"

class Euro(Moeda):
    def __init__(self, valor: float):
        super().__init__(valor)
    def converter(self):
        valorConvertido = self.valor * 6.5
        return valorConvertido
    def info(self):
        return f"Euro: {self.valor}"

    def __str__(self):
        return f"Euro com valor de {self.valor} EUR"

class Cofrinho:
    def __init__(self):
        self.moedas = []

    def adiciona_moeda(self, moeda: Moeda):
        self.moedas.append(moeda)
        print("Moeda adicionada: ", moeda.info())

    def listar_moedas(self):
        for moeda in self.moedas:
            print(moeda.info())

    def remover_moedas(self, moeda: Moeda):
        if moeda in self.moedas:
            self.moedas.remove(moeda)
            print("Moeda removida: ", moeda.info())
        else:
            print("Moeda não encontrada")

    def total_convertido(self):
        total = sum(moeda.converter() for moeda in self.moedas)
        print(f"Total convertido do cofrinho é de: {total:.2f} Reais")

    def salvar_moedas(self, arquivo): #Salva moedas em arquivo JSON
        with open(arquivo, "w") as f:
            for moeda in self.moedas:
                f.write(json.dumps(moeda.to_dict()) + "\n")

    def carregar_moedas(self, arquivo): #Carregar moedas salvas
        try:
            with open(arquivo, "r") as f:
                for linha in f:
                    moeda_dict = json.loads(linha)
                    if moeda_dict["tipo"] == "Dolar":
                        self.moedas.append(Dolar(moeda_dict["valor"]))
                    elif moeda_dict["tipo"] == "Euro":
                        self.moedas.append(Euro(moeda_dict["valor"]))
        except FileNotFoundError:
            print("Arquivo de moedas não encontrado, iniciando com um cofrinho vazio")



