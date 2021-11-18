from veiculo import Veiculo, ListaVeiculos

if __name__ == '__main__':
    # v = Veiculo('1234', 'Wolksvagem', 'Fusca', '1969', 1)
    # v2 = Veiculo('4321', 'Ford', 'Dodge', '1969', 2)
    # v3 = Veiculo('ABC123', 'Nissan', 'v1', '2010', 3)
    # # v.imprime()
    # # v.imprimeFinalPlaca()

    # cadastro = ListaVeiculos(5)
    # cadastro.add(v)
    # cadastro.add(v2)
    # cadastro.add(v3)

    # cadastro.remove('1234')
    # cadastro.imprime()
    
    # print(cadastro.atual)

    # INICIAR COM QUANTIDADE MAXIMA DE CADASTROS
    cadastro = ListaVeiculos(5)
    menu = True
    while menu:
        print("\n######### CADASTRO DE CARROS #########\n")
        print("Aperte 1 - Inserir um veículo na lista")
        print("Aperte 2 - Remover um veículo da lista")
        print("Aperte 3 - Consultar o cadastro")
        print("Aperte Qualquer Outro - Sair")
        r = input("Resposta: ")

        if r == '1':
            novo = Veiculo(input("Placa: "),input("Marca: "),input("Modelo: "),input("Ano: "),input("COD: "))
            cadastro.add(novo)
        elif r == '2':
            cadastro.remove(input('Placa: '))
        elif r == '3':
            placa_find = input('Placa: ')
            if len(placa_find) == 1:
                cadastro.findPlacaFinal(placa_find)
            else:
                cadastro.findPlaca(placa_find) 
        else:
            menu = False