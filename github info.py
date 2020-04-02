#Made by Reza Moradi

import tkinter
from tkinter import *
import requests
import webbrowser

root = Tk()
root.config(width='350',height='400')
root.resizable(0,0)
root.title("Github info")

entry = Entry(root,width = '47')
entry.place(x='10',y='30')

label1 = Label(root, text = 'Enter github USERNAME here:')
label1.place(x='10',y='5')

button1 = Button(root,text = 'Done',fg='white',bg='red')
button1.place(x='300',y='28')

label2=Label(root,text='Followers',bg='blue',fg='white')
label2.config(width='20',height='2')
label2.place(x='10',y='75')

label3=Label(root,text='Following',bg='red',fg='white')
label3.config(width='20',height='2')
label3.place(x='190',y='75')

label3=Label(root,text="0",bg='gray',fg='white')
label3.config(width='20',height='10')
label3.place(x='10',y='110')

label4=Label(root,text='0',bg='gray',fg='white')
label4.config(width='20',height='10')
label4.place(x='190',y='110')

label5=Label(root,text='Repositories: ')
label5.place(x='10',y='275')

label6=Label(root,text='Bio: ')
label6.place(x='10',y='300')

button2=Button(root, text='Go to account')
button2.config(width='50',height='3',bg='blue')
button2.place(x='0',y='350')
try:
    def done(event):
        a=entry.get()
        r = requests.get(f'https://api.github.com/users/{a}').json()
        followers=r['followers']
        following=r['following']
        bio=r['bio']
        repo=r['public_repos']
        link=r["html_url"]
        label3.config(text=followers)
        label4.config(text=following)
        label5.config(text=f'Repositories: {repo}')
        label6.config(text=f"bio: {bio}")
        def go(event):
            webbrowser.open(link)
        button2.bind("<ButtonPress>",go)
    button1.bind("<ButtonPress>",done)
except:
    print("account not found or connection error!")

