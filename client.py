import asyncio
import time

HOST = "127.0.0.1"
PORT = 8080

async def run_client() -> None:
    reader, writer = await asyncio.open_connection(HOST, PORT)

    writer.write(b"Hello world!")
    await writer.drain()

    messages = 10

    while True:
        data = await reader.read(1024)

        # if not data:
            # writer.close()
            # raise Exception("socket closed")
        
        print(f"Received: {data.decode()!r}")

        if messages > 0:
            await asyncio.sleep(1)
            writer.write(f"{time.time()}".encode())
            await writer.drain()
            messages -= 1
        else:
            writer.write(b"quit")
            await writer.drain()
            writer.close()
            break

if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    loop.run_until_complete(run_client())