import threading
import socket


clients = []
def main():

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server.bind(('localhost', 7777))
        server.listen(quit)

    except:
        return print('\n Não foi possível se conectar ao servidor!\n')

    while True:
        client, addr = server.accept()
        client.append(client)

        thread = threading.Thread(target=messagesTreatment, args=[client])
        thread.start()

def messagesTreatment(client):
    while True:
        try:
            msg = client.recv(2048)
            broadcast(msg, client)
            
            
        except:
            deleteClient(client)
            break
            
        

def broadcast(msg, client):
    for clietItem in clients:
        if clientItem != cliet:
            try:
                clientItem.send(msg)
            except:
                deleteClient(clientItem)

def deleteClient(client):
    clients.remove(client)




main()
