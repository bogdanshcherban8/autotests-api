import asyncio
from websockets import ServerConnection
import websockets

async def echo(websocket: ServerConnection):
    async for message in websocket:
        print(f"Получено сообщение от пользователя: {message}")
        response = f" Сообщение пользователя: {message}"
        for _ in range(5):
            await websocket.send(response)

async def main():
    server = await websockets.serve(echo, "localhost", 8765)
    print("Websocket server is running...")
    await server.wait_closed()
asyncio.run(main())