import requests
from bs4 import BeautifulSoup
import pandas as pd
def get_connection():
    url="https://en.wikipedia.org/wiki/List_of_largest_companies_in_India"
    response=requests.get(url)
    if response.status_code==200:
        print("connected")
        return response
    else:
        print("not connected")
def get_data(response):
    new=[]
    page=BeautifulSoup(response.content,"html.parser")
    # title of the website
    print(page.find("title").text)
    # reading the table
    table_data=page.find_all('table')[0]
    #find the headers
    header=table_data.find_all('th')
    head=[i.text.strip() for i in header]
    #explore intable rows
    table_row=table_data.find_all('tr')[1:]
    for i in table_row:
        td=i.find_all('td')
        new.append([i.text.strip() for i in td])
    #create a data frame
    df=pd.DataFrame(new,columns=head)
    df.to_csv(r'D:\own python\python projects\industry.csv',index=False) #save the file in csv
    print("file saved")


conn=get_connection()
details=get_data(conn)
