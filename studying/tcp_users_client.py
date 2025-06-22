import socket


def client():
    # Создаем TCP-сокет
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Подключаемся к серверу
    server_address = ('localhost', 12345)
    client_socket.connect(server_address)

    # Отправляем первое сообщение
    message = "Привет!"
    client_socket.send(message.encode())

    # Получаем ответ от сервера
    response = client_socket.recv(1024).decode()
    print(f"Ответ от сервера: {response}")

    # Закрываем текущее соединение
    client_socket.close()

    # Создаем новое подключение для второго сообщения
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(server_address)

    # Отправляем вопрос о состоянии
    message = "Как дела?"
    client_socket.send(message.encode())

    # Получаем историю сообщений
    history = client_socket.recv(1024).decode()
    print("История сообщений:")
    print(history)

    # Закрываем соединение
    client_socket.close()


if __name__ == '__main__':
    client()