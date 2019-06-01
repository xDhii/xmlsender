import smtplib, ssl

#emaildestinatario = input("Digite o email: ")

def email_configurar():
    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    sender_email = "xmlsendersovos@gmail.com"
    password = "@sovos123"
    
def email_destinatario():
    receiver_email = "xxxghostxxx1@gmail.com"

def email_mensagem():
    message = """\
    Subject: Teste de email
    
    Enviado através do Python."""
    
def email_enviar():    
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)