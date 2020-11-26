import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import PicInPic2 as PiP
import picpic as PiiP
import TextInAudio as TiA
#import TextInAudio as TiA
from tkinter import filedialog
import TextInPic as TiP
import os

root= tk.Tk()

root.title("Stego")
root.iconbitmap('pics/logo.ico')
#####################################################################################################################################################################
#------------------------------------------------------------------------------PicInPic Starts-------------------------------------------------------------------------
picinpic=ttk.Notebook(root)
picinpic.pack()
dir_name=''
one=tk.Frame(picinpic,padx=10,pady=10)
one.pack()

#-------------------------------------------------------------------------------Merge frame-----------------------------------------------------------------------------
def opencar():
    one.filename=filedialog.askopenfilename(initialdir="\\",title="Select Carrier",filetypes=(("PNG files","*.png"),("JPEG files","*.jpg"),("All files","*.*")))
    global f1
    f1=one.filename

def openpay():
    one.filename=filedialog.askopenfilename(initialdir="\\",title="Select Payload",filetypes=(("PNG files","*.png"),("JPEG files","*.jpg"),("All files","*.*")))
    global f2
    f2=one.filename

def saveloc():
    global dir_name
    dir_name = tk.filedialog.askdirectory()
    print(dir_name)

merge_frame=tk.LabelFrame(one,text="Merge",padx=10,pady=10)
merge_frame.pack()

label1=tk.Label(merge_frame,text="Carrier")
label1.grid(row=0,column=0)
button1=tk.Button(merge_frame,text="Choose File",command=opencar)
button1.grid(row=0,column=1)

label1=tk.Label(merge_frame,text="Payload")
label1.grid(row=1,column=0)
button2=tk.Button(merge_frame,text="Choose File",command=openpay)
button2.grid(row=1,column=1)

label1=tk.Label(merge_frame,text="Save in")
label1.grid(row=2,column=0)
button2=tk.Button(merge_frame,text="Choose location",command=saveloc)
button2.grid(row=2,column=1)

label1=tk.Label(merge_frame,text="Output File name (followed by .png)")
label1.grid(row=3,column=0)
e3=tk.Entry(merge_frame,width=50)
e3.grid(row=3,column=1)


def myclick():
    f3=e3.get()
    if(f1.split('.')[1] not in ('png','jpg','jpeg','webp')):
        messagebox.showerror("Error","The carrier type is not supported. You can use JPEG, JPG or PNG")
    elif(f2.split('.')[1] not in ('png','jpg','jpeg','txt')):
        messagebox.showerror("Error","The payload type cannot be merged with the selected carrier type. Yo can use JPG, JPEG, PNG or TXT")
    elif(f3.split('.')[1] not in ('png')):
        messagebox.showerror("Error","This output file type is not supported. Use .png")
    elif(f2.split('.')[1]=='txt'):
        TiP.encode(f1,f2,dir_name+'/'+f3)
        messagebox.showinfo("Status","Merge Complete")
    elif(f2.split('.')[1] in ('png','jpg','jpeg','webp') and len(dir_name)!=0):
        try:
            PiP.merge(f1,f2,dir_name+'/'+f3)
        except ValueError:
            messagebox.showerror("Error","The carrier file is smaller than payload")
        else:
            messagebox.showinfo("Status","Merge Complete")
    elif(f2.split('.')[1] in ('png','jpg','jpeg','webp') and len(dir_name)==0):
        try:
            PiP.merge(f1,f2,f3)
        except ValueError:
            messagebox.showerror("Error","The carrier file is smaller than payload")
        else:
            messagebox.showinfo("Status","Merge Complete")
    
    # mylabel=tk.Label(one,text="Merged")
    # mylabel.pack()
    

mybutton=tk.Button(merge_frame,text="Merge",command=myclick)
mybutton.grid(row=4,column=0,columnspan=2)

#--------------------------------------------------------------------------unmerge frame---------------------------------------------------------------------------
unmerge_frame=tk.LabelFrame(one,text="Unmerge",padx=10,pady=10)
unmerge_frame.pack()

label1=tk.Label(unmerge_frame,text="File Name (followed by .png)")
label1.grid(row=0,column=0)
button3=tk.Button(unmerge_frame,text="Choose File",command=opencar)
button3.grid(row=0,column=1)

label1=tk.Label(unmerge_frame,text="Save in")
label1.grid(row=1,column=0)
button2=tk.Button(unmerge_frame,text="Choose location",command=saveloc)
button2.grid(row=1,column=1)

label1=tk.Label(unmerge_frame,text="Output file name")
label1.grid(row=2,column=0)
e5=tk.Entry(unmerge_frame,width=50)
e5.grid(row=2,column=1)



def myclick2():
    f2=e5.get()
    if(f2.split('.')[1]=='txt' and len(dir_name)!=0):
        TiP.decode(f1,dir_name+'/'+f2)
        messagebox.showinfo("Status","Extraction Complete")
    elif(f2.split('.')[1]=='txt' and len(dir_name)==0):
        TiP.decode(f1,f2)
        messagebox.showinfo("Status","Extraction Complete")
    elif(f2.split('.')[1] not in ('png','jpg','jpeg','txt')):
        messagebox.showerror("Error","The payload type is incorrect.")
    elif(f2.split('.')[1].lower() in ('jpg','png','webp') and len(dir_name)!=0):
        PiP.unmerge(f1,dir_name+'/'+f2)
        messagebox.showinfo("Status","Extraction Complete")
    elif(f2.split('.')[1].lower() in ('jpg','png','webp') and len(dir_name)==0):
        PiP.unmerge(f1,f2)
        messagebox.showinfo("Status","Extraction Complete")
    
    # mylabel=tk.Label(one,text="Unmerged")
    # mylabel.pack()

