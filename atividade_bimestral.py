
                    ## funções ##

def submenus():
    
    print()
    print('--------------------------------')
    print('1. Listar todos')
    print('2. Listar um elemento específico')
    print('3. Incluir')
    print('4. Alterar')
    print('5. Excluir')
    print('6. Sair')
    print('--------------------------------')
    
def clientes_fun(clientes, listinha_dados):

    teste = True
    resposta_submenus = 0


    while resposta_submenus != 6 :
        
        submenus()

        print()
        resposta_submenus = int(input('Escolha uma opção: '))

        if resposta_submenus == 6:
            return()

        if resposta_submenus == 1:
            
            print()
            cpf = input('CPF: ')

            if cpf in clientes:

                print()
                print('CPF:',cpf)
                print('Nome:',clientes[cpf][0])
                print('Endereço:',clientes[cpf][1])
                print('Telefone:',clientes[cpf][2])
                print('Nascimento:',clientes[cpf][3])

            else:

                print()
                print('CPF ainda não cadastrado!')

        elif resposta_submenus == 2:

            cpf = input('CPF: ')

            if cpf in clientes:
                
                print()
                print('-------------')
                print('1. Nome')
                print('2. Endereço')
                print('3. Telefone')
                print('4. Nascimento')
                print('-------------')

                print()
                resposta_sub_sub = int(input('Escolha uma opção: '))

                if resposta_sub_sub == 1:
                    
                    print()
                    print('Nome:', clientes[cpf][0])

                elif resposta_sub_sub == 2:

                    print()
                    print('Endereço:', clientes[cpf][1])

                elif resposta_sub_sub == 3:

                    print()
                    print('Telefone:', clientes[cpf][2])

                else:

                    print()
                    print('Nascimento:', clientes[cpf][3])

            else:

                print()
                print('CPF ainda não cadastrado!')
                    

        elif resposta_submenus == 3:

            teste2 = True
            
            print()
            cpf = input('CPF: ')

            while teste != False:
                if cpf in clientes:
                    print()
                    print('CPF já cadastrado, digite novamente')
                    print()
                    cpf = input('CPF: ')
                else:
                    teste = False

            nome = input('Nome: ')
            endereço = input('Endereço: ')
            telefone = input('Telefone: ')
            nascimento = input('Data de nascimento: ')

            listinha_dados.append(nome)
            listinha_dados.append(endereço)
            listinha_dados.append(telefone)
            listinha_dados.append(nascimento)

            clientes[cpf] = listinha_dados

            print()
            print(clientes)
            

        elif resposta_submenus == 4:
            
            cpf = input('CPF: ')

            if cpf in clientes:
                
                print()
                print('-------------')
                print('1. Nome')
                print('2. Endereço')
                print('3. Telefone')
                print('4. Nascimento')
                print('-------------')

                print()
                resposta_sub_sub = int(input('Escolha uma opção: '))

                if resposta_sub_sub == 1:
                    
                    nome = input('Nome a atualizar: ')

                    confirmação = input('Confirme a atualização (S/N): ')

                    if confirmação == 'S':

                        clientes[cpf][0] = nome
                        print(clientes)

                    else:
                        return()

                elif resposta_sub_sub == 2:

                    endereço = input('Endereço a atualizar: ')

                    confirmação = input('Confirme a atualização (S/N): ')

                    if confirmação == 'S':

                        clientes[cpf][1] = endereço
                        print(clientes)

                    else:
                        return()

                elif resposta_sub_sub == 3:

                    telefone = input('Telefone a atualizar: ')

                    confirmação = input('Confirme a atualização (S/N): ')

                    if confirmação == 'S':

                        clientes[cpf][2] = telefone
                        print(clientes)

                    else:
                        return()

                else:

                    nascimento = input('Nascimento a atualizar: ')

                    confirmação = input('Confirme a atualização (S/N): ')

                    if confirmação == 'S':

                        clientes[cpf][3] = nascimento
                        print(clientes)

                    else:
                        return()
            else:

                print()
                print('CPF ainda não cadastrado!')

        else:

            cpf = input('CPF: ')

            if cpf in clientes:
                
                print()
                print('-------------')
                print('1. Nome')
                print('2. Endereço')
                print('3. Telefone')
                print('4. Nascimento')
                print('-------------')

                print()
                resposta_sub_sub = int(input('Escolha uma opção: '))

                if resposta_sub_sub == 1:

                    confirmação = input('Confirme a retirada (S/N): ')

                    if confirmação == 'S':
                            
                        atualização = 'sem dados'
                        clientes[cpf][0] = atualização
                        print(clientes)

                    else:
                        return()
                
                elif resposta_sub_sub == 2:

                    confirmação = input('Confirme a retirada (S/N): ')

                    if confirmação == 'S':
                            
                        atualização = 'sem dados'
                        clientes[cpf][1] = atualização
                        print(clientes)

                    else:
                        return()

                elif resposta_sub_sub == 3:

                    confirmação = input('Confirme a retirada (S/N): ')

                    if confirmação == 'S':
                            
                        atualização = 'sem dados'
                        clientes[cpf][2] = atualização
                        print(clientes)

                    else:
                        return()

                else:

                    confirmação = input('Confirme a retirada (S/N): ')

                    if confirmação == 'S':
                            
                        atualização = 'sem dados'
                        clientes[cpf][3] = atualização
                        print(clientes)

                    else:
                        return()
            
def veiculos_fun(veiculos, listinha_dados, opcionais):
    
    submenus()
    
    print()
    resposta_submenus = int(input('Escolha uma opção: '))

    
def alugueis_fun(alugueis, listinha_dados):
    
    submenus()


def relatorios_fun(clientes, veiculos, relatorios):
    print()
   
    
                    ## variáveis ##
## aqui os dicionários que vamos utilizar são criados ##
## não apenas os dicionários, mas tudo o que vamos utilizar. ##

## quando for criar alguma nomeie com a função dela! ##
## exemplo: o que vou utilizar para relatórios vai se chamar relatórios ##

clientes = {}
veiculos = {}
alugueis = {}
relatorios = {}
opcionais = []
listinha_dados = []

                    ## menu ##
## o while  faz com que esse menu sempre apareça ##
## a não ser que a opção da pessoa escolha a opção sair ##

resposta = 0

while resposta != 5:
    
    print()
    print('----------------------')
    print('1. Submenu de Clientes')
    print('2. Submenu de Veículos')
    print('3. Submenu de Aluguéis')
    print('4. Relatórios')
    print('5. Sair')
    print('----------------------')

    print()
    resposta = int(input('Escolha uma opção: '))

    if resposta == 1:
        clientes_fun(clientes, listinha_dados)

    elif resposta == 2:
        veiculos_fun(veiculos, listinha_dados, opcionais)

    elif resposta == 3:
        alugueis_fun(alugueis, listinha_dados)
        
    elif resposta == 4:
        relatorios_fun(clientes, veiculos, relatorios)

print()
print('Finalizado')
