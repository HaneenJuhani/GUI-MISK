import tkinter as tk
from tkinter import *
from tkinter import filedialog

import pandas as pd

sample_count = pd.DataFrame()
processed_image = pd.DataFrame()

avg_lpg = []
final_lpg = [0, 0, 0, 0, 0]
n = 1
avg = 0.0
variance = 0.0


# functions

def open_file():
    global sample_count
    file_csv = filedialog.askopenfilename(title='Open a file', filetypes=[('CSV Files', '*.csv')])
    if file_csv:
        df = pd.read_csv(file_csv)
        sample_count = df.iloc[:, 0]
        processed_image = df.iloc[:, 1]
        subh001.insert(1.0, sample_count[0], "center")
        subh002.insert(1.0, sample_count[1], "center")
        subh003.insert(1.0, sample_count[2], "center")
        subh004.insert(1.0, sample_count[3], "center")
        subh005.insert(1.0, sample_count[4], "center")

        subh101.insert(1.0, processed_image[0], "center")
        subh102.insert(1.0, processed_image[1], "center")
        subh103.insert(1.0, processed_image[2], "center")
        subh104.insert(1.0, processed_image[3], "center")
        subh105.insert(1.0, processed_image[4], "center")


def populate(self, *args):
    for i in range(5):
        value = refs[i].get()

    try:
        lpg_1 = float(int(refs[0].get()) / int(sample_count[0]))
        subh201.delete('1.0', END)
        subh201.insert(INSERT, lpg_1, "center")
    except:
        pass

    try:
        lpg_2 = float(int(refs[1].get()) / int(sample_count[1]))
        subh202.delete('1.0', END)
        subh202.insert(INSERT, lpg_2, "center")
    except:
        pass

    try:
        lpg_3 = float(int(refs[2].get()) / int(sample_count[2]))
        subh203.delete('1.0', END)
        subh203.insert(INSERT, lpg_3, "center")
    except:
        pass

    try:
        lpg_4 = float(int(refs[3].get()) / int(sample_count[3]))
        subh204.delete('1.0', END)
        subh204.insert(INSERT, lpg_4, "center")
    except:
        pass

    try:
        lpg_5 = float(int(refs[4].get()) / int(sample_count[4]))
        subh205.delete('1.0', END)
        subh205.insert(INSERT, lpg_5, "center")
    except:
        pass

    final_lpg = [0, 0, 0, 0, 0]

    for i in range(0, 5):
        try:
            final_lpg[i] = (float(int(refs[i].get()) / int(sample_count[i])))
        except:
            pass

    checkbox_val = [Var1.get(), Var2.get(), Var3.get(), Var4.get(), Var5.get()]

    n = 1
    avg = 0.0
    variance = 0.0
    consider_lpg = []

    # Average Calculation
    for i in range(5):
        if checkbox_val[i] == 0:
            avg = avg + final_lpg[i]

    avg_text.delete('1.0', END)
    avg = avg / sum([1 for n in range(5) if checkbox_val[n] == 0])
    avg_text.insert(1.0, avg, "center")

    for i in range(5):
        if checkbox_val[i] == 0:
            variance = variance + (final_lpg[i] - avg) ** 2

    variance = variance / sum([1 for n in range(5) if checkbox_val[n] == 0])
    stdev = variance ** 0.5
    cv = stdev / avg * 100
    cv_text.delete('1.0', END)
    cv_text.insert(1.0, cv, "center")


# End of Functions#

root = tk.Tk()

canvas = tk.Canvas(root, height=650, width=1300, bg="#263D42")
canvas.pack()

frame1 = tk.Frame(root, bg="#F3F3F3")
frame1.place(relwidth=0.5, relheight=0.35, relx=0.07, rely=0.07, )
frame1.place(relwidth=0.5, relheight=0.365, relx=0.07, rely=0.06, )

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

# frame1

h1 = Label(frame1, text="Sampling", fg="black", bg="#138D75", font=("Calibri", 16))
h1 = Label(frame1, text="Sampling", fg="black", bg="#138D75", relief="groove", font=("Calibri", 16))
h1.grid(row=0, columnspan=7, sticky="ewns", padx=3, pady=3)

