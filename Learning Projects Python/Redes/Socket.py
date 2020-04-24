import socket

mysock=socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Creacion de un objeto socket
mysock.connect(('data.pr4e.org',80)) #Conexion con el servidor

cmd='GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode() #Creacion de un mensaje. El metodo encode() converte la cadena a UTF-8
mysock.send(cmd) #Envio del mensaje

while True:
    data=mysock.recv(512)
    if(len(data)<1):
        break
    print(data.decode())

mysock.close() #Cerrar conexion