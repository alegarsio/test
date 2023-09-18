import socket

class get:
    def con(address , port):
        try:
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdeafaulttimeout(1)
            result = server.connect_ex((address , port))
            if result == 0:
                print('Connected')
        except : pass
get.con('192.168.1.1',80)
