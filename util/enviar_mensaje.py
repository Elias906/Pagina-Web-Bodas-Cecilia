import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(correo_electronico, nombres, apellidos, celular, mensaje):
    # Información del servidor de correo electrónico
    smtp_server = 'smtp.gmail.com' #Se cambia por el mail del servidor ejemplo "mail.correa.com.pe"
    smtp_port = 587 #El puerto a usar sea SSL o no SSL
    smtp_username = 'alvayo1997@gmail.com' #El username ejemplo cecilia@ceciliacorrea.com.pe
    smtp_password = 'syvqbossrcyypgbe' #El password creado con el mail

    # Información del destinatario
    #to_number = 'alvayo1997'
    #to_carrier = '@gmail.com'

    # HTML del cuerpo del mensaje
    html = f"""\
    <html>
      <head>
        <style>
          body {{
            background-color: #f2f6fa;
          }}
          .container {{
            background-color: #ffffff;
            max-width: 500px;
            margin: 0 auto;
            padding: 20px;
            border-radius: 10px;
          }}
          h1, h2 {{
            color: #2c3e50;
            font-family: Arial, sans-serif;
            text-align: center;
          }}
          hr {{
            border: none;
            height: 1px;
            background-color: #dfe3e8;
            margin: 20px 0;
          }}
          p {{
            color: #000000;
            font-family: Arial, sans-serif;
            font-size: 16px;
            margin: 5px 0;
          }}
          .label {{
            color: #666666;
            font-weight: bold;
          }}
          .info {{
            color: #888888;
            font-size: 14px;
            text-align: center;
          }}
          span{{
              font-weight: normal;
          }}
        </style>
      </head>
      <body>
        <div class="container">
          <h1>Contacto desde Página Web | Cecilia Correa</h1>
          <hr>
          <p class="label">Nombres: <span>{nombres}</span></p>
          <p class="label">Apellidos: <span>{apellidos}</span></p>
          <p class="label">Celular: <span>{celular}</span></p>
          <p class="label">Correo electrónico: <span>{correo_electronico}</span></p>
          <p class="label">Mensaje: <span>{mensaje}</span></p>
          <hr>
          <p class="info">Este correo electrónico fue enviado desde la página</p>
        </div>
      </body>
    </html>
    """

    # Asunto del mensaje
    subject = 'Contacto desde Página Web - Cecilia Correa'

    # Crear objeto Multipart y agregar el contenido del mensaje
    msg = MIMEMultipart()
    msg.attach(MIMEText(html, 'html'))

    # Dirección de correo electrónico del destinatario
    #to_email = to_number + to_carrier
    to_email = smtp_username

    # Agregar información del mensaje (destinatario, remitente, asunto)
    msg['From'] = smtp_username
    msg['To'] = to_email
    msg['Subject'] = subject

    # Crear objeto de servidor SMTP
    server = smtplib.SMTP(smtp_server, smtp_port)

    # Iniciar sesión en el servidor SMTP
    server.starttls()
    server.login(smtp_username, smtp_password)

    # Enviar mensaje de correo electrónico
    server.sendmail(smtp_username, to_email, msg.as_string())

    # Cerrar sesión en el servidor SMTP
    server.quit()