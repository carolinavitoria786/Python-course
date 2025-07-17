""" Calculadora com while """
# .lower() serve para que o caractere informado seja minusculo
# startswhith serve para verificar com que caractere começa a entrada fornecida 


while True :
    
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite um número: ')
    operador = input('Digite o operador(+-/*): ')
    
    numeros_validos = None
    num_1_float = 0                                 #definição de variavel fora do bloco
    num_2_float = 0
    
    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None
        
    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos.')
        continue
    
    opreradores_permitidos = '+-/*'
    
    if operador not in opreradores_permitidos:
        print('Operador inválido.')
        continue
    
    if len(operador) > 1:                           #para que o programa aceite apenas um operador
        print('Digite apenas um operador.')
        continue        
    
    print('Realizando sua conta. Confira o resultado abaixo: ')
    if operador == '+':
        print(num_1_float + num_2_float)
    elif operador == '-':
        print(num_1_float - num_2_float)
    elif operador == '/':
        print(num_1_float / num_2_float)
    elif operador == '*':
        print(num_1_float * num_2_float)
    else:
        print('Press F to pay respect ;-;') 
        
    sair = input('Quer sair? [s]im: ').lower().startswith('s')
    
    if sair is True:
        break