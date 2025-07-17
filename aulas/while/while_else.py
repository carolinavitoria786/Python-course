""" while/else """

string = 'Valorqualquer'

i = 0

while i < len(string):
    letra = string[i]
    
    if letra == ' ':
        break
    
    print(letra)
    i += 1
else:                                           # else so é e excutado após a execução de todo o while
    print('Não encontrei um espaço na string.')
print('Fora do while.')