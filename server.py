# 
# Server
#
from socket import *
import threading

class ServerTI:
    def __init__(self, host='', port=12000):
        self.server_socket = socket(AF_INET, SOCK_STREAM)
        self.server_socket.bind((host, port))
        self.server_socket.listen(5)
        self.equipments = []  # Lista para armazenar os equipamentos

    def handle_client(self, connection):
        try:
            message = connection.recv(1024).decode()
            print("Mensagem recebida:", message)
            response = self.process_message(message)
            connection.send(response.encode())
        except Exception as e:
            connection.send(f"ERRO: {str(e)}".encode())
        finally:
            connection.close()

    def process_message(self, message):
        command = message[0]  # Primeiro caractere indica o comando

        if command == "A":  # Adicionar equipamento
            parts = message.split("-")
            try:
                id_eq = int(parts[1])
                nome = parts[2]
                tipo = parts[3]
                self.equipments.append({"id": id_eq, "nome": nome, "tipo": tipo})
                return "OK-Adicionado com sucesso!"
            except (IndexError, ValueError):
                return "ERRO-Dados inválidos!"

        elif command == "C":  # Consultar equipamento
            try:
                id_eq = int(message.split("-")[1])
                for eq in self.equipments:
                    if eq["id"] == id_eq:
                        return f"R-{eq['id']}-{eq['nome']}-{eq['tipo']}"
                return "NE-Não encontrado"
            except (IndexError, ValueError):
                return "ERRO-Dados inválidos!"

        else:
            return "NR-Comando não reconhecido!"

    def start(self):
        print("Servidor em execução...")
        while True:
            client_socket, _ = self.server_socket.accept()
            threading.Thread(target=self.handle_client, args=(client_socket,)).start()

if __name__ == "__main__":
    ServerTI().start()
