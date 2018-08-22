import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Email:
    FROM = "ADD@FROM"
    PASSWORD = "ADDPW"
    SUBJECT = "CAMBIO VISIBILIDAD"
    message = MIMEMultipart()

    def prepare_msg(self, to):
        self.message['From'] = self.FROM
        self.message['To'] = to
        self.message['Subject'] = self.SUBJECT

    def attach_msg(self, msg):
        self.message.attach(MIMEText(msg, 'plain'))

    def send_email(self):
        server = smtplib.SMTP('smtp.gmail.com: 587')

        server.starttls()
        server.login(self.FROM, self.PASSWORD)
        server.sendmail(self.FROM, self.message['To'], self.message.as_string())
        server.quit()

    def set_msg(self, files):
        message = "querido usuario se cambio la visibilidad a privado de los siguientes archivos: "

        for f in files:
            message += f+"\n"

        return message
