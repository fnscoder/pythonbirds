class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.idade = idade
        self.nome = nome

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    p = Pessoa()
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)
    print(p.idade)
    p.nome = 'Felipe'
    p.idade = 35
    print(p.nome)
    print(p.idade)
