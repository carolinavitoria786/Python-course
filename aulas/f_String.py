nome = 'Carolina Vitória'
altura = 1.68
peso = 68
imc = peso / (altura * altura)

linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'pesa {peso} quilos e seu imc é {imc:.2f}'

print(linha_1)
print(linha_2)

# f -> para indicar a formatação da string(f-strings)
# {} -> para adicionar as variaveis e suas respectivas formatações como .2f -> duas casas decimais