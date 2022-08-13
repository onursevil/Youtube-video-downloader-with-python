from tkinter import *
from pytube import YouTube

app=Tk()
app.geometry("800x370");app.configure(bg="grey");app.resizable(False,False)
Label(app,text="Link : ",font="impack 15 bold",bg="grey",fg="black").place(x=40,y=130)

def download():
     link=YouTube(str(entry.get()))
     dload=link.streams.first()
     dload.download("C:\\Users\\huawei\\Desktop")  ##Make sure that you have writen correct directory for your computer.

entry=Entry(app,width=60,bd=7,font="impack 10 bold",justify="center")
entry.place(x=220,y=130)



Button(app,text="Download",font="impack 20 bold",bg="red",fg="white",command=download).place(x=350,y=200)


























mainloop()
