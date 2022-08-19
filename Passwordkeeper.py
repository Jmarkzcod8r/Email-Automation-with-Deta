# This is a simple GUI application that let's you store password for different login credentials
# We've all been there when a site asked us some login information and we got hung over if
# what we are typing on the inputs is actually right. Well, this program is a good help.
# Feel free to take a look at it for your best interest

from tkinter import *
from tkinter import simpledialog
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Password Keeper')
# root.iconbitmap('C:/Users/macni/Pictures/Screenshots/asdasd.PNG')
root.geometry("350x280")

#--------for Google----------------------------------------------------
Google_0 = "John_demo@gmail.com"
Google_1= "Chris_demo@gmail.com"

Google_Pw_0 = "admin1234"
Google_Pw_1 = "my_bday"

Google_list= [Google_0, Google_1]  
Google_Pw_list=[Google_Pw_0, Google_Pw_1]

Google_click = StringVar()
Google_options_list = [Google_0,Google_1,]
Google_click.set( Google_0)

def Google_change_password():
    print(Google_click.get())
    for x in range(len(Google_list)):
        if Google_click.get()!=Google_list[x]:
            continue
        Google_password_show=Google_Pw_list[x]
  
        Google_root= tk.Tk()
        Google_root.withdraw()
    
        USER_INP = simpledialog.askstring(title="", prompt="Password is   "+"'"+(Google_password_show)+"'") 
        
        if USER_INP=='' or USER_INP==None:
            continue
        Google_Pw_list[x]=str(USER_INP)
        print(Google_Pw_list)

#-------------------------------------------------------------------
#----------------for Yahoo--------------------------------------
Yahoo_0 = "Steve_demo@yahoo.com"
Yahoo_1= "Vanessa_08@yahoo.com"

Yahoo_Pw_0 = "Guess_right"
Yahoo_Pw_1 = "banana_admin"

Yahoo_list= [Yahoo_0, Yahoo_1]  
Yahoo_Pw_list=[Yahoo_Pw_0, Yahoo_Pw_1]

Yahoo_click = StringVar()
Yahoo_options_list = [Yahoo_0,Yahoo_1,]
Yahoo_click.set( Yahoo_0)

def Yahoo_change_password():
    print(Yahoo_click.get())
    for x in range(len(Yahoo_list)):
        if Yahoo_click.get()!=Yahoo_list[x]:
            continue
        Yahoo_password_show=Yahoo_Pw_list[x]
  
        Yahoo_root= tk.Tk()
        Yahoo_root.withdraw()
    
        USER_INP = simpledialog.askstring(title="", prompt="Password is   "+"'"+(Yahoo_password_show)+"'") 
        
        if USER_INP=='' or USER_INP==None:
            continue
        Yahoo_Pw_list[x]=str(USER_INP)
        print(Yahoo_Pw_list)

#-------------------------------------------------------------------
#----------------for Youtube--------------------------------------
Youtube_0 = "Carl_1260@gmail.com"
Youtube_1= "Mr_biker@yahoo.com"
Youtube_2= "Mike_467@outlook.com"


Youtube_Pw_0 = "Apple_pass"
Youtube_Pw_1 = "Catmeows"
Youtube_Pw_2 = "Givemecookie"

Youtube_list= [Youtube_0,Youtube_1,Youtube_2]  
Youtube_Pw_list=[Youtube_Pw_0,Youtube_Pw_1,Youtube_Pw_2]

Youtube_click = StringVar()
Youtube_options_list = [Youtube_0,Youtube_1,Youtube_2]  
Youtube_click.set( Youtube_0)

def Youtube_change_password():
    print(Youtube_click.get())
    for x in range(len(Youtube_list)):
        if Youtube_click.get()!=Youtube_list[x]:
            continue
        Youtube_password_show=Youtube_Pw_list[x]
  
        Youtube_root= tk.Tk()
        Youtube_root.withdraw()
    
        USER_INP = simpledialog.askstring(title="", prompt="Password is   "+"'"+(Youtube_password_show)+"'") 
        
        if USER_INP=='' or USER_INP==None:
            continue
        Youtube_Pw_list[x]=str(USER_INP)
        print(Youtube_Pw_list)

#-------------------------------------------------------------------
#----------------for Github--------------------------------------
Github_0 = "Chris_demo@gmail.com"
# Github_1= "  asdasd"

Github_Pw_0 = "password_git"
# Github_Pw_1 = "asdsdasdasd"

Github_list= [Github_0]  
Github_Pw_list=[Github_Pw_0]

Github_click = StringVar()
Github_options_list = [Github_0,]
Github_click.set( Github_0)

def Github_change_password():
    print(Github_click.get())
    for x in range(len(Github_list)):
        if Github_click.get()!=Github_list[x]:
            continue
        Github_password_show=Github_Pw_list[x]
  
        Github_root= tk.Tk()
        Github_root.withdraw()
    
        USER_INP = simpledialog.askstring(title="", prompt="Password is   "+"'"+(Github_password_show)+"'") 
        
        if USER_INP=='' or USER_INP==None:
            continue
        Github_Pw_list[x]=str(USER_INP)
        print(Github_Pw_list)

#-------------------------------------------------------------------
#----------------for Instagram--------------------------------------
Instagram_0 = "Chris_demo@gmail.com"
# Instagram_1= "  asdasd"

Instagram_Pw_0 = "password_Insta"
# Instagram_Pw_1 = "asdsdasdasd"

Instagram_list= [Instagram_0]  
Instagram_Pw_list=[Instagram_Pw_0]

Instagram_click = StringVar()
Instagram_options_list = [Instagram_0,]
Instagram_click.set( Instagram_0)

