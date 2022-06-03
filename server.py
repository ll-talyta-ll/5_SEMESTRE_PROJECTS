import threading
import socket
################################################################
# Erros que não consegui resolver, enquanto o while fica       #
# esperando o "input" da conexão, ele não fecha o servidor     #
# tentei inserir +1 cliente pelo servidor para forçar esse     #
# connect mas ficou meio porco                                 # 
# Enquanto o cliente não da enter o terminal do servidor fica  #
# rodando                                                      # 
################################################################

IP = '127.0.0.1'  # endereço IP do servidor
PORTA = 32054   # porta disponibilizada pelo servidor
BUFFER = 1024     # definição do tamanho do buffer
FORMATO = 'UTF-8'
# con é o cliente
clientes = []
on = 0


def main():
    global on
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:  # tenta abrir o servidor
        servidor.bind((IP, PORTA))  # localhost / porta 3205
        servidor.listen()
        print("\nServidor Online\n")
    except:  # caso de erro ao abrir
        return print('\nErro: Servidor Offline!\n')

    while on == 0:  # loop para conectar clientes no servidor
        conn, addr = servidor.accept()  # aceita conexão do cliente
        clientes.append(conn)  # joga o cliente no clientes []
        print('\nUsuário conectado:', addr)
        # Mensagem de cliente conectado
        # passa argumentos para thread + funcao
        thread1 = threading.Thread(target=messagesTreatment, args=[conn])
        thread2 = threading.Thread(target=fecharConexao, args=[conn])
        thread1.start()
        thread2.start()  # inicializa a thread acima
        


def messagesTreatment(conn):
    global on
    while on == 0:
        try:
            msg = conn.recv(BUFFER)
            broadcast(msg, conn)
        except:
            desconectarCliente(conn)
            break
    if on == 1:
        return


def broadcast(msg, conn):
    global on
    if on == 0:
        for clientItem in clientes:
            if clientItem != conn:
                try:
                    clientItem.send(msg)
                except:
                    desconectarCliente(clientItem)
    if on == 1:
        return


def fecharConexao(conn):
    global on
    while on == 0:
        option = input("\nPara fechar conexão com o usuario [y/n]: ")
        if option == "y":
            conn.send(option.encode(FORMATO))
            cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            cliente.connect((IP, PORTA))
            on = 1
            return


def desconectarCliente(conn):
    global on
    if on == 0:
        clientes.remove(conn)
    if on == 1:
        return


main()