subh1 = Label(frame1, text="No.", fg="black", bg="#138D75", font=("Calibri Light", 12))
subh1.config(width=2)
subh1 = Label(frame1, text="No.", fg="black", relief="groove", bg="#138D75", font=("Calibri Light", 12))
subh1.config(width=3)
subh1.grid(row=1, column=0, padx=3, sticky="ew")

subh2 = Label(frame1, text="Sample weight", fg="black", bg="#B2BABB", font=("Calibri Light", 14))
subh2.config(width=12)
subh2 = Label(frame1, text="Sample weight", fg="black", relief="groove", bg="#B2BABB", font=("Calibri Light", 12))
subh2.config(width=14)
subh2.grid(row=1, column=1, padx=3, sticky="ew")

subh3 = Label(frame1, text="Sample count", fg="black", bg="#B2BABB", font=("Calibri Light", 14))
subh3.config(width=12)
subh3 = Label(frame1, text="Sample count", fg="black", relief="groove", bg="#B2BABB", font=("Calibri Light", 12))
subh3.config(width=14)
subh3.grid(row=1, column=2, padx=3, sticky="ew")

subh4 = Label(frame1, text="Processed image", fg="black", bg="#B2BABB", font=("Calibri Light", 14))
subh4.config(width=12)
subh4 = Label(frame1, text="Processed image", fg="black", relief="groove", bg="#B2BABB", font=("Calibri Light", 12))
subh4.config(width=14)
subh4.grid(row=1, column=3, padx=3, sticky="ew")

subh5 = Label(frame1, text="LpG", fg="black", bg="#B2BABB", font=("Calibri Light", 14))
subh5.config(width=11)
subh5 = Label(frame1, text="LpG", fg="black", relief="groove", bg="#B2BABB", font=("Calibri Light", 12))
subh5.config(width=14)
subh5.grid(row=1, column=4, padx=3, sticky="ew")

subh6 = Label(frame1, text="Ignore", fg="black", relief="groove", bg="#B2BABB", font=("Calibri Light", 12))
subh6.config(width=7)
subh6.grid(row=1, column=5, padx=3, sticky="ew")

# Sample weights by user

refs = []
for j in range(5):
    var_refs = tk.StringVar()
    refs.append(var_refs)
    subh01 = Entry(frame1, width=15, fg="black", font=("Calibri Light", 12), textvariable=var_refs)
    subh01.grid(column=1, padx=3, pady=3, ipadx=1, ipady=1)
    var_refs.trace_add('write', populate)



####End of Frame 1 setup####


# Frame 3 for Upload Button

df = pd.DataFrame()

button1 = Button(frame3, text='Upload Sample', command=open_file, borderwidth=3, relief="raised", padx=5, pady=10)
button1.pack(fill=BOTH, expand=TRUE)

################### END OF FRAME3 #################

#(sample count with function)

subh001 = Entry(frame1, width=15, fg="black", font=("Calibri Light", 12))
subh001 = Text(frame1, width='15', height=1, fg="black", bg="#F3F3F3", font=("Calibri Light", 12), borderwidth=1,
               relief="flat")
subh001.grid(column=2, row=2, padx=3, pady=3, ipadx=1, ipady=1)
# subh001.tag_add("center", "1.0", "end")

subh002 = Entry(frame1, width=15, fg="black", font=("Calibri Light", 12))
subh002 = Text(frame1, width='15', height=1, fg="black", bg="#F3F3F3", font=("Calibri Light", 12), borderwidth=1,
               relief="flat")
subh002.grid(column=2, row=3, padx=3, pady=3, ipadx=1, ipady=1)

subh003 = Entry(frame1, width=15, fg="black", font=("Calibri Light", 12))
subh003 = Text(frame1, width='15', height=1, fg="black", bg="#F3F3F3", font=("Calibri Light", 12), borderwidth=1,
               relief="flat")
subh003.grid(column=2, row=4, padx=3, pady=3, ipadx=1, ipady=1)