def Instagram_change_password():
    print(Instagram_click.get())
    for x in range(len(Instagram_list)):
        if Instagram_click.get()!=Instagram_list[x]:
            continue
        Instagram_password_show=Instagram_Pw_list[x]
  
        Instagram_root= tk.Tk()
        Instagram_root.withdraw()
    
        USER_INP = simpledialog.askstring(title="", prompt="Password is   "+"'"+(Instagram_password_show)+"'") 
        
        if USER_INP=='' or USER_INP==None:
            continue
        Instagram_Pw_list[x]=str(USER_INP)
        print(Instagram_Pw_list)

#-------------------------------------------------------------------
#----------------for Facebook--------------------------------------
Facebook_0 = "Steve_demo@yahoo.com"
# Facebook_1= "  asdasd"

Facebook_Pw_0 = "password_7"
# Facebook_Pw_1 = "asdsdasdasd"

Facebook_list= [Facebook_0]  
Facebook_Pw_list=[Facebook_Pw_0]

Facebook_click = StringVar()
Facebook_options_list = [Facebook_0,]
Facebook_click.set( Facebook_0)

def Facebook_change_password():
    print(Facebook_click.get())
    for x in range(len(Facebook_list)):
        if Facebook_click.get()!=Facebook_list[x]:
            continue
        Facebook_password_show=Facebook_Pw_list[x]
  
        Facebook_root= tk.Tk()
        Facebook_root.withdraw()
    
        USER_INP = simpledialog.askstring(title="", prompt="Password is   "+"'"+(Facebook_password_show)+"'") 
        
        if USER_INP=='' or USER_INP==None:
            continue
        Facebook_Pw_list[x]=str(USER_INP)
        print(Facebook_Pw_list)

#-------------------------------------------------------------------
#----------------for Outlook--------------------------------------
Outlook_0 = "Peter_demo@hotmail.com"
# Outlook_1= "  asdasd"

Outlook_Pw_0 = "password_"
# Outlook_Pw_1 = "asdsdasdasd"

Outlook_list= [Outlook_0]  
Outlook_Pw_list=[Outlook_Pw_0]

Outlook_click = StringVar()
Outlook_options_list = [Outlook_0,]
Outlook_click.set( Outlook_0)

def Outlook_change_password():
    print(Outlook_click.get())
    for x in range(len(Outlook_list)):
        if Outlook_click.get()!=Outlook_list[x]:
            continue
        Outlook_password_show=Outlook_Pw_list[x]
  
        Outlook_root= tk.Tk()
        Outlook_root.withdraw()
    
        USER_INP = simpledialog.askstring(title="", prompt="Password is   "+"'"+(Outlook_password_show)+"'") 
        
        if USER_INP=='' or USER_INP==None:
            continue
        Outlook_Pw_list[x]=str(USER_INP)
        print(Outlook_Pw_list)

#-------------------------------------------------------------------

ttk.Label(root, text="Google", font=("Bold", 12)).grid(column=1,  columnspan =1 ,row=1)
ttk.Label(root, text="Yahoo", font=("Bold", 13)).grid(column=1, columnspan =1 ,row=2)
ttk.Label(root, text="Youtube", font=("Bold", 12)).grid(column=1,  columnspan =1 ,row=3)
ttk.Label(root, text="Github", font=("Bold", 12)).grid(column=1,  columnspan =1 ,row=4)
ttk.Label(root, text="Instagram", font=("Times New Roman", 15)).grid(column=1, columnspan =1 ,row=5)
ttk.Label(root, text="Facebook", font=("Bold", 12)).grid(column=1,  columnspan =1 ,row=6)
ttk.Label(root, text="Outlook", font=("Times New Roman", 13)).grid(column=1, columnspan =1 ,row=7)
# ttk.Label(root, text="Youtube", font=("Bold", 12)).grid(column=1,  columnspan =1 ,row=8)
# ttk.Label(root, text="Teespring", font=("Times New Roman", 13)).grid(column=1, columnspan =1 ,row=9)
# ttk.Label(root, text="Linkiro", font=("Times New Roman", 13)).grid(column=1, columnspan =1 ,row=10)


Google_drop = OptionMenu( root , Google_click , *Google_options_list ).grid(row=1, column =2)
Yahoo_drop = OptionMenu( root , Yahoo_click , *Yahoo_options_list ).grid(row=2, column =2)
Youtube_drop = OptionMenu( root , Youtube_click , *Youtube_options_list ).grid(row=3, column =2)
Github_drop = OptionMenu( root , Github_click , *Github_options_list ).grid(row=4, column =2)
Instagram_drop = OptionMenu( root , Instagram_click , *Instagram_options_list ).grid(row=5, column =2)
Facebook_drop = OptionMenu( root , Facebook_click , *Facebook_options_list ).grid(row=6, column =2)
Outlook_drop = OptionMenu( root , Outlook_click , *Outlook_options_list ).grid(row=7, column =2)


Google_password_button = Button(root, text='*', command = Google_change_password ).grid(row=1 , column=5)
Yahoo_password_button = Button(root, text='*', command = Yahoo_change_password ).grid(row=2 , column=5)
Youtube_password_button = Button(root, text='*', command = Youtube_change_password ).grid(row=3 , column=5)
Github_password_button = Button(root, text='*', command = Github_change_password ).grid(row=4 , column=5)
Instagram_password_button = Button(root, text='*', command = Instagram_change_password ).grid(row=5 , column=5)
Facebook_password_button = Button(root, text='*', command = Facebook_change_password ).grid(row=6 , column=5)
Outlook_password_button = Button(root, text='*', command = Outlook_change_password ).grid(row=7 , column=5)


root.mainloop()