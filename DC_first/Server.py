import rpyc

class FactorialService(rpyc.Service):
    def exposed_factorial(self, n):
        print('User Input Recieved: ',n)
        result = 1
        for i in range(1, n+1):
            result *= i
        print("Result sent to user.")
        return result

from rpyc.utils.server import ThreadedServer

server = ThreadedServer(FactorialService, port=18861)
print("Server running...")
server.start()
