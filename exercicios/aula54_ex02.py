"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada.
Ex. Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

pergunta = print('Que horas são (utilize este formato: 00:00? ')
hora = int(input())
minutos = int(input())
try:
    if hora and minutos:
        valor = f'{hora:02d}:{minutos:02d}' #02d é a formatação para os numeros inteiros
    if hora >= 1 and hora <= 11 :
        print(f'Boa dia! {valor}')
    if hora >= 12 and hora <= 17 :
        print(f'Bom tarde! {valor}')
    if hora >= 18 and hora <= 23 :
        print(f'Boa noite! {valor}')
except:
    print('Formato de hora não aceito!')
    
    
#-----------Solução apresentada no curso------------#
entrada = input('Digite a hora em números inteiros: ')

try:
    hora = int(entrada)
    if hora >= 0 and hora <= 11:
        print('Bom dia')
    elif hora >= 12 and hora <= 17:
        print('Boa tarde')
    elif hora >= 18 and hora <=23:
        print('Boa noite')
    else:
        print('Não conheço essa hora')
except:
    print('Por favor, digite apenas números inteiros')
        