import tkinter as tk
from tkinter import *
from tkinter import ttk
from datetime import *
import time
from fpdf import FPDF

######
#######

root = Tk()
root.title("Medical Report")
root.geometry("1420x700")

my_tree= ttk.Treeview(root)

# define columns 
my_tree["columns"] = ("name" , "ID" , "fav")

#formate columns
my_tree.column("#0" , width = 100 , minwidth = 25 )
my_tree.column("name" , anchor=W , width = 350)
my_tree.column("ID" , anchor = W , width = 250)
my_tree.column("fav" , anchor = W , width=350)

#create headings
my_tree.heading("#0" , text = "Label" , anchor = W)
my_tree.heading("name" , text = "Test Name" , anchor = W)
my_tree.heading("ID" , text= "Value and Units" , anchor = CENTER)
my_tree.heading("fav" , text = "Normal Range" , anchor = CENTER)

my_tree.place(x = 50 , y = 300 , height= 350)

#creating frame

frame1 = LabelFrame(root ,  border= 0 , height = 270 , width = 1400)
frame1.place(x = 50 , y = 15)

# patient name lanel and entry box for patient name
pt_label = Label(frame1 , text  = "Patient Name : " , width= 15 , anchor= "w" )
p = tk.StringVar()
patient = Entry(frame1 , width = 30 , textvariable= p)
pt_label.place(x = 10 , y = 50)
patient.place(x = 120 , y = 50)

# choosing gender 
choose = StringVar(frame1)
choose.set("male")
gender = OptionMenu(frame1 , choose ,"male" , "female" )
gender.place(x = 710 , y = 50)

gender_label = Label(frame1 , text = "Gender :" , width = 7 , anchor = "w")
gender_label.place( x  = 640 , y = 50)

#age label and entry box for age
age_label = Label(frame1 , text = "Age : " , width  = 10 , anchor = "w" )
age_label.place(x = 450 , y = 50)

age = Entry(frame1 , width = 10)
age.place(x = 500 , y = 50)

#date label and entry box date is automatically generated 
date_label = Label(frame1 , text = "Date : " , width = 15 , anchor = "w")
date_label.place( x = 1080 , y = 0)
dat = Entry(frame1 , width = 20)
dat.place(x = 1150 , y = 0)
dt = datetime.now().strftime("%d-%m-%Y")
dat.insert(0,dt)

"""
#time label and entry box time is automatically generated 
time_label = Label(frame1 , text = "Time : " , width = 15 , anchor = "w")
time_label.place( x = 1080 , y = 50)
tm = Entry(frame1 , width = 20)
tm.place(x = 1150 , y = 50)
t = time.strftime("%I:%M %p")
tm.insert(0,t) 

"""

#doctor label and entry box for doctor name
doctor_label = Label(frame1 , text = "Doctor Name : " , width = 15 , anchor = "w")
doctor_label.place(x = 10 , y = 5)
doctor = Entry(frame1 , width = 30)
doctor.place(x = 120 , y = 0 )

#test name label and entry box for test name
test_label = Label(frame1 , text = "Test Name" , width = 15 , anchor = "center")
test_label.place(x = 70 , y = 180)
test = Entry(frame1 , width = 30)
test.place(x = 0 , y = 205)

# value and units label and entry box , here values and units are to be entered in single box
uv_label = Label(frame1 , text = "Value and Units" , width = 15 , anchor = "center")
uv_label.place(x = 320 , y = 180)
uv = Entry(frame1 , width = 20)
uv.place(x = 290 , y = 205)

#normal ranges label and entry box
nr_label = Label(frame1 , text = "Normal Range" , width = 15 , anchor = "center")
nr_label.place(x = 520 , y = 180)
nr = Entry(frame1 , width = 20)
nr.place(x = 490 , y = 205)

#multiple commented code is for lab name and address
"""
lab_name_label = Label(root , text = "Lab Name : " , width = 15 , anchor = "w")
lab_name_label.place(x = 1120  , y = 300)
lab_name = Entry(root , width = 30)
lab_name.place(x = 1120 , y = 330)

lab_name_label = Label(root , text = "Address : " , width = 15 , anchor = "w")
lab_name_label.place(x = 1120  , y = 360)
lab_name = Text(root , width = 40 , height = 15  , border= 1)
lab_name.place(x = 1120 , y = 380)
"""
        
