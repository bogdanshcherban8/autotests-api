import socket

def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 12345)
    server_socket.bind(server_address)

    server_socket.listen(10)
    print("server is running")
    messages = []

    while True:
        client_socket, client_address = server_socket.accept()
        print(f'Пользователь с адресом: {client_address} подключился к серверу')

        try:
            data = client_socket.recv(1024).decode()
            if data:
                print(f'Пользователь с адресом: {client_address} отправил сообщение: {data}')
                messages.append(f'{client_address}: {data}')
                history = '\n'.join(messages)

                client_socket.send(history.encode())

        except Exception as e:
            print(f'Ошибка при обработке клиента {client_address}: {e}')
        finally:
            client_socket.close()

if __name__ == '__main__':
    server()
