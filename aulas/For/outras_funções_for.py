"""
O que foi aprendido com while também funciona no for (continue, break, else, etc)
"""

for i in range(10):                                 #informando apenas o fim neste range
    if i == 2:
        print('i é 2, pulando...')
        continue                                    #continue faz com que retorne ao começo do laço
    
    if i == 8:
        print('i é 8, seu else não executará')
        break                                       #break encerra o codigo 
    
    for j in range(1,3):                            #neste caso tendo "i" como linhas e "j" como colunas o range percorre de 1 a 2
        print(i, j)
else:                                               #o bloco for sendo completo o else será executado
    print('For completo com sucesso!')               