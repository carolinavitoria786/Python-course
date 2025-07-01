"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada.
Ex. Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

pergunta = print('Que horas são? ')
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