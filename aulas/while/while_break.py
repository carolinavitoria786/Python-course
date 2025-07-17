"""
Repetições 
while(enquanto)
Executa uma ação enquanto uma condição for verdadeira
"""
"""
Operadores de atribuição
= += -= *= /= //= **= %=
"""
contador = 0 

while contador <= 10: 
    contador = contador + 1
    print(contador)
    
print('Acabou')

#-----Ex.: while, continue e break----------------#

contador = 0 

while contador <= 100:
    contador += 1
    
    if contador == 6:
        print('Não vou mostrar o 6.')
        continue                          #faz com que o programa continue ou seja retorna ao começo do programa para que continue sendo executado
    
    if contador >= 10 and contador <= 27:
        print('Não vou mostrar o', contador)
        continue
    
    print(contador)
    if contador == 40:
        break 

    print('Acabou')
    
#------------while dentro de while----------------#

qtd_linha = 5
qtd_coluna = 5

linha = 1 
while linha <= qtd_coluna:
    coluna = 1
    while coluna <= qtd_coluna:
        print(f'{linha=}{coluna=}')
        coluna += 1
    linha += 1
    
print('Acabou')