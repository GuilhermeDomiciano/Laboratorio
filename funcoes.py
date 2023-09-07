import random

def jogo_de_adivinhacao():
    ganhou = 0
    perdeu = 0
    
    while True:
        numero_secreto = random.randint(1, 128)
        tentativas = 0
        
        print("\nBem-vindo ao Jogo de Adivinhação!")
        print("Tente adivinhar o número secreto entre 1 e 128.")
        
        while tentativas < 7:
            tentativa = int(input("\nTentativa {}: Digite um número: ".format(tentativas + 1)))
            
            if tentativa < numero_secreto:
                print("O número secreto é maior. Tente novamente.")
            elif tentativa > numero_secreto:
                print("O número secreto é menor. Tente novamente.")
            else:
                print(f"Parabéns! Você acertou o número secreto ({numero_secreto}) em {tentativas + 1} tentativas.")
                ganhou += 1
                break
            
            tentativas += 1
        
        if tentativas == 7:
            print(f"Suas 7 tentativas se esgotaram. O número secreto era {numero_secreto}.")
            perdeu += 1
        
        continuar = input("\nDeseja jogar novamente? (s/n): ").lower()
        if continuar != 's':
            break
    
    print("\nJogos ganhos:", ganhou)
    print("Jogos perdidos:", perdeu)
    print("Obrigado por jogar!")

def criar_banco_de_dados():
    return []

def adicionar_informacoes():
    global banco_de_dados
    nome = input("Digite o nome da pessoa: ")
    idade = int(input("Digite a idade da pessoa: "))
    cidade = input("Digite a cidade da pessoa: ")
    telefone = input("Digite o telefone da pessoa: ")
    email = input("Digite o email da pessoa: ")
    mutavel = input("Os dados são mutáveis no futuro? (s/n) ").lower()


    if mutavel != 's':
        pessoa = (nome, idade, cidade, telefone, email, 'Não')
    else:
        pessoa = [nome, idade, cidade, telefone, email, 'Sim']
    banco_de_dados.append(pessoa)
    print("Informações adicionadas com sucesso!\n")


def exibir_banco_de_dados():
    global banco_de_dados
    print("\nBanco de Dados:")
    i = 1
    for pessoa in banco_de_dados:
        nome, idade, cidade, telefone, email, mutavel = pessoa
        print(f"{i}. Nome: {nome}")
        print(f"   Idade: {idade}")
        print(f"   Cidade: {cidade}")
        print(f"   Telefone: {telefone}")
        print(f"   Email: {email}")
        print(f"   Mutável: {mutavel}")
        print()
        i += 1


def alterar_dados():
    global banco_de_dados
    exibir_banco_de_dados()
    numero_item = int(input("Digite o número do item que deseja alterar: "))


    if numero_item < 1 or numero_item > len(banco_de_dados):
        print("Número de item inválido.")
        return


    pessoa = banco_de_dados[numero_item - 1]
    nome, idade, cidade, telefone, email, mutavel = pessoa


    if mutavel == 'Não':
        print("Esta pessoa possui dados imutáveis. Você não pode fazer modificações nela.")
        return


    print(f"\nVocê está editando os dados de {nome}.")
    print("Escolha qual campo deseja modificar:")
    print("1. Nome")
    print("2. Idade")
    print("3. Cidade")
    print("4. Telefone")
    print("5. Email")
    opcao = input("Digite o número da opção desejada: ")


    if opcao == '1':
        novo_nome = input(f"Digite o novo nome da pessoa ({nome}): ")
        if novo_nome:
            pessoa[0] = novo_nome
    elif opcao == '2':
        novo_idade = input(f"Digite a nova idade da pessoa ({idade}): ")
        if novo_idade:
            pessoa[1] = int(novo_idade)
    elif opcao == '3':
        novo_cidade = input(f"Digite a nova cidade da pessoa ({cidade}): ")
        if novo_cidade:
            pessoa[2] = novo_cidade
    elif opcao == '4':
        novo_telefone = input(f"Digite o novo telefone da pessoa ({telefone}): ")
        if novo_telefone:
            pessoa[3] = novo_telefone
    elif opcao == '5':
        novo_email = input(f"Digite o novo email da pessoa ({email}): ")
        if novo_email:
            pessoa[4] = novo_email
    else:
        print("Opção inválida. Tente novamente.")
        return


    print(f"\nDados alterados com sucesso!\n")

def banco_de_dados():
    global banco_de_dados
    banco_de_dados = criar_banco_de_dados()

    while True:
        print("Escolha uma opção:")
        print("1. Adicionar informações")
        print("2. Exibir banco de dados")
        print("3. Alterar dados de uma pessoa")
        print("4. Sair")
    
        opcao = input("Digite o número da opção desejada: ")


        if opcao == '1':
            adicionar_informacoes()
        elif opcao == '2':
            exibir_banco_de_dados()
        elif opcao == '3':
            alterar_dados()
        elif opcao == '4':
            print("Saindo do programa. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")