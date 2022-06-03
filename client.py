import threading
import socket

IP = '127.0.0.1'  # endereço IP do servidor
PORTA = 32054 # porta disponibilizada pelo servidor
BUFFER = 1048     # definição do tamanho do buffer
FORMATO = 'UTF-8'
on = 0


def main():

    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        cliente.connect((IP,PORTA))
    except:
        return print('\nNão foi possível se conectar ao servidor!\n')

    nick = input('Insira seu nick: ')
    print('\nVocê está conectado ao servidor BrunoChat e está apto a enviar/receber mensagens')

    thread1 = threading.Thread(target=receberMensagem, args=[cliente])
    thread2 = threading.Thread(target=enviarMensagem, args=[cliente, nick])

    thread1.start()
    thread2.start()


def receberMensagem(cliente):
    global on
    while on==0:
        try:
            msg = cliente.recv(BUFFER).decode(FORMATO)
            if msg == "y":
                print("Conexão fechada pelo servidor")
                on = 1
                return
            else:
                print(msg+'\n')

        except:
            print('\nNão foi possível permanecer conectado no servidor!\n')
            print('Pressione <Enter> Para continuar...')
            cliente.close()
            break


def enviarMensagem(cliente, nick):
    global on
    while on ==0:
        try:
            msg = input('\n ')
            cliente.send(f'{nick}---> {msg}'.encode(FORMATO))
        except:
            return


main()