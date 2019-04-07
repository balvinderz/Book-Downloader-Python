from tkinter import *
from tkinter.filedialog import askdirectory
from tkinter import messagebox
import requests
from bs4 import *
import urllib.request as urllib2

from functools import partial
def download(link,title,extension):
    page=requests.get(link)
    if(len(title)>20):
       title=title[0:19]
    file=requests.get(link,stream=True)
    folder = askdirectory()
    filename=folder+'/'+title+"."+extension
    response=urllib2.urlopen(link)
    file_=open(filename,'wb')
    data=response.read()
    file_.write(data)
    file.close()
    messagebox.showinfo("download", "download completed")
def scrape():
    
    bookname=e1.get()
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
        downloadlink=tr.find_all('td')[10].a['href']
        extension=tr.find_all('td')[8].text
        Label(w,text=author).grid(row=i,column=1)
        Label(w,text=title).grid(row=i,column=2)
        Button(w,text='download',command=partial(download,downloadlink,title,extension)).grid(row=i,column=3)
r=Tk()
r.title("Book Downloader")
w=Frame(r,)
w.pack()
Label(w,text="Book name").grid(row=0)
e1=Entry(w)
e1.grid(row=0,column=1)
submitbutton=Button(w,text="Search",command=scrape)

submitbutton.grid(row=0,column=2)
