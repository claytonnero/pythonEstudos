import json

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
		self.frases = {"oi" : "Olá qual é o seu nome?", 'tchau' : 'tchau'}
		
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
			return "Aprendido tá ok!"

		if frase == "listar":
			return self.frases

		if frase == "help":
			return ['oi', 'aprende', 'listar', 'tchau', 'help']

		if frase == "ajuda":
			return ['oi', 'aprende', 'listar', 'tchau', 'help']


		if frase == 'tchau':
			return 'tchau'

		if frase in self.frases:
			return self.frases[frase]

		if self.histórico[-1] == "Olá qual é o seu nome?":
			nome = self.pegaNome(frase)
			frase = self.respondeNome(nome)
			return frase

		#aula usando python em um programa python
		try:
			resp = eval(frase)
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
		print(frase)
		self.histórico.append(frase)
