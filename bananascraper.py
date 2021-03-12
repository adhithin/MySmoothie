import requests
from bs4 import BeautifulSoup
import smtplib

bananaURL = 'https://en.wikipedia.org/wiki/Banana'

headers = { "User-Agent":'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'}

page = requests.get(bananaURL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

title = soup.find(id="firstHeading").get_text()

print(title)

print(bananaURL)

def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('adhithi.nmurthy07@gmail.com', 'yavesbrwlogwvuaa')

    subject = 'mar 11 bananas + test'

    body = ' hiiii if you are getting this email, that means the program i just made is running and can send emails to people directly from the code. Check out the website to learn about Bananas: https://en.wikipedia.org/wiki/Banana'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'adhithi.nmurthy07@gmail.com',
        'adhithi.nmurthy07@gmail.com',
        msg

    )

    print("email has been sent!")

    server.quit()

answer = input("do you want this sent to your email?")

if answer == "yes":
    send_email()
else:
    print("okay, email will not send")