subh004 = Entry(frame1, width=15, fg="black", font=("Calibri Light", 12))
subh004 = Text(frame1, width='15', height=1, fg="black", bg="#F3F3F3", font=("Calibri Light", 12), borderwidth=1,
               relief="flat")
subh004.grid(column=2, row=5, padx=3, pady=3, ipadx=1, ipady=1)

subh005 = Entry(frame1, width=15, fg="black", font=("Calibri Light", 12))
subh005 = Text(frame1, width='15', height=1, fg="black", bg="#F3F3F3", font=("Calibri Light", 12), borderwidth=1,
               relief="flat")
subh005.grid(column=2, row=6, padx=3, pady=3, ipadx=1, ipady=1)

# Processed image column

subh101 = Entry(frame1, width=15, fg="black", font=("Calibri Light", 12))
subh101 = Text(frame1, width='15', height=1, fg="black", bg="#F3F3F3", font=("Calibri Light", 12), borderwidth=1,
               relief="flat")
subh101.grid(column=3, row=2, padx=3, pady=3, ipadx=1, ipady=1)

subh102 = Entry(frame1, width=15, fg="black", font=("Calibri Light", 12))
subh102 = Text(frame1, width='15', height=1, fg="black", bg="#F3F3F3", font=("Calibri Light", 12), borderwidth=1,
               relief="flat")
subh102.grid(column=3, row=3, padx=3, pady=3, ipadx=1, ipady=1)

subh103 = Entry(frame1, width=15, fg="black", font=("Calibri Light", 12))
subh103 = Text(frame1, width='15', height=1, fg="black", bg="#F3F3F3", font=("Calibri Light", 12), borderwidth=1,
               relief="flat")
subh103.grid(column=3, row=4, padx=3, pady=3, ipadx=1, ipady=1)

subh104 = Entry(frame1, width=15, fg="black", font=("Calibri Light", 12))
subh104 = Text(frame1, width='15', height=1, fg="black", bg="#F3F3F3", font=("Calibri Light", 12), borderwidth=1,
               relief="flat")
subh104.grid(column=3, row=5, padx=3, pady=3, ipadx=1, ipady=1)

subh105 = Entry(frame1, width=15, fg="black", font=("Calibri Light", 12))
subh105 = Text(frame1, width='15', height=1, fg="black", bg="#F3F3F3", font=("Calibri Light", 12), borderwidth=1,
               relief="flat")
subh105.grid(column=3, row=6, padx=3, pady=3, ipadx=1, ipady=1)

# LpG column

subh201 = Entry(frame1, width=15, fg="black", font=("Calibri Light", 12))
subh201 = Text(frame1, width='15', height=1, fg="black", bg="#F3F3F3", font=("Calibri Light", 12), borderwidth=1,
               relief="flat")
subh201.grid(column=4, row=2, padx=3, pady=3, ipadx=1, ipady=1)

subh202 = Entry(frame1, width=15, fg="black", font=("Calibri Light", 12))
subh202 = Text(frame1, width='15', height=1, fg="black", bg="#F3F3F3", font=("Calibri Light", 12), borderwidth=1,
               relief="flat")
subh202.grid(column=4, row=3, padx=3, pady=3, ipadx=1, ipady=1)

subh203 = Entry(frame1, width=15, fg="black", font=("Calibri Light", 12))
subh203 = Text(frame1, width='15', height=1, fg="black", bg="#F3F3F3", font=("Calibri Light", 12), borderwidth=1,
               relief="flat")
subh203.grid(column=4, row=4, padx=3, pady=3, ipadx=1, ipady=1)

subh204 = Entry(frame1, width=15, fg="black", font=("Calibri Light", 12))
subh204 = Text(frame1, width='15', height=1, fg="black", bg="#F3F3F3", font=("Calibri Light", 12), borderwidth=1,
               relief="flat")
subh204.grid(column=4, row=5, padx=3, pady=3, ipadx=1, ipady=1)

