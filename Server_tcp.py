'''
S E R V I D O R    T C P  

'''

import socket

target_host = "www.google.com"
target_port = 80

#Criar um objeto socket     af_net = indica que sera utilizado um endereço IPV4 -> strem indica que sera protocolo TCP
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Conectar o cliente
client.connect((target_host,target_port))

#Enviar alguns dados
client.send(b"GET / HTTP/1.1\r\nHost: www.google.com\r\nConnection: close\r\n\r\n")

#Receber alguns dados
response = client.recv(4096)

print (response.decode())
client.close