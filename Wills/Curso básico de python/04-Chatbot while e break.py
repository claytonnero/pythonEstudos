##aula 2
# feito na aula 1
print('Olá qual é o seu nome?')
nome = input('>: ')

#feito na aula 2
if "o meu nome eh " in nome:
	nome = nome[14:]

if nome == "Clayton":
	print("E Aí ({})!".format(nome))
else:
	print("Muito Prazer {}!".format(nome))
	# feito na aula 1
while True:
	resposta = input(">: ")
	if resposta == 'tchau':
		break
print("thau, thau!")