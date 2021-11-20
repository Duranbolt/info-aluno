estudante=1
while (estudante>=1):
    print('Insira os dados do estudante ',estudante)
    mat=int(input(' Insira sua matrícula: \n'))
    name=input(' Insira seu nome: \n')
    print('Se não houve realização de alguma prova de recuperação, por favor insira o valor 0')
    av1=int(input(' Insira sua nota na AV1: \n'))
    av2=int(input(' Insira sua nota na AV2: \n'))
    av3=int(input(' Insira sua nota na AV3: \n'))
    avd=int(input(' Insira sua nota na AVD: \n'))
    avds=int(input(' Insira sua nota na AVDS: \n'))
    email=input(' Insira seu email: \n')
    endereco=input(' Insira seu endereço: \n')
    campus=input(' Insira qual seu campus: \n')
    periodo=int(input(' Insira em qual período você está: \n'))

    if avd<avds:
        if av1<av3:
            imedia = (av3+av2+avds)/3
        elif av2<av3:
            imedia = (av1+av3+avds)/3
        else:
            imedia = (av1+av2+avds)/3        
    else:
        if av1<av3:
            imedia = (av3+av2+avd)/3        
        elif av2<av3:
            imedia = (av1+av3+avd)/3
        else:
            imedia = (av1+av2+avd)/3

    media = "{:.1f}".format(imedia)

    print('Matrícula: ',mat)
    print('Nome: ',name)
    print('Nota da AV1: ',av1)
    print('Nota da AV1: ',av2)
    if av3== 0:
        print('A AV3 foi sinalizada com valor 0 pois não precisou ser realizada')
    else:
        print('Nota da AV3: ',av3)
    print('Nota da AVD: ',avd)
    if avds==0:
        print('A AVDS foi sinalizada com valor 0 pois não precisou ser realizada')
    else:
        print('Nota da AVDS: ',avds)
    print('Email: ',email)
    print('Email: ',endereco)
    print('Campus: ',campus)
    print('Período: ',periodo)

    if imedia<6:
        print('Sua média é ', media,'e por isso infelizmente você não passou de ano!')
    else:    
        print('Sua média é ', media,'e por isso você passou de ano!')
    
    estudante=estudante+1