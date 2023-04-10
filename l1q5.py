#faça um programa que converta metros para centímetros 
#1m tem 100cm
#entrada
temanho_em_metros = float(input('digite o tamanho em metros: '))

#cálculo
tamanho_em_centimetros = temanho_em_metros *100

#exibir
print('{} metros é igual a {:.0f} centimetros'. format(temanho_em_metros,tamanho_em_centimetros))