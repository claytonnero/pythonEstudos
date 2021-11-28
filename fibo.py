def fib(limite):
	anterior = 0
	atual = 0
	for i in int(limite):
		anterior = i - 1
		atual = i
		atual += anterior
	return atual

fi = fib(50)
print(fi)
		