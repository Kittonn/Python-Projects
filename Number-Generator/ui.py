from tkinter import *
from tkinter import ttk
from unicodedata import name
from requests import get
from random import randint

url_amphur = "https://raw.githubusercontent.com/kongvut/thai-province-data/master/api_amphure.json"

root = Tk()
root.title("Number Generator")
root.geometry('300x150')

card_number = StringVar()

def generator():
    res = get(url_amphur)
    data = res.json()
    
    ls_num = [int(i) for i in str(data[randint(0,967)]['id'])]
    ls_num.sort()

    card=[]
    sum = 0

    for i in range(13,1,-1):
        if (i <= 12 and i >= 9):
            sum += ls_num[i-13]*i
            card.append(ls_num[i-13])
        else:
            ran = randint(1,9)
            sum += ran * i
            card.append(ran)

    if (sum % 11 == 0):
        card.append(1)
    elif (sum % 11 == 1):
        card.append(0)
    elif (sum % 11 == 2):
        card.append(9)
    elif (sum % 11 == 3):
        card.append(8)
    elif (sum % 11 == 4):
        card.append(7)
    elif (sum % 11 == 5):
        card.append(6)
    elif (sum % 11 == 6):
        card.append(5)
    elif (sum % 11 == 7):
        card.append(4)
    elif (sum % 11 == 8):
        card.append(3)
    elif (sum % 11 == 9):
        card.append(2)
    elif (sum % 11 == 10):
        card.append(1)
    suc = ''.join([str(i) for i in card])
    card_number.set(suc)
    
    


name_lbl = ttk.Label(root,text="Number Generator")
name_lbl.place(x=10,y=10)

show_ent = ttk.Entry(root,textvariable=card_number)
show_ent.place(x=10,y=50)

random_btn = ttk.Button(root,text="Random",command=generator)
random_btn.place(x=10,y=90)

root.mainloop()