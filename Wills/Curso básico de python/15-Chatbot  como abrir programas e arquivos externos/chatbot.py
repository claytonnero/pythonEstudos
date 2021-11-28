import json
import sys
import os
import subprocess as s

comandos_bot = ['/start', 'aprende', '/listar', 'tchau', '/help']

class Chatbot():

	def __init__(self, nome):

		try:
			memória = open(nome+".json", "r")

		except FileNotFoundError:
			mem = open(nome+".json", "w")
			mem.write('["Clayton", "will"]')
			mem.close()
			memória = open(nome+".json", "r")
			
		self.nome = nome
		self.conhecidos = json.load(memória)
		memória.close()
		self.histórico = []
		self.frases = {"/start" : "Olá qual é o seu nome?", 'tchau' : 'tchau amigo! volte depois pra prosearmos novamente! '}
		
	def escuta(self):

		#captura a resposta do usuário e pré-processa a resposta
		frase = input('>: ')
		frase = frase.lower()
		frase = frase.replace('é', 'eh', 1)
		return frase
            
	def pensa(self, frase):
		
		if frase == "aprende":
			chave = input("O que quer ensinar?: ")
			valor = input("Diga a resposta: ")
			self.frases[chave] = valor
			memória = open(self.nome+".json", "w")
			json.dump(self.frases, memória)
			memória.close()
			return "Aprendido tá ok!"

		if frase == "/listar":
			return self.frases

		if frase == "/help":
			return comandos_bot

		if frase == "ajuda":
			return comandos_bot


		if frase == 'tchau':
			return self.frases['tchau']

		if frase in self.frases:
			return self.frases[frase]

		if self.histórico[-1] == "Olá qual é o seu nome?":
			nome = self.pegaNome(frase)
			frase = self.respondeNome(nome)
			return frase

		#aula usando python em um programa python
		try:
			resp = str(eval(frase))
			return resp

		except:
			pass

		return "Não Entendí"
     
	def pegaNome(self, nome):
		if "o meu nome eh" in nome:
			nome = nome[14:]
		if "eu me chamo " in nome:
			nome = nome[11:]
		nome = nome.title()	
		return nome

	def respondeNome(self, nome):	
		if nome in self.conhecidos:
			frase = "E Aí "
		else:
			frase = "Muito Prazer "
			self.conhecidos.append(nome)
			memória = open(self.nome+".json", "w")
			json.dump(self.conhecidos, memória)
			memória.close()
			
		return frase+"{}!".format(nome)
            
	def fala(self, frase):
		if "executa " in frase:
			plat = sys.platform
			comando = frase.replace('executa', '')
			
			if 'win' in plat:
				os.startfile(comando)
				
			if 'linux' in plat:
				
				try:
					
					s.Popen(comando)
					
				except FileNotFoundError:
                                        s.Popen(['xdg-open', comando])
                                        #os.system('xdg-open {}'.format(comando)) 
		else:
			print(frase)
		self.histórico.append(frase)
