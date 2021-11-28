# -*- coding: utf-8 -*-
from time import sleep
from os import system
system('clear')
class Carro:
    def __init__(self):
        self.cor = 'azul'
        self.rodas = 4
        self.marca = 'chevrolet'
        self.gasolina = 15
    def abastecer(self,valor):
        self.valor = valor 
        self.gasolina += self.valor
veiculo = Carro()
print('Espacificações do carro\n')
print('Cor:',veiculo.cor)
print('Rodas:',veiculo.rodas)
print('Marca:',veiculo.marca)
print('Gasolina:',veiculo.gasolina)
print('\nNovo carro')
veiculo.cor = 'Rosa'
veiculo.rodas = 4
veiculo.marca = 'Honda'
veiculo.gasolina = 60
print('Especificações do carro\n')
print('Cor:',veiculo.cor)
print('Rodas:',veiculo.rodas)
print('Marca:',veiculo.marca)
print('Gasolina:',veiculo.gasolina)
enche_gasolina = input('Vai encher a gasolina ? ')
if enche_gasolina == 'sim':
    valor_gasolina = int(input('Vai colocar quanto de gasolina ? '))
    print('Enchendo tanque..')
    sleep(3)
    veiculo.abastecer(valor_gasolina)
    print('Gasolina atual:',veiculo.gasolina)
