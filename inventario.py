import csv

computadores = []

opcao = 1

while opcao != 5:

    print("1 - Cadastrar computador")
    print("2 - Listar computadores")
    print("3 - Salvar inventário")
    print("4 - Ler inventário")
    print("5 - Sair")

    try:
         opcao = int(input("Digite uma opção: "))
    except ValueError:
        opcao = 6

    if opcao < 1 or opcao > 5:
        print("Opção inválida.")

    if opcao == 1:

        print("------------- INVENTÁRIO DE COMPUTADORES ----------------------")

        nome = input("Digite o nome da máquina: ")

        while nome.strip() == "":
            print("O nome não pode ficar vazio.")
            nome = input("Digite o nome da máquina: ")

        patrimonio = input("Digite o patrimônio da máquina: ")

        while patrimonio.strip() == "":
            print("O patrimônio não pode ficar vazio.")
            patrimonio = input("Digite o patrimônio da máquina: ")

        patrimonio_existe = True

        while patrimonio_existe == True:

            patrimonio_existe = False

            for computador in computadores:
                if patrimonio == computador["patrimonio"]:
                    patrimonio_existe = True

            if patrimonio_existe == True:
                print("Esse patrimônio já existe. Escolha outro.")
                patrimonio = input("Digite o patrimônio da máquina: ")

        setor = input("Digite o setor que a máquina está alocada: ")

        while setor.strip() == "":
            print("O setor não pode ficar vazio.")
            setor = input("Digite o setor que a máquina está alocada: ")

        sistema_operacional = input("Digite o sistema operacional da máquina: ")

        while sistema_operacional.strip() == "":
            print("O sistema operacional não pode ficar vazio.")
            sistema_operacional = input("Digite o sistema operacional da máquina: ")

        memoria_valida = False

        while not memoria_valida:
            try:
                memoria = int(input("Digite a memória da máquina: "))
                memoria_valida = True

            except ValueError:
                print("Digite a memória em números.")

        processador = input("Digite o processador da máquina: ")

        while processador.strip() == "":
            print("O processador não pode ficar vazio.")
            processador = input("Digite o processador da máquina: ")

        print("---------------------------------------------------------------")

        computador = {
            "nome": nome,
            "patrimonio": patrimonio,
            "setor": setor,
            "sistema_operacional": sistema_operacional,
            "memoria": memoria,
            "processador": processador
        }

        computadores.append(computador)

        print("Computador cadastrado com sucesso!")

    elif opcao == 2:

        if computadores:

            for computador in computadores:

                print("-----------------------------")
                print("Nome: " + computador["nome"])
                print("Patrimônio: " + computador["patrimonio"])
                print("Setor: " + computador["setor"])
                print("Sistema Operacional: " + computador["sistema_operacional"])
                print("Memória: " + str(computador["memoria"]))
                print("Processador: " + computador["processador"])
                print("-----------------------------")

        else:
            print("Nenhum computador cadastrado.")

    elif opcao == 3:

        arquivo = open("inventario.csv", "w")
        escritor = csv.writer(arquivo)

        escritor.writerow([
            "nome",
            "patrimonio",
            "setor",
            "sistema_operacional",
            "memoria",
            "processador"
        ])

        for computador in computadores:

            escritor.writerow([
                computador["nome"],
                computador["patrimonio"],
                computador["setor"],
                computador["sistema_operacional"],
                computador["memoria"],
                computador["processador"]
            ])

        arquivo.close()

        print("Inventário salvo com sucesso!")

    elif opcao == 4:

        arquivo = open("inventario.csv", "r")
        leitor = csv.reader(arquivo)

        for computador in leitor:

            if computador != []:

                if computador[0] != "nome":

                    print("-----------------------------")
                    print("Nome: " + computador[0])
                    print("Patrimônio: " + computador[1])
                    print("Setor: " + computador[2])
                    print("Sistema operacional: " + computador[3])
                    print("Memória: " + computador[4])
                    print("Processador: " + computador[5])
                    print("-----------------------------")

        arquivo.close()

