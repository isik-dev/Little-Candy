import smtplib
import datetime as dt
import random


MY_EMAIL = "myemail(gmail)"
PASSWORD = "mypassword"


now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL, to_addrs="enter recepient mail",
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )
