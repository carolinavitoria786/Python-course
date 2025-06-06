"""
Interpolação básica de strings
s - string
d e i - int 
f - float
x e X - Hexadecimal (ABCDEF0123456789)
. <número de dígitos>f
(Caractere)(><^)( quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a
"""

nome = 'Carolina'
preco = 1000.95897643
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %x' % (15,15))

#-------------------------------------------------------------------------------------#

variavel_pad = 'ABC'
print(f'{variavel_pad}')
print(f'{variavel_pad:*>10}')
print(f'{variavel_pad:*<10}')
print(f'{variavel_pad:*^10}')
print(f'{1000.4873648123746:0=+10,.1f}')
print(f'O hexadecimal de 1500 é {1500:08x}')