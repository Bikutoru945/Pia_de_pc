import argparse

UPPERLETTERS = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ´¨' 
LETTERS_AND_SPACE = UPPERLETTERS + UPPERLETTERS.lower() + ' \t\n'
def cifrar(clave, mensaje, SYMBOLS):
    translated = ""
    espacio=clave
    for symbol in mensaje:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            translatedIndex = symbolIndex + espacio
            if translatedIndex >= len(SYMBOLS):
                translatedIndex = translatedIndex - len(SYMBOLS)
            elif translatedIndex < 0:
                translatedIndex = translatedIndex + len(SYMBOLS)
            translated = translated + SYMBOLS[translatedIndex]
        else:
            translated = translated + symbol
    return translated


def descifrar(clave, mensaje, SYMBOLS):
    translated = ""
    espacio=clave
    for symbol in mensaje:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            translatedIndex = symbolIndex - espacio
            if translatedIndex >= len(SYMBOLS):
                translatedIndex = translatedIndex - len(SYMBOLS)
            elif translatedIndex < 0:
                translatedIndex = translatedIndex + len(SYMBOLS)
            translated = translated + SYMBOLS[translatedIndex]
        else:
            translated = translated + symbol
    return translated



SYMBOLS = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz1234567890¡!¿?.´¨'"


'''
description = """Ejemplo de uso
Para que funcione el script, hacer lo siguiente:
python nombre_script.py -modo (c|d|h) -mensaje 'mensaje' -clave ' numero clave'
OPCIONALES
-clave """

parser = argparse.ArgumentParser(description='Cifrado Cesar', epilog=description,
formatter_class=argparse.RawDescriptionHelpFormatter)

parser.add_argument("-modo", metavar='MODO', dest="modo", choices=["c","d","h"], help="c=cifrar, d=descifrar, h=hackear", required=True)
parser.add_argument("-mensaje", metavar='MENSAJE', dest="mensaje", help="Mensaje a cifrar, descifrar o hackear", required=True)
parser.add_argument("-clave", metavar='CLAVE', dest="clave", help="numero de la clave", type=int, default=3)

params = parser.parse_args()

modo = params.modo
mensaje = params.mensaje
clave = params.clave

if modo == "c":
    msg_cifrado = cifrar(clave, mensaje, SYMBOLS)
    print("Mensaje cifrado: ", msg_cifrado)
elif modo == "d":
    msg_decifrado = descifrar(clave,mensaje,SYMBOLS)
    print("Mensaje decifrado: ", msg_decifrado)
'''