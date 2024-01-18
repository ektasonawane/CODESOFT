from tkinter import *
import string
import random
import pyperclip



def generator():
    samll_albhabets=string.ascii_lowercase
    capital_alphabets=string.ascii_uppercase
    numbers=string.digits
    special_charecters=string.punctuation

    all=samll_albhabets+capital_alphabets+numbers+special_charecters
    password_length=int(lb.get())

    if choice.get()==1:
        pf.insert(0,random.sample(samll_albhabets,password_length))

    if choice.get()==2:
        pf.insert(0,random.sample(samll_albhabets+capital_alphabets,password_length))
    if choice.get()==3:
        pf.insert(0,random.sample(all,password_length))

equation="Password Generator"



def copy():

    random_password=pf.get()
    pyperclip.copy(random_password)

root=Tk()
root.title('Password Generator')
root.geometry("570x600+100+200")
root.config(bg="#3697F5")
choice=IntVar()
Font=('arial',13,'bold')
pl=Label(root,text="Password Generator", font =("times new roman",20,"bold"),bg='gray20',fg='white')
pl.grid(pady=10)
wrb=Radiobutton(root,text="Weak",value=1,variable=choice,font=Font)
wrb.grid(pady=5)
mrb=Radiobutton(root,text="Medium",value=2,variable=choice,font=Font)
mrb.grid(pady=5)
srb=Radiobutton(root,text="Strong",value=3,variable=choice,font=Font)
srb.grid(pady=5)
ll=Label(root,text="Password Lenght", font =Font,bg='gray20',fg='white')
ll.grid(pady=5)

lb=Spinbox(root,from_=5,to_=18,width=5,font=Font,fg='black')
lb.grid(pady=5)
# # l_b=Spinbox(root,from_=5,font=Font) #bg="gray20",fg='white')
# # l_b.grid(pady=5)
g_b=Button(root,text='Generate',font=Font,command=generator) #bg="gray20",fg='white')
g_b.grid(pady=5)

pf=Entry(root,width=25,bd=2,font=Font)
pf.grid(pady=5)
cb=Button(root,text='Copy',font=Font,command=copy,bg="#232224",fg='white')
cb.grid(pady=5)


root.mainloop()