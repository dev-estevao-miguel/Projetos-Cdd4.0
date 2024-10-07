n = [" "]*5
s = [" "]*5

tam = len(n)
cont = 0
num = 0

print()#Organização de Código

print("\033[0;30;45m Bem vindo ao Cadastro GOV. Abaixo, tem um menu de informações onde podera selecionar oque deseja fazer.\033[m")

print()#Organização de Código

menu = int(input("\033[0;30;47m Press N1 \033[m - Para Cadastrar usuario\n"
                 "\033[0;30;47m Press N2 \033[m - Para fazer Loguin \n"
                 "\033[0;30;47m Press N3 \033[m - Para visualizar usuarios cadastrados \n"
                 "\033[0;30;47m Press N4 \033[m - Para Encerrar o Processo \n"))

while menu == 1 or menu == 2:

    if menu == 2:
        print(f"Você ainda não é Cadastrado ")

    for z in range(tam):
        user = n[z]
        senha = s[z]
        print(f"Cadastro realizado com sucesso.")
        print(f"Proximo Cadastro")

        user = input("Nome de usuario cadastrado: ")
        senha = input("Senha de usuario cadastrado: ")
        print("\033[0;30;42Cadastro realizado com Sucesso!\033[m")

        if user == n[0] and senha == s[0]:
            print(f"Seja bem vindo Sr(a). {user}. Acesse a plataforma .GOV")
        elif user == n[1] and senha == s[1]:
            print(f"Seja bem vindo Sr(a). {user}. Acesse a plataforma .GOV")
        elif user == [2] and senha == [2]:
            print(f"Seja bem vindo Sr(a). {user}. Acesse a plataforma .GOV")
        elif user == [3] and senha == [3]:
            print(f"Seja bem vindo Sr(a). {user}. Acesse a plataforma .GOV")
        elif user == [4] and senha == [4]:
            print(f"Seja bem vindo Sr(a). {user}. Acesse a plataforma .GOV")
        elif user == [5] and senha == [5]:
            print(f"Seja bem vindo Sr(a). {user}. Acesse a plataforma .GOV")

    proc = int(input("Encerrar o .gov ou deseja fazer alguma edição? "))
    if proc == 1:
        break


