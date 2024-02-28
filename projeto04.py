codigo = input("Qual o codigo do seu produto:\n[1] cachorro-Quente\n[2] X-Salada\n[3] X-Bacon\n[4] Torrada\n[5] Refrigerante\nDigite AQUI: ")

cachorro_quente = 4.00
x_salada = 4.50
x_bacon = 5.00
torrada = 2.00
refri = 1.50


if codigo == '1':
    print('Você escolheu cachorro quente ')
    quant = float(input('Quantos vc quer?\n'))
    print('O valor a ser pago é R$',quant*cachorro_quente)

elif codigo == '2':
    print('Você escolheu o X-salada')
    quant = float(input('Quantos vc quer?\n'))
    print('O valor a ser pago é R$',quant*x_salada)

elif codigo == '3':
    print('Você escolheu X-Bacon')
    quant = float(input('Quantos vc quer?\n'))
    print('O valor a ser pago é R$',quant*x_bacon)

elif codigo == '4':
    print('Você escolheu torrada')
    quant = float(input('Quantos vc quer?\n'))
    print('O valor a ser pago é R$',quant*torrada)

elif codigo == '5':
    print('Você escolheu o refrigerante')
    quant = float(input('Quantos vc quer?\n'))
    print('O valor a ser pago é R$',quant*refri)