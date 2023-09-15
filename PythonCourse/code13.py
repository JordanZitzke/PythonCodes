# Formatação de strings f-strings

nome = 'Jordan Pinho'
altura = 1.73
peso = 71.40

imc = peso / altura ** 2

# Na linha abaixo 'f' é utilizado para formatar a string, enquanto que o ':.2f' 
# representa o número de casas decimais 
 
linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'pesa {peso:.2f} Kg e seu imc é: {imc:.2f}'


# print (nome + " tem " + str(altura) +", pesa " + str(peso) + " e seu IMC é: " + str(imc))
print(linha_1, linha_2)