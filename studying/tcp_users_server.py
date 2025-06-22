import socket


def server():
    # Создаем TCP-сокет
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 12345)
    server_socket.bind(server_address)

    server_socket.listen(10)
    print("Сервер запущен и ждет подключений...")

    message_history = []

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Подключение от {client_address}")

        data = client_socket.recv(1024).decode()
        print(f"Получено сообщение: {data}")

        message_history.append(data)

        # Проверяем содержимое сообщения
        if data.lower() == "как дела?":
            response = "\n".join(message_history)
        else:
            response = f"{data}"

        # Отправляем ответ клиенту
        client_socket.send(response.encode())

        # Закрываем соединение с клиентом
        client_socket.close()


if __name__ == '__main__':
    server()
