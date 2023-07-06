
import random
import pandas
import datetime as dt
import smtplib
# PERSONAL INFO FOR MAIL
MY_EMAIL = "IMPORT_YOUR_EMAIL"
PASSWORD = "IMPORT_YOUR_PASSWORD"


# Choose person who has birthday today
def get_person(dictionary, current_month, current_day):
    for item in dictionary:
        if (item['month'] == current_month) and (item['day'] == current_day):
            return item
    return None


# Choose random template of letter for file
def choose_letter(name):
    letters_list = ["letter_templates/letter_1.txt", "letter_templates/letter_2.txt", "letter_templates/letter_3.txt"]
    letter = random.choice(letters_list)
    with open(letter) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", name)
    return contents


# Send email
def send_email(letter, email):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=email, msg=f"Subject:Happy Birhtday\n\n {letter}")


# Create directory from csv
def get_directory():
    data = pandas.read_csv("birthdays.csv")
    dictionary_pandas = data.to_dict(orient="records")
    return dictionary_pandas


# Main function
def main():
    # Date
    day = dt.datetime.now()
    current_day = day.day
    current_month = day.month

    users_directory = get_directory()
    correct_item = get_person(users_directory, current_month, current_day)

    if correct_item is not None:

        name = correct_item['name']
        email = correct_item['email']

        letter_to_send = choose_letter(name)
        send_email(letter_to_send, email)


if __name__ == '__main__':
    main()

