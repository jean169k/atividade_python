#faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
#calcule e mostre o total do seu salário no referido mês 

#entrada 
valor_hora_trabalho = float (input('Qual o valor da hora de trabalho: '))
quantidade_horas_trabalhadas = float (input ('Qual a quantidade de horas trabalhadas: '))

#processamento 
salario_mensal = valor_hora_trabalho * quantidade_horas_trabalhadas

#saída 
print ('O valor do salário mensal é: {}'. format(salario_mensal))
