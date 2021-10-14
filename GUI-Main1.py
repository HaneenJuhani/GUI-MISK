import tkinter as tk
from tkinter import filedialog, Text
import os
from tkinter.constants import W 
from tkinter import *
from tkinter import ttk 
import pandas as pd



root = tk.Tk()

canvas = tk.Canvas(root, height=650, width=1300, bg="#263D42")
canvas.pack()



# frames of the app

frame1 = tk.Frame(root, bg="#F3F3F3")
frame1.place(relwidth=0.5, relheight=0.365, relx=0.07, rely=0.06,)

frame2 = tk.Frame(root, bg="#F3F3F3")
frame2.place(relwidth=0.5, relheight=0.35, relx=0.07, rely=0.55)

frame3 = tk.Frame(root, bg="#F3F3F3")
frame3.place(relwidth=0.1, relheight=0.05, relx=0.47, rely=0.44)

frame4 = tk.Frame(root, bg="#F3F3F3")
frame4.place(relwidth=0.33, relheight=0.2, relx=0.65, rely=0.15)

frame5 = tk.Frame(root, bg="#F3F3F3")
frame5.place(relwidth=0.33, relheight=0.2, relx=0.65, rely=0.65)

frame6 = tk.Frame(root, bg="#F3F3F3")
frame6.place(relwidth=0.1, relheight=0.05, relx=0.47, rely=0.92)




#frame1 
h1=Label(frame1, text="Sampling", fg="black", bg="#138D75", relief="groove", font=("Calibri", 16))
h1.grid(row=0, columnspan=7, sticky="ewns", padx=3, pady=3)

subh1=Label(frame1, text="No.", fg="black", relief="groove", bg="#138D75", font=("Calibri Light", 12))
subh1.config(width=3)
subh1.grid(row=1, column=0, padx=3, sticky="ew")

subh2=Label(frame1, text="Sample weight", fg="black", relief="groove", bg="#B2BABB", font=("Calibri Light", 12))
subh2.config(width=14)
subh2.grid(row=1, column=1, padx=3, sticky="ew")

subh3=Label(frame1, text="Sample count", fg="black", relief="groove", bg="#B2BABB", font=("Calibri Light", 12))
subh3.config(width=14)
subh3.grid(row=1, column=2, padx=3, sticky="ew")

subh4=Label(frame1, text="Processed image", fg="black", relief="groove", bg="#B2BABB", font=("Calibri Light", 12))
subh4.config(width=14)
subh4.grid(row=1, column=3, padx=3, sticky="ew")

subh5=Label(frame1, text="LpG", fg="black", relief="groove", bg="#B2BABB", font=("Calibri Light", 12))
subh5.config(width=14)
subh5.grid(row=1, column=4, padx=3, sticky="ew")

subh6=Label(frame1, text="Ignore", fg="black", relief="groove", bg="#B2BABB", font=("Calibri Light", 12))
subh6.config(width=7)
subh6.grid(row=1, column=5, padx=3, sticky="ew")


#trying to make the rows and columns smaller so the whole table can been seen, however, it didn't work
frame1.columnconfigure(0, weight=0)
frame1.columnconfigure(1, weight=0)
frame1.columnconfigure(2, weight=0)
frame1.columnconfigure(3, weight=0)
frame1.columnconfigure(4, weight=0)
frame1.columnconfigure(5, weight=0)
frame1.columnconfigure(6, weight=0)

frame1.rowconfigure(0, weight=0)
frame1.rowconfigure(1, weight=0)
frame1.rowconfigure(2, weight=0)
frame1.rowconfigure(3, weight=0)
frame1.rowconfigure(4, weight=0)
frame1.rowconfigure(5, weight=0)
frame1.rowconfigure(6, weight=0)



#here i'm trying to add enteries to each column but i can only get one column to work, the rest won't work
for j in range (5):
    subh01=Entry(frame1, width=15, fg="black", font=("Calibri Light", 12))
    subh01.grid(column=1, padx=3, pady=3, ipadx=1, ipady=1)
    


