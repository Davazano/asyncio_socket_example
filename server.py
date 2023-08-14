import asyncio

HOST = "127.0.0.1"
PORT = 8080

async def handle_echo(reader: asyncio.StreamReader, writer: asyncio.StreamWriter) -> None:
    data = None

    while data != b"quit":
        data = await reader.read(1024)
        msg = data.decode()
        addr, port = writer.get_extra_info("peername")
        print(f"Message from {addr}:{port}: {msg!r}")

        writer.write(data)
        await writer.drain()
    
    print("clossing server")
    writer.close()
    await writer.wait_closed()
    print("clossed server")

    #raise SystemExit
    raise KeyboardInterrupt 
    #raise Exception('Closing server Exception')
    

async def run_server() -> None:
    try:
        print("start server")
        server = await asyncio.start_server(handle_echo, HOST, PORT)
        print("start server***")
        async with server:
            await server.serve_forever()
            #await server.start_serving()
            print("end server")
        
        print("end server***")
    except Exception:
        print("System exit")
        print("end server---")


if __name__ == "__main__":
    #loop = asyncio.new_event_loop()
    #loop.run_until_complete(run_server())
    print("beginning of server program")
    asyncio.run(run_server())
    print("end of server program")
    # loop.close()