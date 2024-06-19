import socket

target_host = "127.0.0.1"
target_port = 9998

# создаем объект сокета
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# подключаем клиент
client.connect((target_host,target_port))

# отправляем какие-нибудь данные
client.send(b"ABCDEF_TEST\r\nHost: 127.0.0.1\r\n\r\n")

# принимаем какие-нибудь данные
response = client.recv(4096)
print(response.decode())
client.close()