#(No. column)>>need to rewrite this to make it autogenrate numbers 
subh0001=Label(frame1, width=2, text="1", fg="black", bg="#138D75", relief="groove", font=("Calibri Light", 12))
subh0001.grid(row=2, column=0, padx=3, sticky="ew")

subh0002=Label(frame1, width=2, text="2", fg="black", bg="#138D75", relief="groove", font=("Calibri Light", 12))
subh0002.grid(row=3, column=0, padx=3, sticky="ew")

subh0003=Label(frame1, width=2, text="3", fg="black", bg="#138D75", relief="groove", font=("Calibri Light", 12))
subh0003.grid(row=4, column=0, padx=3, sticky="ew")

subh0004=Label(frame1, width=2, text="4", fg="black", bg="#138D75", relief="groove", font=("Calibri Light", 12))
subh0004.grid(row=5, column=0, padx=3, sticky="ew")

subh0005=Label(frame1, width=2, text="5", fg="black", bg="#138D75", relief="groove", font=("Calibri Light", 12))
subh0005.grid(row=6, column=0, padx=3, sticky="ew")


#Texts 

#(sample count column)  

df0 = pd.read_csv(r'c:/Users/hano-/OneDrive/Desktop/RESULTS1.csv')
sample_count = df0["Sample count"]


subh001= Text(frame1,width='15', height=1,fg="black", bg="#F3F3F3", font=("Calibri Light", 12),borderwidth=1,relief="flat")
subh001.insert(1.0, sample_count,"center")
subh001.grid(column=2, row=2, padx=3, pady=3, ipadx=1, ipady=1)
subh001.tag_add("center", "1.0", "end")

subh002=Text(frame1,width='15', height=1,fg="black", bg="#F3F3F3", font=("Calibri Light", 12),borderwidth=1,relief="flat")
subh002.grid(column=2, row=3, padx=3, pady=3, ipadx=1, ipady=1)

subh003=Text(frame1,width='15', height=1,fg="black", bg="#F3F3F3", font=("Calibri Light", 12),borderwidth=1,relief="flat")
subh003.grid(column=2, row=4, padx=3, pady=3, ipadx=1, ipady=1)

subh004=Text(frame1,width='15', height=1,fg="black", bg="#F3F3F3", font=("Calibri Light", 12),borderwidth=1,relief="flat")
subh004.grid(column=2, row=5, padx=3, pady=3, ipadx=1, ipady=1)

subh005=Text(frame1,width='15', height=1,fg="black", bg="#F3F3F3", font=("Calibri Light", 12),borderwidth=1,relief="flat")
subh005.grid(column=2, row=6, padx=3, pady=3, ipadx=1, ipady=1)

#(processed image column)

processed_image= df0["Processed image"]

subh101=Text(frame1,width='15', height=1,fg="black", bg="#F3F3F3", font=("Calibri Light", 12),borderwidth=1,relief="flat")
subh101.insert(1.0, processed_image,"center")
subh101.grid(column=3, row=2, padx=3, pady=3, ipadx=1, ipady=1)

subh102=Text(frame1,width='15', height=1,fg="black", bg="#F3F3F3", font=("Calibri Light", 12),borderwidth=1,relief="flat")
subh102.grid(column=3, row=3, padx=3, pady=3, ipadx=1, ipady=1)

subh103=Text(frame1,width='15', height=1,fg="black", bg="#F3F3F3", font=("Calibri Light", 12),borderwidth=1,relief="flat")
subh103.grid(column=3, row=4, padx=3, pady=3, ipadx=1, ipady=1)

subh104=Text(frame1,width='15', height=1,fg="black", bg="#F3F3F3", font=("Calibri Light", 12),borderwidth=1,relief="flat")
subh104.grid(column=3, row=5, padx=3, pady=3, ipadx=1, ipady=1)

