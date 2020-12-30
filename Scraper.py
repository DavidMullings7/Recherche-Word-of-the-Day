import requests
from bs4 import BeautifulSoup
import random
import smtplib

# URL of a rare-words dictionary
URL = "https://www.lexico.com/explore/literary-words"

# gets the HTML file of the main page
page = requests.get(URL)

# Constructs a BeautifulSoup object that will be used to screen-scrape the dictionary
soup = BeautifulSoup(page.content, 'html.parser')

# finds all words in the dictionary
words = soup.find_all("tr")
definitions = soup.find_all

# counts how many words in dictionary
count = 0
for word in words:
    count += 1

# generate random index for dictionary
rand = random.randint(1, count)

# iterates over words picking random word
count = 0
word_def = ""
for word in words:
    count += 1
    if count == rand:
        # populates variable with random word and definition
        word_def = word.get_text("     ")
        break

# strips excess whitespace from word
word_def = word_def.strip()
print(word_def)

# intro
intro = "Your Daily Rare Word, Lordship:"

#outro
outro = "Sincerely, The Code"

# email text
email_text = """
%s

%s

%s
""" % (intro, word_def, outro)


#The mail addresses and password
sender_address = 'davidjmullings@gmail.com'
sender_pass = 'H7bL8$YgtG]w!D\]'
receiver_address = '9155030808@vtext.com'
receiver_address2 = '9152411931@vtext.com'
receiver_address3 = '9155845639@vtext.com'

#Create SMTP session for sending the mail
session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
session.starttls() #enable security
session.login(sender_address, sender_pass) #login with mail_id and password
session.sendmail(sender_address, receiver_address, email_text)
session.sendmail(sender_address, receiver_address2, email_text)
session.sendmail(sender_address, receiver_address3, email_text)
session.quit()

