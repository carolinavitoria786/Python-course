"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
"""

primeiroNome = input('Digite seu primeiro nome: ')
valor = (len(primeiroNome))
try:
    if valor <= 4:
        print('Seu nome é curto')
    if valor >= 5 and valor <= 6:
        print('Seu nome é normal')
    if valor > 6 :
        print('Seu nome é muito grande')
except:
    print('Nome não aceito')