#class to create header for pdf
class PDF(FPDF):
    def header(self) :
        self.set_font("times" , "B" , 30)
        self.cell(0 , 30 , "LAB NAME"  , border  = 0 ,ln = 1 , align = "C")
        
        self.set_font("times" , "" , 16)
        pdf.set_font("times" , "" , 16)
        pdf.cell(140 , 10 , f"Doctor Name : {doctor.get()}" , align = "L")
        pdf.cell(30 , 10 , f"Date : {dat.get()}" , align = "L" , ln = 1)
        pdf.cell(90 , 10 , f"Patient Name : {patient.get()}" , align = "L" , ln = 0)
        pdf.cell(50 , 10 , f"Patient Age : {age.get()}" , align = "L")
        pdf.cell(50 , 10 , f"Gender : {choose.get()}" , align = "L" , ln = 1)
    
        
        pdf.set_y(65)
        pdf.set_font("times" , "B" , 16 )
        q00 = str("Test Name")
        q01 = str("Value and Units")
        q02 = str("Normal Range")
        pdf.cell(15 , 20 , "No"  ,border= 0, ln = 0 , align = "L")
        pdf.cell(70 , 20 , q00  ,border= 0, ln = 0 , align = "L")
        pdf.cell(60 , 20 , q01  ,border= 0, ln = 0 , align = "L")
        pdf.cell(60 , 20 , q02 ,border= 0, ln = 1 , align = "L")

#add function : Adds data entered in the entry box to table and to the pdf simultaneousy

i = 0
ii = 0
y = 0
pdf  = PDF("P" , "mm" , "Letter"  )
pdf.add_page()

pdf.set_font("times" ,"" , 16)
pdf.set_auto_page_break(auto = True , margin = 20)

def add() :
    global i , y
    if test.get() != "" and uv.get() != "" and nr.get() != "" :
        my_tree.insert(parent = "" , index = "end" , iid = i , text = i+1  , values = (test.get() , uv.get() , nr.get()))

        i += 1
        ii = i
    else :
        print("cells are empty")

    if ii == 1 :
            pdf.set_y(40)
            pdf.set_font("times" , "" , 16)
            pdf.cell(140 , 10 , f"Doctor Name : {doctor.get()}" , align = "L")
            pdf.cell(30 , 10 , f"Date : {dat.get()}" , align = "L" , ln = 1)
            pdf.cell(90 , 10 , f"Patient Name : {patient.get()}" , align = "L" , ln = 0)
            pdf.cell(50 , 10 , f"Patient Age : {age.get()}" , align = "L")
            pdf.cell(50 , 10 , f"Gender : {choose.get()}" , align = "L" , ln = 1)
    
        
            pdf.set_y(85)
            pdf.set_font("times" , "" , 14 )

   
    q = str(ii)
    q1 = str(test.get())
    q2 = str(uv.get())
    q3 = str(nr.get())

    pdf.cell(15 , 10 , q + "."  ,border= 0, ln = 0 , align = "L")
    pdf.cell(70 , 10 , q1 ,border= 0, ln = 0 , align = "L")
    pdf.cell(60 , 10 , q2 ,border= 0, ln = 0 , align = "L")
    pdf.cell(60 , 10 , q3 ,border= 0, ln = 1 , align = "L")


    #test.delete(0 , END)
    #uv.delete(0 , END)
    #nr.delete(0 , END)


#prnt function : prints the pdf
def prnt():
    pdf.set_y(40)
    pdf.set_font("times" , "" , 16)
    pdf.cell(140 , 10 , f"Doctor Name : {doctor.get()}" , align = "L")
    pdf.cell(30 , 10 , f"Date : {dat.get()}" , align = "L" , ln = 1)
    pdf.cell(90 , 10 , f"Patient Name : {patient.get()}" , align = "L" , ln = 0)
    pdf.cell(50 , 10 , f"Patient Age : {age.get()}" , align = "L")
    pdf.cell(50 , 10 , f"Gender : {choose.get()}" , align = "L" , ln = 1)
    

    pdf.output("medical_report.pdf")
    

#add button when clicked runs add function 
add_button = Button(frame1 , text = "Add Data" , command = add)
add_button.place(x = 690 , y = 204 )

#print button when clicked runs prnt function
print_button = Button(root , text = "Print" , command = prnt)
print_button.place(x = 1150 , y = 620 )

root.mainloop()