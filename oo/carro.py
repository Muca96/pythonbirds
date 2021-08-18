"""
você deve criar uma classe carro que deve possuir
dois atributps compostos por outras duas classes

1 motor
2 direção

omotor tera a responsabilidade de controlar a velocidade.
ele oferece os seguientes atribustos :
1 atributo de dado velocidade
2 metodo acelerar, que devera incrementar em uma unidade.
3 metedo de frear que devera decrementar a velocidade em duas unidadades.
A direção tera responsabilidade de controlar a direçao ela oferece
os seguientes atributos:
1 valor da direçao com valores possíveis : norte , sul , leste , oeste.
2 metodo girar_a_direita
3 metodo girar_a_esquerda
       N
     O   L
       S
     Exemplo:
     #testando motor
     >>> motor = Motor()
     >>> motor.velocidade
     0
     >>> motor.acelerar()
     >>> motor.velocidade
     1
     >>> motor.acelerar()
     >>> motor.velocidade
     2
     >>> motor.acelerar()
     >>> motor.velocidade
     3
     >>> motor.frear()
     >>> motor.velocidade
     1
     >>> motor.frear()
     >>> motor.velocidade
     0
     >>> # testando direção
     >>> direcao = Direcao()
     >>> direcao.valor
     'norte'
     >>> direcao.girar_a_direita()
     >>> direcao.valor
     'leste'
     >>> direcao.girar_a_direita()
     >>> direcao.valor
     'sul'
     >>> direcao.girar_a_direita()
     >>> direcao.valor
     'oeste'
     >>> direcao.girar_a_direita()
     >>> direcao.valor
     'norte'
     >>> direcao.girar_a_esquerda()
     >>> direcao.valor
     'oeste'
     >>> direcao.girar_a_esquerda()
     >>> direcao.valor
     'sul'
     >>> direcao.girar_a_esquerda()
     >>> direcao.valor
     'leste'
     >>> direcao.girar_a_esquerda()
     >>> direcao.valor
     'norte'
     >>> carro = Carro(direcao, motor)
     >>> carro.calcular_velocidade()
     0
     >>> carro.acelerar()
     >>> carro.calcular_velocidade()
     1
     >>> carro.acelerar()
     >>> carro.calcular_velocidade()
     2
     >>> carro.frear()
     >>> carro.calcular_velocidade()
     0
     >>> carro.calcular_direcao()
     'norte'
     >>> carro.girar_a_direita()
     >>> carro.calcular_direcao()
     'leste'
     >>> carro.girar_a_esquerda()
     >>> carro.calcular_direcao()
     'norte'
     >>> carro.girar_a_esquerda()
     >>> carro.calcular_direcao()
     'oeste'

"""

class Carro :
    def __init__(self,direcao,motor):
        self.motor = motor
        self.direcao = direcao
    def calcular_velocidade(self):
        return self.motor.velocidade
    def acelerar(self):
        return self.motor.acelerar()
    def frear(self):
        return self.motor.frear()
    def calcular_direcao(self):
        return self.direcao.valor
    def girar_a_direita(self):
        return  self.direcao.girar_a_direita()
    def girar_a_esquerda(self):
        return self.direcao.girar_a_esquerda()



class Motor:
    def __init__(self):
        self.velocidade = 0
    def acelerar(self):
        self.velocidade += 1
    def frear(self):
        self.velocidade -=2
        self.velocidade = max(0, self.velocidade)
NORTE = 'norte'
LESTE = 'leste'
SUL = 'sul'
OESTE = 'oeste'

class Direcao:
    rotacao_a_direita_dict={
        NORTE : LESTE , LESTE : SUL , SUL : OESTE , OESTE : NORTE

    }
    rotacao_a_esquerda_dict={
        NORTE : OESTE , OESTE : SUL , SUL : LESTE , LESTE : NORTE
    }
    def __init__(self):
        self.valor = 'norte'

    def girar_a_direita(self):
        self.valor = self.rotacao_a_direita_dict[self.valor]

    def girar_a_esquerda(self):
        self.valor = self.rotacao_a_esquerda_dict[self.valor]
