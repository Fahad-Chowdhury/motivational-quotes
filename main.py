import datetime as dt
import os
import random
import smtplib


# Set the correct values of email addresses and password of the email account.
SENDER = "my_email_address@gmail.com"
PASSWORD = "your_password"
RECEIVER = "receiver@email.com"


def send_email(subject, msg):
    """ Send an email with the given subject and message, from 'SENDER' to 'RECEIVER'. """
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=SENDER, password=PASSWORD)
        email_msg = f"Subject:{subject}\n\n{msg}"
        connection.sendmail(from_addr=SENDER, to_addrs=RECEIVER, msg=email_msg)


def select_quote():
    """ Reads quotes from 'quotes.txt' file and randomly selects a quote,
    and returns it. """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, 'quotes.txt')
    with open(file_path, "r") as file:
        quotes = file.readlines()
    selected_quote = random.choice(quotes)
    return selected_quote


def send_motivation():
    """ Send an email to 'RECEIVER' with a motivational quote on Mondays. """
    quote = select_quote()
    if dt.datetime.now().weekday() == 0:
        send_email('Monday Motivation', quote)


if __name__ == "__main__":
    send_motivation()
