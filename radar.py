km_medido = float(input('Digite o km do carro ao passar o radar: '))

limite_velocidade = 80
multa = (km_medido - limite_velocidade) * 20


if km_medido > 80:
    nome_infrator = input('Digite o nome completo do meliante: ').upper()
    placa_infrator = input('Digite a placa do meliante: ')
    print(f' {nome_infrator}, PLACA {placa_infrator}, você foi multado por dirigir a {km_medido}km \n Sua multa devida é de R${multa} reais \n Continue assim que Deus te dará um poste ')
else:
    print(f'Dirija com segurança.') 