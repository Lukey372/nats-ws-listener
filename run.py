import websockets
import asyncio
import json

async def send_keepalive(websocket):
    while True:
        await websocket.send(b"PING\r\n")
        await asyncio.sleep(120)

async def test():
    last_mint = ""
    async with websockets.connect("wss://prod-v2.nats.realtime.pump.fun/") as websocket:
        asyncio.create_task(send_keepalive(websocket))

        response = await websocket.recv()
        if "INFO" in response.decode()[0:5]:
            print("Connected")
        await websocket.send(b'CONNECT {"no_responders":true,"protocol":1,"verbose":false,"pedantic":false,"user":"subscriber","pass":"lW5a9y20NceF6AE9","lang":"nats.ws","version":"1.29.2","headers":true}\r\n')

        try:
            await websocket.send(b'SUB newCoinCreated.prod 1\r\n')
            print("Authorized")
        except websockets.exceptions.ConnectionClosedError:
            print("Unauthorized")
            exit(1)

        while True:
            response = await websocket.recv()

            if response == b"PING\r\n":
                await websocket.send(b"PONG\r\n")
            elif response == b"PONG\r\n":
                # No action required for PONG.
                pass
            else:
                decoded = response.decode()
                if decoded[0:3] == "MSG":
                    new_json = json.loads(decoded.split("\r\n")[1])
                    if new_json["mint"] == last_mint:
                        pass
                    else:
                        last_mint = new_json["mint"]
                        print(new_json)
                else:
                    print("Unknown Message")

asyncio.run(test())
