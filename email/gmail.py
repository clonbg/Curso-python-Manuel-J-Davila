import smtplib
import getpass
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.encoders import encode_base64

user = input('usuario: ')
password = getpass.getpass('Password: ')

# Cabeceras
remitente = input('From, ejemplo:administrador <admin@gmail.com>: ')
destinatario = input('To, ejemplo: amigo <amigo@gmail.com>: ')
asunto = input('Subject, Asunto del mensaje: ')
mensaje = input('Mensaje html')
archivo=input('Adjuntar archivos')

# Host y puerto smtp
gmail = smtplib.SMTP('smtp.gmail.com', 587)

# Cifrado
gmail.starttls()

# Credenciales
gmail.login(user, password)

# muestra la depuración mientras se envía
gmail.set_debuglevel(1)

header = MIMEMultipart()
header['Subject'] = asunto
header['From'] = remitente
header['To'] = destinatario

mensaje = MIMEText(mensaje, 'html')  # Content-type:text/html
header.attach(mensaje)

if(os.path.isfile(archivo)):
    adjunto = MIMEBase('application', 'octet-stream')
    adjunto.set_payload(open(archivo,'rb').read())
    encode_base64(adjunto)
    adjunto.add_header('Content-Disposition', "attachmen; filename='%s'" % os.path.basename(archivo))
    header.attach(adjunto)

# Enviar
gmail.send(remitente, destinatario, header.as_string())

# Cerrar conexión
gmail.quit()

# IMPORTANTE la cuenta de Gmail desde la que se envía debe tener activado "el acceso para las aplicaciones menos seguras".
# De no ser así dará error de conexión y recibiremos un correo diciendo que "Google acaba de bloquear a alguien para impedir que iniciara sesión en tu cuenta de Google".
# Por tanto, conviene crear una cuenta de Gmail solo para este tipo de servicio.