subh205 = Entry(frame1, width=15, fg="black", font=("Calibri Light", 12))
subh205 = Text(frame1, width='15', height=1, fg="black", bg="#F3F3F3", font=("Calibri Light", 12), borderwidth=1,
               relief="flat")
subh205.grid(column=4, row=6, padx=3, pady=3, ipadx=1, ipady=1)

# (No. column)

subh0001 = Label(frame1, width=2, text="1", fg="black", bg="#138D75", font=("Calibri Light", 12))
subh0001.grid(row=2, column=0, padx=3, sticky="ew")

subh0002 = Label(frame1, width=2, text="2", fg="black", bg="#138D75", font=("Calibri Light", 12))
subh0002.grid(row=3, column=0, padx=3, sticky="ew")

subh0003 = Label(frame1, width=2, text="3", fg="black", bg="#138D75", font=("Calibri Light", 12))
subh0003.grid(row=4, column=0, padx=3, sticky="ew")

subh0004 = Label(frame1, width=2, text="4", fg="black", bg="#138D75", font=("Calibri Light", 12))
subh0004.grid(row=5, column=0, padx=3, sticky="ew")

subh0005 = Label(frame1, width=2, text="5", fg="black", bg="#138D75", font=("Calibri Light", 12))
subh0005.grid(row=6, column=0, padx=3, sticky="ew")

# checkbuttons
Var1 = IntVar()
Var2 = IntVar()
Var3 = IntVar()
Var4 = IntVar()
Var5 = IntVar()

ChkBtn1 = Checkbutton(frame1, width=0, variable=Var1)
ChkBtn1 = Checkbutton(frame1, width=0, bg="#F3F3F3", variable=Var1)
ChkBtn1.config(width=1)
ChkBtn1.grid(row=2, column=6, padx=5, pady=5)
ChkBtn1.grid(row=2, column=5, padx=5, pady=5)
Var1.trace_add('write', populate)

ChkBtn2 = Checkbutton(frame1, width=0, variable=Var2)
ChkBtn2 = Checkbutton(frame1, width=0, bg="#F3F3F3", variable=Var2)
ChkBtn2.config(width=1)
ChkBtn2.grid(row=3, column=6, padx=5, pady=5)
ChkBtn2.grid(row=3, column=5, padx=5, pady=5)
Var2.trace_add('write', populate)

ChkBtn3 = Checkbutton(frame1, width=0, variable=Var3)
ChkBtn3 = Checkbutton(frame1, width=0, bg="#F3F3F3", variable=Var3)
ChkBtn3.config(width=1)
ChkBtn3.grid(row=4, column=6, padx=5, pady=5)
ChkBtn3.grid(row=4, column=5, padx=5, pady=5)
Var3.trace_add('write', populate)

ChkBtn4 = Checkbutton(frame1, width=0, variable=Var4)
ChkBtn4 = Checkbutton(frame1, width=0, bg="#F3F3F3", variable=Var4)
ChkBtn4.config(width=1)
ChkBtn4.grid(row=5, column=6, padx=5, pady=5)
ChkBtn4.grid(row=5, column=5, padx=5, pady=5)
Var4.trace_add('write', populate)

ChkBtn5 = Checkbutton(frame1, width=0, variable=Var5)
ChkBtn5 = Checkbutton(frame1, width=0, bg="#F3F3F3", variable=Var5)
ChkBtn5.config(width=1)
ChkBtn5.grid(row=6, column=6, padx=5, pady=5)
ChkBtn5.grid(row=6, column=5, padx=5, pady=5)
Var5.trace_add('write', populate)


# Frame 4 for Average LPG and Sample variation

avg_lbl = Label(frame4, text='Average LpG', width='20', fg="black", bg="#138D75", font=("Calibri Light", 12),
                borderwidth=3, relief="raised", padx=5, pady=5)
avg_lbl.place(x=10, y=20)

var_lbl = Label(frame4, text='Sample Variation', width='20', fg="black", bg="#138D75", font=("Calibri Light", 12),
                borderwidth=3, relief="raised", padx=5, pady=5)
var_lbl.place(x=10, y=75)