subh105=Text(frame1,width='15', height=1,fg="black", bg="#F3F3F3", font=("Calibri Light", 12),borderwidth=1,relief="flat")
subh105.grid(column=3, row=6, padx=3, pady=3, ipadx=1, ipady=1)

#(LpG column)

LpG = subh01.get().split("subh001/subh01")


subh201=Text(frame1,width='15', height=1,fg="black", bg="#F3F3F3", font=("Calibri Light", 12),borderwidth=1,relief="flat")
subh201.insert(1.0, LpG,"center")
subh201.grid(column=4, row=2, padx=3, pady=3, ipadx=1, ipady=1)

subh202=Text(frame1,width='15', height=1,fg="black", bg="#F3F3F3", font=("Calibri Light", 12),borderwidth=1,relief="flat")
subh202.grid(column=4, row=3, padx=3, pady=3, ipadx=1, ipady=1)

subh203=Text(frame1,width='15', height=1,fg="black", bg="#F3F3F3", font=("Calibri Light", 12),borderwidth=1,relief="flat")
subh203.grid(column=4, row=4, padx=3, pady=3, ipadx=1, ipady=1)

subh204=Text(frame1,width='15', height=1,fg="black", bg="#F3F3F3", font=("Calibri Light", 12),borderwidth=1,relief="flat")
subh204.grid(column=4, row=5, padx=3, pady=3, ipadx=1, ipady=1)

subh205=Text(frame1,width='15', height=1,fg="black", bg="#F3F3F3", font=("Calibri Light", 12),borderwidth=1,relief="flat")
subh205.grid(column=4, row=6, padx=3, pady=3, ipadx=1, ipady=1)


#checkbuttons
Var1 = IntVar()
Var2 = IntVar()
Var3 = IntVar()
Var4 = IntVar()
Var5 = IntVar()
 
ChkBtn1 = Checkbutton(frame1, width = 0, bg="#F3F3F3", variable = Var1)
ChkBtn1.config(width=1)
ChkBtn1.grid(row=2, column=5, padx = 5, pady = 5)

ChkBtn2 = Checkbutton(frame1, width = 0, bg="#F3F3F3", variable = Var2)
ChkBtn2.config(width=1)
ChkBtn2.grid(row=3, column=5, padx = 5, pady = 5) 

ChkBtn3 = Checkbutton(frame1, width = 0, bg="#F3F3F3", variable = Var3)
ChkBtn3.config(width=1)
ChkBtn3.grid(row=4, column=5, padx = 5, pady = 5) 

ChkBtn4 = Checkbutton(frame1, width = 0, bg="#F3F3F3", variable = Var4)
ChkBtn4.config(width=1)
ChkBtn4.grid(row=5, column=5, padx = 5, pady = 5) 

ChkBtn5 = Checkbutton(frame1, width = 0, bg="#F3F3F3", variable = Var5)
ChkBtn5.config(width=1)
ChkBtn5.grid(row=6, column=5, padx = 5, pady = 5) 

#scrollbar
#here the scrollbar should be on frame1 and 'pack' should change to 'grid' (start from row 3 and end on endless columns)
#scrl1= Scrollbar(frame4) 
#scrl1.pack(side = RIGHT, fill = Y) 

#button
#a botton to add rows (to see the button you can change 'row=7' to 'row=3')
btn1 = tk.Button(frame1, text="+", fg="#1ABC9C", font=("Calibri Bold", 12))
btn1.grid(row=7, column=0, ipadx=4, ipady=0)





#Note: I believe that the best way to create this table is to create one row with everything then create loops of it (trying to learn how)
################### END OF FRAME1 #################




#frame 2   
#Karim has been working on this 
#trying to get the table to be bellow the heading

h2=Label(frame2, text="Results", fg="black", bg="#138D75", font=("Calibri Light", 16))
h2.grid(row=0, columnspan=7, sticky="ew", padx=3, pady=3)

