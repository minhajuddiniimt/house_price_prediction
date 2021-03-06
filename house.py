from tkinter import *
from joblib import load
model = load('housing_model.joblib')

def predict_value():
    crim = crim_entry.get()
    zn = zn_entry.get()
    indus = INDUS_entry.get()
    chas = CHAS_entry.get()
    nox = NOX_entry.get()
    rm = RM_entry.get()
    age = AGE_entry.get()
    dis = DIS_entry.get()
    rad = RAD_entry.get()
    tax = TAX_entry.get()
    ptrotio = PTRATIO_entry.get()
    b = B_entry.get()
    lstat = LSTAT_entry.get()
    
    values = [crim, zn, indus, chas, nox, rm, age, dis, rad, tax, ptrotio, b, lstat]
    pred = model.predict([values])
    pred = "Predicted value - "+str(pred[0])
    result = Label(root, text=pred).grid(row=14, columnspan=2)
    
    
root = Tk()

crim_label = Label(root, text="CRIM")
zn_label = Label(root, text="ZN")
INDUS_label = Label(root, text="INDUS")
CHAS_label = Label(root, text="CHAS")
NOX_label = Label(root, text="NOX")
RM_label = Label(root, text="RM")
AGE_label = Label(root, text="AGE")
DIS_label = Label(root, text="DIS")
RAD_label = Label(root, text="RAD")
TAX_label = Label(root, text="TAX")
PTRATIO_label = Label(root, text="PTRATIO")
B_label = Label(root, text="B")
LSTAT_label = Label(root, text="LSTAT")

crim_label.grid(row=0,column=0)
zn_label.grid(row=1, column=0)
INDUS_label.grid(row=2, column=0)
CHAS_label.grid(row=3, column=0)
NOX_label.grid(row=4, column=0)
RM_label.grid(row=5, column=0)
AGE_label.grid(row=6, column=0)
DIS_label.grid(row=7, column=0)
RAD_label.grid(row=8, column=0)
TAX_label.grid(row=9, column=0)
PTRATIO_label.grid(row=10, column=0)
B_label.grid(row=11, column=0)
LSTAT_label.grid(row=12, column=0)


crim_entry = Entry(root, width=40)
crim_entry.grid(row=0,column=1)
zn_entry = Entry(root, width=40)
zn_entry.grid(row=1,column=1)
INDUS_entry = Entry(root, width=40)
INDUS_entry.grid(row=2,column=1)
CHAS_entry = Entry(root, width=40)
CHAS_entry.grid(row=3,column=1)
NOX_entry = Entry(root, width=40)
NOX_entry.grid(row=4,column=1)
RM_entry = Entry(root, width=40)
RM_entry.grid(row=5,column=1)
AGE_entry = Entry(root,  width=40)
AGE_entry.grid(row=6,column=1)
DIS_entry = Entry(root,  width=40)
DIS_entry.grid(row=7,column=1)
RAD_entry = Entry(root, width=40)
RAD_entry.grid(row=8,column=1)
TAX_entry = Entry(root, width=40)
TAX_entry.grid(row=9,column=1)
PTRATIO_entry = Entry(root, width=40)
PTRATIO_entry.grid(row=10,column=1)
B_entry = Entry(root, width=40)
B_entry.grid(row=11,column=1)
LSTAT_entry = Entry(root, width=40)
LSTAT_entry.grid(row=12,column=1)

predict = Button(root, text="Predict house value", command=predict_value).grid(row=13, columnspan=2)

root.mainloop() 