avg_text = Text(frame4, width='25', height=1, borderwidth=1, relief="solid", padx=5, pady=5)
avg_text.place(x=200, y=25)
avg_text.tag_add("center", "1.0", "end")

cv_text = Text(frame4, width='25', height=1, borderwidth=1, relief="solid", padx=5, pady=5)
cv_text.place(x=200, y=80)
cv_text.tag_add("center", "1.0", "end")


################### END OF FRAME4 #################

############### Frame2 #################

h2=Label(frame2, text="Results", fg="black", bg="#138D75", font=("Calibri", 16))
h2.grid(row=0, columnspan=7, sticky="ew", padx=3, pady=3)

no1=Label(frame2, text="No.", fg="black", relief="groove", bg="#138D75", font=("Calibri Light", 12))
no1.config(width=3)
no1.grid(row=1, column=0, padx=3, sticky="ew")

type1=Label(frame2, text="Type", fg="black", relief="groove", bg="#B2BABB", font=("Calibri Light", 12))
type1.config(width=17)
type1.grid(row=1, column=1, padx=3, sticky="ew")

target1=Label(frame2, text="Target No.", fg="black", relief="groove", bg="#B2BABB", font=("Calibri Light", 12))
target1.config(width=18)
target1.grid(row=1, column=2, padx=3, sticky="ew")

tubs1=Label(frame2, text="No. Tubs", fg="black", relief="groove", bg="#B2BABB", font=("Calibri Light", 12))
tubs1.config(width=18)
tubs1.grid(row=1, column=3, padx=3, sticky="ew")

dosage1=Label(frame2, text="Dosage", fg="black", relief="groove", bg="#B2BABB", font=("Calibri Light", 12))
dosage1.config(width=18)
dosage1.grid(row=1, column=4, padx=3, sticky="ew")

#No.
no01 = Label(frame2, width=2, text="1", fg="black", bg="#138D75", font=("Calibri Light", 12))
no01.grid(row=2, column=0, padx=3, sticky="ew")

no02 = Label(frame2, width=2, text="2", fg="black", bg="#138D75", font=("Calibri Light", 12))
no02.grid(row=3, column=0, padx=3, sticky="ew")

no03 = Label(frame2, width=2, text="3", fg="black", bg="#138D75", font=("Calibri Light", 12))
no03.grid(row=4, column=0, padx=3, sticky="ew")

no04 = Label(frame2, width=2, text="4", fg="black", bg="#138D75", font=("Calibri Light", 12))
no04.grid(row=5, column=0, padx=3, sticky="ew")

no05 = Label(frame2, width=2, text="5", fg="black", bg="#138D75", font=("Calibri Light", 12))
no05.grid(row=6, column=0, padx=3, sticky="ew")

#dosage

do01 = Label(frame2, width=2, fg="black", relief="flat", font=("Calibri Light", 12))
do01.grid(row=2, column=4, padx=3, sticky="ew")

do02 = Label(frame2, width=2, fg="black", relief="flat", font=("Calibri Light", 12))
do02.grid(row=3, column=4, padx=3, sticky="ew")

do03 = Label(frame2, width=2, fg="black", relief="flat", font=("Calibri Light", 12))
do03.grid(row=4, column=4, padx=3, sticky="ew")

do04 = Label(frame2, width=2, fg="black", relief="flat", font=("Calibri Light", 12))
do04.grid(row=5, column=4, padx=3, sticky="ew")

do05 = Label(frame2, width=2, fg="black", relief="flat", font=("Calibri Light", 12))
do05.grid(row=6, column=4, padx=3, sticky="ew")

#type loop

#refs = []
#for j in range(5):
#    var_refs = tk.StringVar()
#    refs.append(var_refs)
#    ty01 = Entry(frame2, width=15, fg="black", font=("Calibri Light", 12), textvariable=var_refs)
#    ty01.grid(column=1, padx=3, pady=3, ipadx=1, ipady=1)
#    var_refs.trace_add('write', populate)    


