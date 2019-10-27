"""
Você deve criar uma classe carro que vai possuir
dois atributos compostos por outras duas classes:

Motor
Direção
O Motor terá a responsabilidade de controlar a velocidade.
Ele oferece os seguintes atributos:

Atributo de dado velocidade
Método acelerar, que deverá incremetar a velocidade de uma unidade
Método frear que deverá decrementar a velocidade em duas unidades
A Direção terá a responsabilidade de controlar a direção. Ela oferece
os seguintes atributos:

Valor de diração com valores possíveis: Norte, Sul, Leste, Oeste.
Método girar_a_direita
Método girar_a_esquerda

       N
    O     L
       S

Exemplo:
    # Testando motor
    motor = Motor()
    motor.velocidade
    0
    motor.acelerar()
    motor.velocidade
    1
    motor.acelerar()
    motor.velocidade
    2
    motor.acelerar()
    motor.velocidade
    3
    motor.frear()
    motor.velocidade
    1
    motor.frear()
    motor.velocidade
    0
    # Testando Direcao
    direcao = Direcao()
    direcao.valor
    'Norte'
    direcao.girar_a_direita()
    direcao.valor
    'Leste'
    direcao.girar_a_direita()
    direcao.valor
    'Sul'
    direcao.girar_a_direita()
    direcao.valor
    'Oeste'
    direcao.girar_a_direita()
    direcao.valor
    'Norte'
    direcao.girar_a_esquerda()
    direcao.valor
    'Oeste'
    direcao.girar_a_esquerda()
    direcao.valor
    'Sul'
    direcao.girar_a_esquerda()
    direcao.valor
    'Leste'
    direcao.girar_a_esquerda()
    direcao.valor
    'Norte'
    carro = Carro(direcao, motor)
    carro.calcular_velocidade()
    0
    carro.acelerar()
    carro.calcular_velocidade()
    1
    carro.acelerar()
    carro.calcular_velocidade()
    2
    carro.frear()
    carro.calcular_velocidade()
    0
    carro.calcular_direcao()
    'Norte'
    carro.girar_a_direita()
    carro.calcular_direcao()
    'Leste'
    carro.girar_a_esquerda()
    carro.calcular_direcao()
    'Norte'
    carro.girar_a_esquerda()
    carro.calcular_direcao()
    'Oeste'
"""

class Motor:
    def __init__(self, velocidade=0):
        self.velocidade = velocidade

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade = self.velocidade - 2 if self.velocidade >= 2 else 0


class Direcao:
    def __init__(self, valor='Norte'):
        self.valor = valor

    def girar_a_direita(self):
        direcoes = {
            'Norte': 'Leste',
            'Leste': 'Sul',
            'Sul': 'Oeste',
            'Oeste': 'Norte'
        }
        self.valor = direcoes[self.valor]

    def girar_a_esquerda(self):
        direcoes = {
            'Norte': 'Oeste',
            'Oeste': 'Sul',
            'Sul': 'Leste',
            'Leste': 'Norte'
        }
        self.valor = direcoes[self.valor]

class Carro:
    def __init__(self):
        self.motor = Motor()
        self.direcao = Direcao()


if __name__ == '__main__':
    c = Carro()
    print('acelerando')
    c.motor.acelerar()
    print(c.motor.velocidade)
    c.motor.acelerar()
    print(c.motor.velocidade)
    c.motor.acelerar()
    print(c.motor.velocidade)

    print('freando')
    c.motor.frear()
    print(c.motor.velocidade)
    c.motor.frear()
    print(c.motor.velocidade)
    c.motor.frear()
    print(c.motor.velocidade)
    c.motor.acelerar()
    print(c.motor.velocidade)

    print('girando a direita')
    print(c.direcao.valor)
    c.direcao.girar_a_direita()
    print(c.direcao.valor)
    c.direcao.girar_a_direita()
    print(c.direcao.valor)
    c.direcao.girar_a_direita()
    print(c.direcao.valor)
    c.direcao.girar_a_direita()
    print(c.direcao.valor)

    print('girando a esquerda')
    print(c.direcao.valor)
    c.direcao.girar_a_esquerda()
    print(c.direcao.valor)
    c.direcao.girar_a_esquerda()
    print(c.direcao.valor)
    c.direcao.girar_a_esquerda()
    print(c.direcao.valor)
    c.direcao.girar_a_esquerda()
    print(c.direcao.valor)
