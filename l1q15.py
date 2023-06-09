"""Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês,
 sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
    ◦ salário bruto.
    ◦ quanto pagou ao INSS.
    ◦ quanto pagou ao sindicato.
    ◦ o salário líquido.
    ◦ calcule os descontos e o salário líquido, conforme a tabela abaixo:
      + Salário Bruto : R$
      - IR (11%) : R$
      - INSS (8%) : R$
      - Sindicato ( 5%) : R$
      = Salário Liquido : R$
      Obs.: Salário Bruto - Descontos = Salário Líquido."""
#entrada
ganho_por_hora = float(input('Digite quanto você ganha por hora: '))
horas_por_mes = float(input('Digite quantas horas você trabalha por mês: '))

#processamento
salario_bruto = ganho_por_hora * horas_por_mes * 30
imposto_de_renda = salario_bruto - (11/100 * salario_bruto)
inss = salario_bruto - (8/100 * salario_bruto)
sindicato = salario_bruto - (5/100 * salario_bruto)
salario_liquido = salario_bruto -((11/100 * salario_bruto)+ (8/100 * salario_bruto) + (5/100 * salario_bruto))

#saida
print('+ Salário Bruto : R${:.2f}'.format(salario_bruto)) 
print('- IR (11%) : R${:.2f}'.format(imposto_de_renda))
print(' - INSS (8%) : R${:.2f}'.format(inss))
print('- Sindicato ( 5%) : R${:.2f}'.format(sindicato))
print('= Salário Liquido : R${:.2f}'.format(salario_bruto))