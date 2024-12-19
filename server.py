import socket

# Создаем сокет
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Связываем сокет с хостом и портом
server_socket.bind(('localhost', 9090))
print("Сервер запущен и привязан к порту 9090")

# Устанавливаем сервер в режим прослушивания
server_socket.listen(1)
print("Сервер слушает порт...")

while True:
    print("Ожидание подключения клиента...")
    conn, addr = server_socket.accept()
    print(f"Клиент подключился: {addr}")

    try:
        while True:
            # Прием данных от клиента
            data = conn.recv(1024).decode('utf-8')
            if not data:
                print("Клиент разорвал соединение")
                break

            print(f"Получено сообщение: {data}")

            # Проверка команды выхода
            if data.strip().lower() == 'exit':
                print("Клиент отправил команду 'exit'. Закрываем соединение.")
                conn.send("Соединение закрыто".encode('utf-8'))
                break

            # Отправка данных клиенту
            conn.send(f"Эхо: {data}".encode('utf-8'))
            print(f"Отправлено клиенту: Эхо: {data}")
    except Exception as e:
        print(f"Ошибка: {e}")
    finally:
        conn.close()
        print("Соединение с клиентом закрыто")
