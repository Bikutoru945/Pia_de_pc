from email.message import EmailMessage
from email.utils import make_msgid
import mimetypes
import smtplib

def env_email():
    msg = EmailMessage()

    Nom = input("Cual es tu nombre\n")
    my_email = input("Cual es tu correo?\n")
    contra = input("Ingresa tu contraseña:\n")
    rec_email = input("A que correo quieres escribirle?\n")
    Asunto = str(input("Cual es el asunto?\n"))
    Cuerpo = str(input("Cual es el cuerpo?\n"))
    Img_Dir = input("Direccion de la imagen que quieres mandar?\n")

    msg['Subject'] = Asunto
    msg['From'] = my_email
    msg['To'] = rec_email
    msg.set_content('Este mail tiene una imagen.')

    image_cid = make_msgid()
    msg.add_alternative("""\
    <html>
        <body>
            <p>Hola soy {Nom}.
            {Cuerpo}
            </p>
            <img src="cid:{image_cid}">
        </body>
    </html>
    """.format(Nom=Nom, Cuerpo=Cuerpo, image_cid=image_cid[1:-1]), subtype='html')

    with open(Img_Dir, 'rb') as img:
        maintype, subtype = mimetypes.guess_type(img.name)[0].split('/')
        msg.get_payload()[1].add_related(img.read(),
                                         maintype=maintype,
                                         subtype=subtype,
                                         cid=image_cid)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(my_email, contra)

        smtp.send_message(msg)

if __name__ == '__main__':
    env_email()