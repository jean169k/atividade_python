#faça um programa que peça as 4 notas bimestrais e mostre a media.
# soamr as 4 notas dividir por 4
nota1 = float(input('digite a primeira nota: '))
nota2 = float(input('digite a segunda nota: '))
nota3 = float(input('digite a terceira nota: '))
nota4 = float(input('digite a quanta nota: '))

#cálculo da média
media = (nota1 + nota2 + nota3 + nota4) / 4

#exibir o resultado
print('a média da {} {} {} {} notas é {:,2f}'.format(nota1, nota2, nota3
, nota4, media))
