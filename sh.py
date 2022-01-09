nome = str(input('Digite o nome do funcionario: '))
fun = str(input('Diga a função do funcionario {} : '.format(nome)))
valoh = float(input('Senhor {} qual o valor que o senhor recebe por hora R$ '.format(nome)))
ht = float(input('Diga quantas horas voce trabalha por mes senhor {} H: '.format(nome)))

cal = valoh * ht

print('Senhor {} voce receberá cerca de R$ {:.2f} no mes .'.format(nome, cal))
