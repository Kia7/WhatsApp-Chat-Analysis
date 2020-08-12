import pandas as pd
import re
import matplotlib.pyplot as plt

date=[]      ##list to extract and store date of the message
time=[]      ##list to extract and store time of the message
author=[]    ##list to store author of the message in the group
message=[]   ##list to store the content of the message
ms=[]
wordcountpermessage=[]
####Function to extract date using regex which was imported using re
def dater(s):
    global date
    pattern='(\d{1,2}([.\-/])\d{1,2}([.\-/])\d{1,2})'      ####Pattern for date
    dat = re.search(pattern,s)
    x = "joined using this group's invite link"
    y = "Messages to this group are now secured with end-to-end encryption. Tap for more info."
    z = "added"
    c = "changed"
    d = "created"
    e = "left"
    ####For the message to be valid, these keywords should not be a part of the line of the text
    if x not in s and y not in s and z not in s and c not in s and d not in s and e not in s:
        if dat:
            if s[0] != '*' and s[0]!=' ':
                date.append(dat.group()) ####appending the extracted date saved in "dat" and storing it in the date list and grouping by date
####Function to extract time using regex which was imported using re
def timer(s):
    global time
    pattern='(\d\d:\d\d)'  ####Pattern for time
    t = re.search(pattern,s) ####Extracting time and storing it in t
    x = "joined using this group's invite link"
    y = "Messages to this group are now secured with end-to-end encryption. Tap for more info."
    z = "added"
    c = "changed"
    d = "created"
    e = "left"
    ####For the message to be valid, these keywords should not be a part of the line of the text

    if x not in s and y not in s and z not in s and c not in s and d not in s and e not in s:
        if t:
            if s[0]!='*':
                time.append(t.group()) ####Appending the extracted time and storing it in list "time"
####Function to extract the sender and message using regex which was imported using re
def authorr(s):
    global author
    global message
    global ms
    global wordcountpermessage
    pattern = '(\d{1,2}([.\-/])\d{1,2}([.\-/])\d{1,4})'####Pattern for date
    dat = re.search(pattern, s)
    pattern = '(\d\d:\d\d)'####Pattern for time
    t = re.search(pattern, s)
    splitLine = s.split(' - ')
    dateTime = splitLine[0]
    message = ' '.join(splitLine[1:])####Splitting the message and the sender from the text
    a=message.split(": ")####The text after date,time author and : will all be the message that has been sent
    x = "joined using this group's invite link"
    y="Messages to this group are now secured with end-to-end encryption. Tap for more info."
    z="added"
    c="changed"
    d="created"
    e="left"

    if x not in s and y not in s and z not in s and c not in s and d not in s and e not in s:
        if dat:
            if t:
                author.append(a[0])
                splitMessage = message.split(': ')
                message = ' '.join(splitMessage[1:])
                ms.append(message)####Message is storeed in ms list
                wordcountpermessage.append(len(message))####Words are counted for each message
def toptenuser(df):
    ac = df['USERNAME'].value_counts()
    top10 = ac.head(10)
    top10.plot.bar()
    plt.xlabel("Usernames")
    plt.ylabel("No of messages")
    plt.title("TOP TEN USERS AND THEIR NUMBER OF MESSAGES")
    plt.show()
def datewiseactivity(df):
    g=df['DATE'].value_counts()
    g.plot.bar()
    plt.xlabel("Date")
    plt.ylabel("No of messages")
    plt.title("DATE WISE ACTIVITY")
    plt.show()
def mostactivetimeperiod(df):
    g=df['TIME'].value_counts()
    d=g.head(10)
    f=g.tail(10)
    d.plot.bar()
    plt.xlabel("Time")
    plt.ylabel("No of messages")
    plt.title("MOST ACTIVE TIME PERIOD")
    plt.show()
    f.plot.bar()
    plt.xlabel("Time")
    plt.ylabel("No of messages")
    plt.title("LEAST ACTIVE TIME PERIOD")
    plt.show()
def main():
    f = open("es.txt", encoding="utf8")####Opening the text file imported from WhatsApp group
    while 1:
        rd=f.readline()####Reading the texct line by line
        if not rd:break
        dater(rd)
        timer(rd)
        authorr(rd)

    datasheet={'DATE':date,'TIME':time,'USERNAME':author,'MESSAGE':ms}####Creating a data sheet dictionary
    df=pd.DataFrame(datasheet)####Creatign a dataframe from the data sheet created
    toptenuser(df)
    datewiseactivity(df)
    mostactivetimeperiod(df)
    #mostwords(df)
main()