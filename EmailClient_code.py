import smtplib #smtplib package for sending email by setting up server
import email # email package
from email.message import EmailMessage #importing emailmessage
import requests #importing requests
import json #importing json
import time #importing time

def email_sender(subject,body,to): #function for sending email

    server = smtplib.SMTP('smtp.gmail.com', 587) #setting up server
    server.starttls() #starting server

    text_msg = EmailMessage() #creating email message
    text_msg.set_content(body) #setting content of email
    text_msg['subject'] = subject #setting subject of email
    text_msg['to'] = to #setting to whom email is to be sent

    yourmail = "emailservice48@gmail.com" #your email
    passward = "oarzgvvvmcctmxaf" #your password
    text_msg['from'] = yourmail #setting from whom email is to be sent


    server.login(yourmail, passward) #logging in to server
    server.send_message(text_msg) #sending email
    server.quit() #quitting server


if __name__ == "__main__": # set up main function for compining at first

    subscriber = [] #creating list for storing email and topic of subscribers

    youremail = input("Enter your email: ") #taking email of subscriber
    subscriber.append(youremail) #appending email to list
    option = input("Enter your topic :  ") #taking topic of subscriber
    subscriber.append(option) #appending topic to list

    response = requests.post(
    "https://api.deepai.org/api/text-generator", #api for generating text
    data={
        'text': option,
    },
    headers={'api-key': 'quickstart-QUdJIGlzIGNvbWluZy4uLi4K'} #api key
    )
    email_data = response.json() #converting response to json
    msg = email_data['output'] #getting output from json

    subject = "Hello! Your topic is : " + option #setting subject of email
    body = msg #setting body of email
    to = youremail #setting to whom email is to be sent

    file = open("subscriber.txt","a") #opening file in append mode
    for i in subscriber: #loop for writing email and topic in file
        file.write(i) #writing email and topic in file
        file.write("\n") #writing new line in file
    file.write("\n") #writing new line in file
    file.close() #closing file

    frequency = int(input("Enter the frequency of email: ")) #taking frequency of email

    for i in range(int(frequency)): #loop for sending email
        email_sender(subject,body,to) #calling email_sender function
        time.sleep(240) #waiting for 60 seconds rather scheduling it

    print('The email has been successfully sent') #printing email sent