class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=None):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nomes_e_atributos_da_classe(cls):
        return f'Classe: {cls} - olhos {cls.olhos}'


class Homem(Pessoa):
    pass


if __name__ == '__main__':
    lucas = Pessoa(nome='Lucas')
    anna = Pessoa(nome='Anna')
    pedro = Pessoa(nome='Pedro')
    felipe = Homem(lucas, anna, pedro, nome='Felipe')
    print(Pessoa.cumprimentar(felipe))
    print(id(felipe))
    print(felipe.cumprimentar())
    print(felipe.nome)
    print(felipe.idade)
    for filho in felipe.filhos:
        print(filho.nome)
    felipe.sobrenome = 'Souza'
    print(felipe.sobrenome)
    print(felipe.__dict__)
    print(lucas.__dict__)
    del felipe.sobrenome
    print(felipe.__dict__)
    print(Pessoa.olhos)
    print(felipe.olhos)
    felipe.olhos = 1
    print(felipe.__dict__)
    print(anna.olhos)
    print(id(Pessoa.olhos), id(pedro.olhos), id(felipe.olhos))
    print(Pessoa.metodo_estatico(), felipe.metodo_estatico())
    print(Pessoa.nomes_e_atributos_da_classe(), felipe.nomes_e_atributos_da_classe())
    pessoa = Pessoa()
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(felipe, Pessoa))
    print(isinstance(felipe, Homem))
