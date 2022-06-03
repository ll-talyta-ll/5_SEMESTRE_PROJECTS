import socket #importa modulo socket
 
TCP_IP = '172.25.31.162'  # endereço IP do servidor
TCP_PORTA = 32054    # porta disponibilizada pelo servidor
TAMANHO_BUFFER = 1024     # definição do tamanho do buffer
FORMATO = 'UTF-8'
 
# Criação de socket TCP
# SOCK_STREAM, indica que será TCP.
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# IP e porta que o servidor deve aguardar a conexão
servidor.bind((TCP_IP, TCP_PORTA))
#Define o limite de conexões. 
servidor.listen(1)

print("Servidor Online") 
# Aceita conexão 
conn, addr = servidor.accept()
print ('Usuário conectado:', addr)
while True:
    #dados retidados da mensagem recebida
    data = conn.recv(TAMANHO_BUFFER)
    if data.decode()=="QUIT":
        print("Conexão finalizada pelo cliente")
        servidor.close()
        break
    else:
        print(addr, "-->", data.decode())
        MENSAGEM = input("Digite sua mensagem para o servidor: ")
        if MENSAGEM =="QUIT":
            conn.send(MENSAGEM.encode(FORMATO))
            print("Conexão finalizada")
            break
        else:
            conn.send(MENSAGEM.encode(FORMATO))