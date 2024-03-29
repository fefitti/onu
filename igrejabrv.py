class Usuario:
    def __init__(self, nome, sobrenome, email, telefone):
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = email
        self.telefone = telefone

class CadastroUsuarios:
    def __init__(self):
        self.usuarios = []

    def cadastrar_usuario(self, nome, sobrenome, email, telefone):
        novo_usuario = Usuario(nome, sobrenome, email, telefone)
        self.usuarios.append(novo_usuario)
        print("Usuário cadastrado com sucesso!")

    def listar_usuarios(self):
        if self.usuarios:
            print("Lista de usuários cadastrados:")
            for i, usuario in enumerate(self.usuarios, 1):
                print(f"{i}. {usuario.nome} {usuario.sobrenome} - Email: {usuario.email} - Telefone: {usuario.telefone}")
        else:
            print("Nenhum usuário cadastrado.")

def main():
    cadastro = CadastroUsuarios()

    while True:
        print("\n--- Menu ---")
        print("1. Cadastrar usuário")
        print("2. Listar usuários")
        print("3. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            sobrenome = input("Sobrenome: ")
            email = input("Email: ")
            telefone = input("Telefone: ")
            cadastro.cadastrar_usuario(nome, sobrenome, email, telefone)
        elif opcao == "2":
            cadastro.listar_usuarios()
        elif opcao == "3":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
