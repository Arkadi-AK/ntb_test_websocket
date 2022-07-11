import logging

import websockets

logging.basicConfig(level=logging.INFO)


async def produce(message: str, host: str, port: int) -> None:
    async with websockets.connect(f"ws://{host}:{port}") as ws:
        message_key = await ws.recv()
        message_hmac = await ws.recv()
        message_example = await ws.recv()
        message_example1 = await ws.recv()
        message_example2 = await ws.recv()
        await ws.send(message)
        mes = ws.recv()
        await ws.close()
        return await mes