#type 
ty001 = Entry(frame2, width=2, fg="black", font=("Calibri Light", 12))
ty001.grid(row=2, column=1, padx=3, pady=3, sticky="ew")

ty002 = Entry(frame2, width=2, fg="black", font=("Calibri Light", 12))
ty002.grid(row=3, column=1, padx=3, pady=3, sticky="ew")

ty003 = Entry(frame2, width=2, fg="black", font=("Calibri Light", 12))
ty003.grid(row=4, column=1, padx=3, pady=3, sticky="ew")

ty004 = Entry(frame2, width=2, fg="black", font=("Calibri Light", 12))
ty004.grid(row=5, column=1, padx=3, pady=3,sticky="ew")

ty005 = Entry(frame2, width=2, fg="black", font=("Calibri Light", 12))
ty005.grid(row=6, column=1, padx=3, pady=3, sticky="ew")

#Target
tr001 = Entry(frame2, width=2, fg="black", font=("Calibri Light", 12))
tr001.grid(row=2, column=2, padx=3, pady=3, sticky="ew")

tr002 = Entry(frame2, width=2, fg="black", font=("Calibri Light", 12))
tr002.grid(row=3, column=2, padx=3, pady=3, sticky="ew")

tr003 = Entry(frame2, width=2, fg="black", font=("Calibri Light", 12))
tr003.grid(row=4, column=2, padx=3, pady=3, sticky="ew")

tr004 = Entry(frame2, width=2, fg="black", font=("Calibri Light", 12))
tr004.grid(row=5, column=2, padx=3, pady=3,sticky="ew")

tr005 = Entry(frame2, width=2, fg="black", font=("Calibri Light", 12))
tr005.grid(row=6, column=2, padx=3, pady=3, sticky="ew")

#Tubs

tu001 = Entry(frame2, width=2, fg="black", font=("Calibri Light", 12))
tu001.grid(row=2, column=3, padx=3, pady=3, sticky="ew")

do002 = Entry(frame2, width=2, fg="black", font=("Calibri Light", 12))
do002.grid(row=3, column=3, padx=3, pady=3, sticky="ew")

do003 = Entry(frame2, width=2, fg="black", font=("Calibri Light", 12))
do003.grid(row=4, column=3, padx=3, pady=3, sticky="ew")

do004 = Entry(frame2, width=2, fg="black", font=("Calibri Light", 12))
do004.grid(row=5, column=3, padx=3, pady=3,sticky="ew")

do005 = Entry(frame2, width=2, fg="black", font=("Calibri Light", 12))
do005.grid(row=6, column=3, padx=3, pady=3, sticky="ew")




############ END OF FRAME2 ################
 
  
# Frame 5
#Ismail has been working on this (frame 5 & 6)

def open_files():
    T2 = Entry(frame5, fg="black", font=("Calibri Bold", 14))
    T2.grid(row=2, column=2)


i1=Label(frame5, text="Total Weight", width='20',fg="black", bg="#138D75", font=("Calibri Light", 12),borderwidth=3,relief="raised",padx=5,pady=5)
i1.place(x=10, y=20)

T1=Entry(frame5,fg="black", width='25', borderwidth=1, relief="solid", font=("Calibri Light", 12))
T1.place(x=200, y=25)

i2=Label(frame5, width=20, text="Remaining Weight", fg="black", bg="#138D75", font=("Calibri Light", 12),borderwidth=3,relief="raised",padx=5,pady=5)
i2.place(x=10, y=75)

i2_text = Text(frame5, width='25', height=1, borderwidth=1, relief="solid", padx=5, pady=5)
i2_text.place(x=200, y=80)
i2_text.tag_add("center", "1.0", "end")

#T2=Entry(frame5,fg="black", bg="#F0FFFF", font=("Calibri Bold", 14))
#T2.grid(row=2, column=2)


################### END OF FRAME5 #################

# Frame 6

i3 = Button(frame6, text="Export Results", borderwidth=3, relief="raised", padx=5, pady=10, font=("Calibri Light", 10))
i3.pack(fill=BOTH, expand=TRUE)

################### END OF FRAME6 #################
root.mainloop()