mybutton2=tk.Button(unmerge_frame,text="Unmerge",command=myclick2)
mybutton2.grid(row=3,column=0,columnspan=2)
# picinpic.add(one,text="Picture")
#-------------------------------------------------------------------------------------PicInPic Ends-------------------------------------------------------------

################################################################################################################################################################

#---------------------------------------------------------------------------------------TiA starts--------------------------------------------------------------
# tia=ttk.Notebook(root)
# tia.pack()
two=tk.Frame(picinpic,padx=10,pady=10)
two.pack()

#-------------------------------------------------------------------------------------Encode frame-------------------------------------------------------------

def opencaraud():
    two.filename=filedialog.askopenfilename(initialdir="\\",title="Select Carrier",filetypes=(("Audio Files", ".wav .ogg"),   ("All Files", "*.*")))
    global a1
    a1=two.filename

def openpayaud():
    two.filename=filedialog.askopenfilename(initialdir="\\",title="Select Payload",filetypes=(("Audio Files", ".wav .ogg"),("All Files", "*.*")))
    global a2
    a2=two.filename

encode_frame=tk.LabelFrame(two,text="Encode",padx=10,pady=10)
encode_frame.pack()
label1=tk.Label(encode_frame,text="Carrier")
label1.grid(row=0,column=0)
button21=tk.Button(encode_frame,text="Choose File",command=opencaraud)
button21.grid(row=0,column=1)

label1=tk.Label(encode_frame,text="Payload")
label1.grid(row=1,column=0)
button22=tk.Button(encode_frame,text="Choose File",command=openpayaud)
button22.grid(row=1,column=1)

label1=tk.Label(encode_frame,text="Save in")
label1.grid(row=2,column=0)
button2=tk.Button(encode_frame,text="Choose location",command=saveloc)
button2.grid(row=2,column=1)

label1=tk.Label(encode_frame,text="Output File name (followed by .wav)")
label1.grid(row=3,column=0)
e7=tk.Entry(encode_frame,width=50)
e7.grid(row=3,column=1)

label1=tk.Label(encode_frame,text="Password for AES")
label1.grid(row=4,column=0)
e8=tk.Entry(encode_frame,width=50)
e8.grid(row=4,column=1)


def myclickaud():
    a3=e7.get()
    password=e8.get()
    if(a3.split('.')[1]!='wav'):
        messagebox.showerror("Error","The output type is incorrect. Can be saved to wav.")
    elif(a2.split('.')[1]!='txt'):
        messagebox.showerror("Error","The payload type is incorrect. Can hide only txt files.")
    elif(a1.split('.')[1]!='wav'):
        messagebox.showerror("Error","The carrier type is incorrect. Choose a wav file")
    elif(len(password)==0):
        messagebox.showerror("Error","Please enter password.")
    elif(len(dir_name)==0):
        TiA.EncodeToAudio(a2,a1,a3,password)
        messagebox.showinfo("Status","Merge Complete")
    else:
        TiA.EncodeToAudio(a2,a1,dir_name+'/'+a3,password)
        messagebox.showinfo("Status","Merge Complete")
    # mylabel=tk.Label(two,text="Encoded")
    # mylabel.pack()
    

mybutton21=tk.Button(encode_frame,text="Encode",command=myclickaud)
mybutton21.grid(row=5,column=0,columnspan=2)
#------------------------------------------------------------------------------Decode frame---------------------------------------------------
decode_frame=tk.LabelFrame(two,text="Unmerge",padx=10,pady=10)
decode_frame.pack()

label1=tk.Label(decode_frame,text="Audio File")
label1.grid(row=0,column=0)
button3=tk.Button(decode_frame,text="Choose File",command=opencaraud)
button3.grid(row=0,column=1)

label1=tk.Label(decode_frame,text="Save in")
label1.grid(row=1,column=0)
button2=tk.Button(decode_frame,text="Choose location",command=saveloc)
button2.grid(row=1,column=1)

label1=tk.Label(decode_frame,text="Output file name (followed by .txt)")
label1.grid(row=2,column=0)
e9=tk.Entry(decode_frame,width=50)
e9.grid(row=2,column=1)

label1=tk.Label(decode_frame,text="Password for AES")
label1.grid(row=3,column=0)
e10=tk.Entry(decode_frame,width=50)
e10.grid(row=3,column=1)

def myclick2aud():
    a4=e9.get()
    password=e10.get()
    if(a4.split('.')[1]!='txt'):
        messagebox.showerror("Error","Incorrect payload type provided. (Check your output file extension)")
    elif(len(password)==0):
        messagebox.showwarning("Missing value","Please provide the password")
    elif(a1.split('.')[1]!='wav'):
        messagebox.showerror("Error","File type chosen is not wav")
    else:
        try:
            TiA.DecodeFromAudio(a1,dir_name+'/'+a4,password)
        except ValueError:
            messagebox.showerror("Error","Incorrect password provided")
        else:
            messagebox.showinfo("Status","Extraction Complete")
    
    # mylabel=tk.Label(two,text="Decoded")
    # mylabel.pack()

mybutton22=tk.Button(decode_frame,text="Decode",command=myclick2aud)
mybutton22.grid(row=4,column=0,columnspan=2)

picinpic.add(one,text="Picture")
picinpic.add(two,text="Audio")
#---------------------------------------------------------------------------------------TiA ends--------------------------------------------------------------


##########################################################-------------------------exit-----------------------------#############################################
button_quit=tk.Button(root, text="Exit",command=root.quit)
button_quit.pack()
root.mainloop()