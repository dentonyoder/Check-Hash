#!/usr/bin/env python3
"""
Author : denton <denton@localhost>
Date   : 2020-10-11
Purpose: Check hash of a file
"""

from tkinter import *
#from tkinter.ttk import *
from tkinter import filedialog
from tkinter import messagebox
import os, hashlib
#import pyperclip

def doit(x):
    if x == 1 : 
        # get filename filedialog
        f1.filename =  filedialog.askopenfilename(title = "Select file",filetypes = (("all files","*.*"),("jpeg files","*.jpg")))
        
        # show progress bar
        #p1 = ttk.Progressbar(f1,mode="determinate", length = 200)
        #p1.grid(row=1,column=0, columnspan=3)
        #p1.destroy()
                
        # Put filename on label and open then read the file
        lab1.config(text=f1.filename)
        file1 = open(f1.filename, "rb")
        data = file1.read()
        
        global md5Hashed, sha1Hashed, sha256Hashed
        #md5 hash
        md5Hash = hashlib.md5(data)
        md5Hashed = md5Hash.hexdigest()
        
        #sha1 hash
        sha1Hash = hashlib.sha1(data)
        sha1Hashed = sha1Hash.hexdigest()
        
        #sha256 hash
        sha256Hashed = hashlib.sha256(data).hexdigest()
        
        file1.close
        
        lab1.config(text = f1.filename + "\nMD5: " + md5Hashed + "\nSha1: " + sha1Hashed + "\nSha256: " + sha256Hashed)
        

    elif x == 2 :  
        #print("User hit Compair" )   
        #print(rbvar.get())
        if rbvar.get() == 1 :
            if eb1.get() == md5Hashed :
                messagebox.showinfo(title="MD5", message="Strings Match!")
            else :
                messagebox.showinfo(title="MD5", message="Sorry, NO match!")
        elif rbvar.get() == 2 :
            if eb1.get() == sha1Hashed :
                messagebox.showinfo(title="Sha1", message="Strings Match!")
            else :
                messagebox.showinfo(title="Sha1", message="Sorry, NO Match!")
        elif rbvar.get() == 3 :
            if eb1.get() == sha256Hashed :
                messagebox.showinfo(title="Sha256", message="Strings Match!")
            else :
                messagebox.showinfo(title="Sha256", message="Sorry, NO Match!")
       

    elif x == 3 :  
        #print("User hit Copy to clip " )
        # Using pyperclip forced a dependancy that default users would not have... Swithing to os copy.
        #pyperclip.copy(f1.filename + "\nMD5: " + md5Hashed + "\nSha1: " + sha1Hashed + "\nSha256: " + sha256Hashed)
        import os
        if os.name == "nt" :
            os.system('echo ' + f1.filename + ' MD5: ' + md5Hashed + ' Sha1: ' + sha1Hashed + ' Sha256: ' + sha256Hashed + '| clip')


# --------------------------------------------------
def main():
    """Create and Fill out forms"""

    #create mainform
    global f1, lab1, rbvar, eb1
    f1 = Tk()
    f1.title("check-hash by: Denton Yoder denton@vt.edu v:1.2")

    # Add button menu
    but1 = Button(f1,text="Select File", command=lambda:doit(1))
    but1.grid(row=0,column=0)
    but2 = Button(f1,text="Compare", command=lambda:doit(2))
    but2.grid(row=0,column=1)
    but3 = Button(f1,text="copy to Clipboard", command=lambda:doit(3))
    but3.grid(row=0,column=2)
    

    # Add label spanning all columns
    lab1 = Label(f1, text="Paste known hash in Edit box, and select it's hash type\nthen Select the file to check\n" +
        "Hit compair after the file is selected...\nIf you are just creating a hash, select your file and copy to the clipboard...", 
         height = "5", wraplength=500, justify = LEFT)
    lab1.grid(row=2,rowspan=3,column=0,columnspan=3)
    eb1 = Entry(f1,width="50")
    eb1.grid(row=5, column = 0, columnspan = 3)
    eb1.insert(0,"Value to compare goes here...")
    
    rbvar = IntVar()
    
    rb1 = Radiobutton(f1,text="MD5", variable = rbvar, value = 1)
    rb1.grid(row=0,column=3)
    rb1.select()
    rb2 = Radiobutton(f1,text="Sha1", variable = rbvar, value = 2)
    rb2.grid(row=1,column=3)
    rb3 = Radiobutton(f1,text="Sha256", variable = rbvar, value = 3)
    rb3.grid(row=2,column=3)
    
    
    
    f1.mainloop()

# --------------------------------------------------
if __name__ == '__main__':
    main()
