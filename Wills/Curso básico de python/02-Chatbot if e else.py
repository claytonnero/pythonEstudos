#o print é o comando que imprime dados na tela
print('Olá qual é o seu nome?')

#o input é o comando que espera a entrada do usuário, e atribui a variável nome!
nome = input('>: ')

#aqui uma novidade, o comando if compara se a variável nome é exatamente igual a string "Clayton"
if nome == "Clayton":
	
	#caso seja! imprime mensagem intima de conhecido! e o chama pelo nome!
	print("E Aí ({})".format(nome))

#caso a string nao seja "Clayton"
else:
	
	#imprime mensagem de boas vindas e de satisfaçao em conhecê-lo!
	print("Muito Prazer {} seja bem vindo!".format(nome))