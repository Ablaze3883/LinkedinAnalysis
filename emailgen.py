import smtplib
import csv
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def read_template(filename):
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)


def main():
    message_template = read_template('template.txt')
    MY_ADDRESS = ' ag20223838@gmail.com'

    PASSWORD = ' @#ABCD1234@# '

    s = smtplib.SMTP(host='smtp.gmail.com', port = 587)
    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)

    with open("details.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=', ')

        next(csv_reader)
        for lines in csv_reader:
            msg = MIMEMultipart()
            message = message_template.substitute(PERSON_NAME=row[0], MATH=row[2],
                                                  ENG=row[3], SCI=row[4])
        print(message)
        # setup the parameters of the message
        msg['From']=MY_ADDRESS
        msg['To']=lines[1]
        msg['Subject']=" "
        # add in the message body
        msg.attach(MIMEText(message, 'plain'))
        # send the message via the server set up earlier.
        s.send_message(msg)
        del msg
        s.quit()
if __name__ == '__main__':
    main()