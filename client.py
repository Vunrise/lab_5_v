import socket

# Создаем сокет
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Подключаемся к серверу
client_socket.connect(('localhost', 9090))
print("Соединение с сервером установлено")

try:
    while True:
        # Ввод данных для отправки на сервер
        message = input("Введите сообщение (или 'exit' для выхода): ")

        # Отправка данных серверу
        client_socket.send(message.encode('utf-8'))
        print(f"Отправлено серверу: {message}")

        # Если команда выхода, прерываем цикл
        if message.strip().lower() == 'exit':
            print("Выход из соединения")
            break

        # Прием данных от сервера
        data = client_socket.recv(1024).decode('utf-8')
        print(f"Получено от сервера: {data}")
finally:
    client_socket.close()
    print("Соединение с сервером закрыто")
