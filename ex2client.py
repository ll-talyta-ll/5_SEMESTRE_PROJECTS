import socket
from tracemalloc import stop  # importa modulo socket

TCP_IP = '172.25.31.162'  # endereço IP do servidor
TCP_PORTA = 32054     # porta disponibilizada pelo servidor
TAMANHO_BUFFER = 1024
FORMATO = 'UTF-8'

# Criação de socket TCP do cliente
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Conecta ao servidor em IP e porta especifica
cliente.connect((TCP_IP, TCP_PORTA))
while True:
    MENSAGEM = input("Digite sua mensagem para o servidor: ")
    cliente.send(MENSAGEM.encode(FORMATO))
    if MENSAGEM == 'QUIT':
        cliente.send(MENSAGEM.encode(FORMATO))
        print("Conexão finalizada")
        break
    else:
        data, addr = cliente.recvfrom(1024)
        print("Servidor -->", data.decode())
        if data.decode()=="QUIT":
            print("Conexão fechada pelo servidor")
            break


# envia mensagem para servidor
# cliente.send(MENSAGEM.encode(FORMATO))

# recebe dados do servidor
# data, addr = cliente.recvfrom(1024)

# fecha conexão com servidor
#cliente.close()