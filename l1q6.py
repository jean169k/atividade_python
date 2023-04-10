#importa o valor de pi e a função de pontecia (pow) da biblioteca math
from math import pi, pow

#faça um programa que peça o raio de um círculo, mostre sua área.
#área do círculo = 2 * pi * r * r
#entrada
raio_do_círculo = float(input('informe o tamanho do raio do circulo: '))

#processamento
area_do_circulo = 2 * pi * pow(raio_do_círculo,2)

#respota
print('a área do circulo é {:.2f}' .format(area_do_circulo))