import asyncio

import websockets


async def client():
    uri = "ws://localhost:8765"  # Адрес сервера
    async with websockets.connect(uri) as websocket:
        message = "Привет, сервер!"  # Сообщение, которое отправит клиент
        for _ in range(5):
            message = await websocket.recv()
            print(message)
            await websocket.send(message)  # Отправляем сообщение

        response = await websocket.recv()  # Получаем ответ от сервера
        print(f"Ответ от сервера: {response}")


asyncio.run(client())