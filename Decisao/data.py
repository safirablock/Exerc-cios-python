# Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

dia = int(input('Dia (dd): '))
mes = int(input('Mês (mm): '))
ano = int(input('Ano (aaaa): '))

valido = False

if (mes == 1) or (mes == 3) or (mes == 5) or (mes == 7) or (mes == 8) or (mes == 10) or (mes == 12):
    if (dia <= 31):
        valido = True
elif ((mes == 2)): 
    if((ano % 4 == 0 and ano % 100 != 0) or (ano % 4 == 0 and ano % 400 == 0)):
        if(dia<=29):
            valido = True
    elif(dia<=28):
        valido = True
elif (mes == 4) or (mes == 6) or (mes == 9) or (mes == 11):
    if (dia <= 30):
         valido = True

if(valido):
    print('Data válida')
else:
    print('Data inválida')