import socket
import sys
import logging

def checkPortsSocket(ip,portlist):
    try:
        for port in portlist:
            sock= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            sock.settimeout(5)
            result = sock.connect_ex((ip,port)) #
            if result == 0:
                print ("Puerto {}: \t Abierto".format(port))
            else:
                print ("Puerto {}: \t Cerrado".format(port))
            sock.close()
    except socket.error as error:
        logging.basicConfig(filename='app.log', level='DEBUG')
        print (str(error))
        print ("Error de conexion")
        logging.error('No se pudo establecer la conexion')
        sys.exit()


