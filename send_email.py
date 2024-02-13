import smtplib, ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = "simoaboulfath52@gmail.com"
    password = "xxxxxxxxxxxxx: you dont want to know my password!!"

    receiver = "simoaboulfath52@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

