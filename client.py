#
# Client
#
from socket import *

SERVER_HOST = 'localhost'
SERVER_PORT = 12000

def send_request(message):
    try:
        with socket(AF_INET, SOCK_STREAM) as client_socket:
            client_socket.connect((SERVER_HOST, SERVER_PORT))
            client_socket.send(message.encode())
            response = client_socket.recv(1024).decode()
        return response
    except Exception as e:
        return f"ERRO: {str(e)}"

while True:
    print("\n-------------------------")
    print("Gerenciamento de Equipamentos")
    print("-------------------------")
    print("1 - Adicionar Equipamento")
    print("2 - Consultar Equipamento")
    print("0 - Sair")
    option = input("Opção: ")

    if option == "0":
        print("\nEncerrando cliente...")
        break

    elif option == "1":  # Adicionar equipamento
        id_eq = input("ID do Equipamento: ")
        nome = input("Nome do Equipamento: ")
        tipo = input("Tipo do Equipamento: ")
        message = f"A-{id_eq}-{nome}-{tipo}"
        response = send_request(message)
        print("Resposta do servidor:", response)

    elif option == "2":  # Consultar equipamento
        id_eq = input("ID para consulta: ")
        message = f"C-{id_eq}"
        response = send_request(message)
        if response.startswith("R-"):
            _, id_eq, nome, tipo = response.split("-")
            print(f"ID: {id_eq}, Nome: {nome}, Tipo: {tipo}")
        elif response.startswith("NE"):
            print("Equipamento não encontrado!")
        else:
            print("Resposta do servidor:", response)

    else:
        print("Opção inválida. Tente novamente.")
