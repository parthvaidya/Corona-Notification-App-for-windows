from plyer import notification
import requests
from bs4 import BeautifulSoup
import time

def notifyMe(title,message):
    notification.notify(
        title = title,
        message = message,
        app_icon = r"D:\Notification Project\icon.ico",
        timeout = 80
    )

def getData(url):
    r = requests.get(url)
    return r.text

notifyMe("sagar","Hello")
while True:
    myHtmlData = getData("https://www.mohfw.gov.in/")
    data =""
    soup = BeautifulSoup(myHtmlData, 'html.parser')
    for tr in soup.find_all('tbody'):
        data += tr.get_text()
    data_list = data.split("\n\n")

    states = ['Maharashtra']
    nested_list = []
    for item in data_list[0:80]:
        final_list = item.split("\n")[1:]
        nested_list.append(final_list)
    temp = data_list[31].split("\n")

    for i in nested_list[1:]:
        if i[1] in states:
            title = "Coronovirus cases : "
            text = f"State : {i[1]}\nTotal Cases : {i[2]}\nTotal Cured : {i[3]} \nTotal Deaths : {i[4]}\n"
            notifyMe(title,text)
            time.sleep(5)
            title = "Total Number of cases in India : "
            text = f"{temp[2]}\n\nMade By Sagar"
            notifyMe(title,text)
    time.sleep(1800)