class Table:

    def __init__(self, frame2):

        # code for creating table
        for i in range(total_rows):
            for j in range(total_columns):
                self.e = Entry(frame2, width=10, fg='blue',
                               font=('Arial', 16, 'bold',))

                self.e.grid(row=i, column=j)
                self.e.insert(END, lst[i][j])


# take the data
lst = [('No.', 'Type', 'Target No.', 'No. Tubs', 'Dosage'),
       (1, '', '', '', ''),
       (2, '', '', '', ''),
       (3, '', '', '', ''),
       (4, '', '', '', ''),
       (5, '', '', '', '')]

# find total number of rows and
# columns in list
total_rows = len(lst)
total_columns = len(lst[0])


t = Table(frame2)




################### END OF FRAME2 #################




#Frame 3 
#Ahmad has been working on this (Frame 3 & 4)
#for Upload Sample Button

def open_file():

   file = filedialog.askopenfile(mode='r', filetypes=[('Python Files', '*.py')])

   if file:

      content = file.read()

      file.close()

#Frame 4 for Average LPG and Sample variation
avg_lbl = Label(frame4,text='Average LpG',width='20',fg="black", bg="#138D75", font=("Calibri Light", 12),borderwidth=3,relief="raised",padx=5,pady=5)

avg_lbl.place(x=10,y=20)

var_lbl = Label(frame4,text='Sample Variation',width='20',fg="black", bg="#138D75", font=("Calibri Light", 12),borderwidth=3,relief="raised",padx=5,pady=5)

var_lbl.place(x=10,y=75)

##############-------Functions-------#################


#Change this file location to where you place the csv file

df = pd.read_csv(r'c:/Users/hano-/OneDrive/Desktop/RESULTS1.csv')

avg = df['Larvae per gram'].mean()

stdev=df['Larvae per gram'].std()

cv=stdev/avg * 100



avg_text = Text(frame4,width='25',height=1,borderwidth=1,relief="solid",padx=5,pady=5)

avg_text.insert(1.0,avg,"center")

avg_text.place(x=200,y=25)

avg_text.tag_add("center", "1.0", "end")



cv_text = Text(frame4,width='25',height=1,borderwidth=1,relief="solid",padx=5,pady=5)

cv_text.insert(1.0,cv,"center")

cv_text.place(x=200,y=80)

cv_text.tag_add("center", "1.0", "end")


####################### END of Frame 3 #######################



#frame4 
#Use whichever option you like - First is for a solid border and second for a raised border

#button1= Button(frame3,text='Upload Sample',borderwidth=1,relief="solid",padx=5,pady=10)

button1= Button(frame3,text='Upload Sample',command=open_file, font=("Calibri Light", 10), borderwidth=3,relief="raised",padx=5,pady=10)

button1.pack(fill = BOTH,expand = TRUE)

#################### END OF FRAME4 #######################



#frame 5   
#Ismail has been working on this (frame 5 & 6)

i1=Label(frame5, text="Total Weight", width='20',fg="black", bg="#138D75", font=("Calibri Light", 12),borderwidth=3,relief="raised",padx=5,pady=5)
i1.grid(row=1, column=1,sticky="ew" ,padx=15, pady=15)

T1=Entry(frame5,fg="black", bg="#F0FFFF", font=("Calibri Bold", 14))
T1.grid(row=1, column=2)

i2=Label(frame5, text="Remaining Weight", fg="black", bg="#138D75", font=("Calibri Light", 12),borderwidth=3,relief="raised",padx=5,pady=5)
i2.grid(row=2, column=1,sticky="ew", padx=15, pady=15)

T2=Entry(frame5,fg="black", bg="#F0FFFF", font=("Calibri Bold", 14))
T2.grid(row=2, column=2)



################### END OF FRAME5 #################

#frame 6

i3=Button(frame6, text="Export Results", borderwidth=3,relief="raised",padx=5,pady=10, font=("Calibri Light", 10))
i3.pack(fill=BOTH, expand=TRUE)


################### END OF FRAME6 #################



root.mainloop()


