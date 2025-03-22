#desconto inss e ir
lista_salario_bruto = []
lista_salario_liquido = []

while True:
  salario_bruto = float(input('Digite o salário bruto: '))

  if salario_bruto == 0:
    print('Encerrado!')
    break


  #INSS
  if salario_bruto <= 1518:
    inss = salario_bruto * 0.075
  elif salario_bruto > 1518 and salario_bruto <= 2793.88:
    inss = salario_bruto * 0.09
  elif salario_bruto > 2793.88 and salario_bruto <= 4190.83:
    inss = salario_bruto * 0.12
  else:
    inss = salario_bruto * 0.14
  inss = round(inss, 2)

  salario_descontado_inss = salario_bruto - inss
  lista_salario_bruto.append(salario_bruto)

  print(f'Valor a descontar de INSS: R$ {inss}')
  print(f'Valor do salário após desconto de INSS: R$ {salario_descontado_inss}')

  #IR
  if salario_descontado_inss <= 2259.20:
    ir = 0
  elif salario_descontado_inss > 2259.20 and salario_descontado_inss <= 2826.65:
    ir = (salario_descontado_inss * 0.075) - 169.44
  elif salario_descontado_inss > 2826.65 and salario_descontado_inss <= 3751.05:
    ir = (salario_descontado_inss * 0.15) - 381.44
  elif salario_descontado_inss > 3751.05 and salario_descontado_inss <= 4664.68:
    ir = (salario_descontado_inss * 0.225) - 662.77
  else:
    ir = (salario_descontado_inss * 0.275) - 896
  ir = round(ir, 2)

  salario_liquido = salario_descontado_inss - ir
  lista_salario_liquido.append(salario_liquido)


  print(f'Valor a descontar de IR: R$ {ir}')
  print(f'Valor do salário líquido: R$ {salario_liquido}')
  print('\n')

#media salario bruto e liquido
media_salario_bruto = sum(lista_salario_bruto)/len(lista_salario_bruto)
media_salario_liquido = sum (lista_salario_liquido)/len(lista_salario_liquido)

print(f'A media de salario bruto e igual {round(media_salario_bruto, 2)}')
print(f'A media de salario liquido e igual {round(media_salario_liquido, 2)}')