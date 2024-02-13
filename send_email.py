import smtplib, ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = "simoaboulfath52@gmail.com"
    password = "jjbh sohi drrq tjko"

    receiver = "simoaboulfath52@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

