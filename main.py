import datetime as dt
import pandas
import random
import smtplib

MY_EMAIL = 'leolab744@gmail.com'
PASS = 'ritwiksingh@74482'
port = 587


today = dt.datetime.now()
today_tuple = (today.month, today.day)

# use pandas to read the birthday
data = pandas.read_csv("birthdays.csv")

birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        new_mail=contents.replace("[NAME]", birthday_person["name"])


    # send generated email to  person's mail
    with smtplib.SMTP("smtp.gmail.com", port) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASS)
        connection.sendmail(
            from_addr=MY_EMAIL, 
            to_addrs=birthday_person["email"], 
            msg=f"Subject:Happy Birthday!!\n\n{new_mail}")





