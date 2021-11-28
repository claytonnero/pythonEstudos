from funções import *
print('Olá qual é o seu nome?')

nome = pegaNome(resposta())
resp = respondeNome(nome)	
print(resp)
	
while True:
	resposta = input(">: ")
	
	if resposta == 'tchau':
		break
		
print("thau, thau!")