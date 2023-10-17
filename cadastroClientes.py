# Definição da estrutura do cliente
class Cliente:
    def __init__(self, nome_completo, data_nascimento, contato_telefonico, email, endereco, cpf):
        self.nome_completo = nome_completo
        self.data_nascimento = data_nascimento
        self.contato_telefonico = contato_telefonico
        self.email = email
        self.endereco = endereco
        self.cpf = cpf

    def __str__(self):
        return (f"Nome Completo: {self.nome_completo}\n"
                f"Data de Nascimento: {self.data_nascimento}\n"
                f"Contato Telefônico: {self.contato_telefonico}\n"
                f"E-mail: {self.email}\n"
                f"Endereço: {self.endereco}\n"
                f"CPF: {self.cpf}\n")

class Node:
    def __init__(self, cliente):
        self.cliente = cliente
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None
    
    def insert(self, cliente):
        self.root = self._insert(self.root, cliente)
        
    def _insert(self, node, cliente):
        # Inserção na BST
        if not node:
            return Node(cliente)
        if cliente.nome_completo < node.cliente.nome_completo:  # Comparação pelo nome
            node.left = self._insert(node.left, cliente)
        else:
            node.right = self._insert(node.right, cliente)
            
        # Atualização da altura do nó
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        
        # Balanceamento do nó
        return self._balance(node)
    
    def search(self, cpf):
        node, comparisons = self._search(self.root, cpf, 0)
        if node:
            return node.cliente, comparisons
        return None, comparisons

    def _search(self, node, cpf, comparisons):
        if not node:
            return None, comparisons
        comparisons += 1
        if cpf == node.cliente.cpf:
            return node, comparisons
        elif cpf < node.cliente.cpf:
            return self._search(node.left, cpf, comparisons)
        else:
            return self._search(node.right, cpf, comparisons)
    
    def _get_height(self, node):
        if not node:
            return 0
        return node.height
    
    def _get_balance_factor(self, node):
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def _balance(self, node):
        balance_factor = self._get_balance_factor(node)
        if balance_factor > 1:
            if self._get_balance_factor(node.left) < 0:
                node.left = self._rotate_left(node.left)
            node = self._rotate_right(node)
        if balance_factor < -1:
            if self._get_balance_factor(node.right) > 0:
                node.right = self._rotate_right(node.right)
            node = self._rotate_left(node)
        return node
    
    def _rotate_left(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        return y

    def _rotate_right(self, y):
        x = y.left
        T3 = x.right
        x.right = y
        y.left = T3
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        x.height = 1 + max(self._get_height(x.left), self._get_height(x.right))
        return x

clientes = AVLTree()

def cadastrar_cliente():
    clear_screen()
    print("---- Cadastro de Cliente ----")
    nome_completo = input("Nome Completo: ")
    data_nascimento = input("Data de Nascimento (dd/mm/yyyy): ")
    contato_telefonico = input("Contato Telefônico: ")
    email = input("E-mail: ")
    endereco = input("Endereço: ")
    cpf = input("CPF (somente números): ")

    # Aqui pode-se adicionar validações

    cliente = Cliente(nome_completo, data_nascimento, contato_telefonico, email, endereco, cpf)
    clientes.insert(cliente)
    input("\nCliente cadastrado com sucesso! Pressione ENTER para continuar.")

def buscar_cliente_por_cpf():
    clear_screen()
    print("---- Buscar Cliente por CPF ----")
    cpf_busca = input("Digite o CPF do cliente que deseja buscar: ")
    
    cliente, comparisons = clientes.search(cpf_busca)
    
    if cliente:
        print("\n", "-"*30, "\n", cliente, "\n", "-"*30)
        print(f"\nComparações necessárias: {comparisons}\n")
    else:
        print("\nNenhum cliente com o CPF informado foi encontrado.")
        print(f"\nComparações realizadas: {comparisons}\n")
    input("Pressione ENTER para continuar.")

def listar_clientes():
    clear_screen()
    print("---- Lista de Clientes ----")

    def in_order_traversal(node):
        if node:
            in_order_traversal(node.left)
            print("\n", "-"*30, "\n", node.cliente, "\n", "-"*30)
            in_order_traversal(node.right)

    in_order_traversal(clientes.root)
    input("\nPressione ENTER para continuar.")

def clear_screen():
    print("\n" * 50)  # Simplesmente imprime várias linhas em branco para "limpar" a tela.

def main():
    while True:
        clear_screen()
        print("-" * 40)
        print(" Sistema de Cadastro de Clientes ".center(40, "-"))
        print("-" * 40)
        print("\n1. Cadastrar Cliente")
        print("2. Listar Clientes")
        print("3. Buscar Cliente por CPF")
        print("4. Sair\n")
        
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_cliente()
        elif opcao == '2':
            listar_clientes()
        elif opcao == '3':
            buscar_cliente_por_cpf()
        elif opcao == '4':
            print("\nEncerrando o sistema.")
            break
        else:
            print("\nOpção inválida. Tente novamente.\n")
            input("Pressione ENTER para continuar.")

if __name__ == '__main__':
    main()