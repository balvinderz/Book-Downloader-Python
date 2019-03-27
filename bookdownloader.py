from tkinter import *
import requests
from bs4 import *
from functools import partial
def download(link):
    print(link)
def scrape():
    
    bookname=e1.get()
    print(bookname)
    url="http://libgen.is/search.php?req="+bookname+"&lg_topic=libgen&open=0&view=simple&res=25&phrase=1&column=def"
    page=requests.get(url)    
    soup=BeautifulSoup(page.text,'html.parser')
    xyz=soup.find_all('table')
    soup=xyz[2]
    trs=soup.find_all('tr')
    for i in range(1,len(trs)):
        tr=trs[i]
        author=tr.find_all('td')[1].a.text
        title=tr.find_all('td')[2].a.text
        Label(w,text=author).grid(row=i,column=1)
        Label(w,text=title).grid(row=i,column=2)
        Button(w,text='download',command=partial(download,i)).grid(row=i,column=3)
        
    """for i in range(1,len(trs)):
        soup=trs[i]
        print(soup)
    for i in range(5):"""
    
r=Tk()
r.title("Book Downloader")
w=Frame(r,)
w.pack()
Label(w,text="Book name").grid(row=0)
e1=Entry(w)
e1.grid(row=0,column=1)
submitbutton=Button(w,text="Search",command=scrape)

submitbutton.grid(row=0,column=2)
