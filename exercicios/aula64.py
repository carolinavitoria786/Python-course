"""
Iteração de String com while
"""

nome = input('Digite seu nome: ')

while nome :
    tamanho = len(nome)
    print(tamanho)
    print(f'{nome}')
    break

#---------resolução do exercicio---------# 

indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}' # *C*a*r*o*l*i*n*a* *V*i*t*ó*r*i*a
    indice += 1

novo_nome += '*'  # acrescenta o asteristico que falta no final da string  
print(novo_nome)
