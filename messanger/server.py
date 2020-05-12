import asyncio
from asyncio import transports
from typing import Optional


class ClientProtocol(asyncio.Protocol):
    login: str
    server: 'Server'
    transport: transports.Transport

    def __init__(self, server: 'Server'):
        self.server = server

    def data_received(self, data: bytes):
        print(data)

    def connection_made(self, transport: transports.Transport):
        self.transport = transport
        self.server.clients.append(self)
        print('connection established')

    def connection_lost(self, exception):
        self.server.clients.remove(self)
        print('connection lost')


class Server:
    clients: list

    def __init__(self):
        self.clients = []

    def create_protocol(self):
        return ClientProtocol(self)

    async def start(self):
        loop = asyncio.get_running_loop()
        coroutine = await loop.create_server(
            self.create_protocol,
            '127.0.0.1',
            8888
        )
        print('server was started ...')

        await coroutine.serve_forever()


process = Server()
asyncio.run(process.start())
