"""18. Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps),
calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos)."""
#1 MB = 1Mbps 8,3886
tamanho_do_download = float(input('Digite o tamanho do download em MB: '))
velocidade_do_link_de_internet = float(input('Digite a velocidade do link em Mbps: '))
convert =velocidade_do_link_de_internet
convert2 = convert / velocidade_do_link_de_internet
convert3 = convert / 60
print('São necessarios {:.2f} min para completar o download'.format(convert3))