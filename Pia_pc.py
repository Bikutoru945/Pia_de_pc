import argparse
from ViruTUrl import url_scan
from imagesend import env_email
from cifrado import cifrar
from cifrado import descifrar
from check_ports_socket import checkPortsSocket
import subprocess, sys
import os

parser = argparse.ArgumentParser()
parser.add_argument("-modo", dest="mod", choices=['u', 'c', 's', 'p', 'd', 'x'], help="Modos de la herramienta:"
                                                                            "\n[u]Reporte de una url"
                                                                            "\n[c]Cifrado de de un mensajen"
                                                                            "\n[D]decifrado de de un mensaje"
                                                                            "\n[s]Mandar un email con una imagen"
                                                                            "\n[p]modo para escanear una ip"
                                                                            "\n[x]Sacar hash de un de archivos", required=True)

params = parser.parse_args()

SYMBOLS = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz1234567890¡!¿?.´¨'"

if __name__ == '__main__':
    if params.mod == "u":
        url = input("Url a escanear:\n")
        url_scan(url)

    elif params.mod == "s":
        env_email()

    elif params.mod == "c":
        msg = input("Cual es tu mensaje?\n")
        clave = int(input("Cual es tu numero clave?\n"))
        msg_cifrado = cifrar(clave, msg, SYMBOLS)
        print("Mensaje cifrado: ", msg_cifrado)

    elif params.mod == "d":
        msg = input("Cual es tu mensaje cifrado?\n")
        clave = int(input("Cual es tu numero clave?\n"))
        msg_decifrado = descifrar(clave, msg, SYMBOLS)
        print("Mensaje decifrado: ", msg_decifrado)

    elif params.mod == "p":
        ip = input("Ip que quieres escanear?\n")
        ports = input('Puerto o puertos a escanear[Separa con una coma para varios puertos ej.18,20]\n')
        ports = ports.split(',')
        for i in range(len(ports)):
            ports[i] = int(ports[i])
        checkPortsSocket(ip, ports)

    elif params.mod == "x":
        dir_path = os.path.dirname(os.path.realpath(__file__))
        dir_path = '.\Hashps.ps1'
        p = subprocess.Popen(["powershell.exe", dir_path], stdout=sys.stdout)
        p.communicate()