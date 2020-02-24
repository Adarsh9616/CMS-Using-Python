import CMS_OOPS
from tkinter import *
from tkinter import messagebox

def btnAddClick():
    cus=CMS.Customer()
    cus.id=varid.get()
    cus.age=varage.get()
    cus.name=varname.get()
    cus.addCostumer()
    messagebox.showinfo("CMS","Customer Added Successfully")
    varid.set("")
    varage.set("")
    varname.set("")


def btnSearchClick():
    cus=CMS.Customer()
    cus.id=varid.get()
    cus.searchCostumer()
    varage.set(cus.age)
    varname.set(cus.name)
    messagebox.showinfo("CMS", "Search Successful")



def btnDeleteClick():
    cus=CMS.Customer()
    cus.id=varid.get()
    cus.deleteCostumer()
    messagebox.showinfo("CMS", "Customer Deleted Successfully")
    varname.set("")
    varage.set("")
    varname.set("")


def btnModifyCLick():
    cus = CMS.Customer()
    cus.id = varid.get()
    cus.age = varage.get()
    cus.name = varname.get()
    cus.modifyCostumer()
    messagebox.showinfo("CMS", "Customer Modified Successfully")
    varname.set("")
    varage.set("")
    varname.set("")


def btnDisplayClick():
    root1=Tk()
    lablid1 = Label(root1, text="Customer Id:", font=1,bg="light Blue",width=20)
    lablid1.grid(row=0, column=0, padx=2, pady=2)
    lablage1 = Label(root1, text="Customer Age:", font=1,bg="lightBlue",width=20)
    lablage1.grid(row=0, column=1, padx=2, pady=2)
    lablname1 = Label(root1, text="Customer Name:", font=1,bg="light Blue",width=20)
    lablname1.grid(row=0, column=2, padx=2, pady=2)
    i=1
    for e in CMS.Customer.cuslist:
        lablid2 = Label(root1, text=f"{e.id}", font=1, bg="Yellow", width=20)
        lablid2.grid(row=i, column=0, padx=2, pady=2)
        lablage2 = Label(root1, text=f"{e.age}", font=1, bg="Yellow", width=20)
        lablage2.grid(row=i, column=1, padx=2, pady=2)
        lablname2 = Label(root1, text=f"{e.name}", font=1, bg="Yellow", width=20)
        lablname2.grid(row=i, column=2, padx=2, pady=2)
        i+=1

def btnSaveClick():
    cus = CMS.Customer()
    cus.savetoPickle()
    messagebox.showinfo("CMS", "Saved Successfully")

def btnLoadClick():
    cus = CMS.Customer()
    cus.loadfromPickle()
    messagebox.showinfo("CMS", "Loaded Successfully")

root = Tk()

root.geometry("500x400")

lablid = Label(root, text="Enter Cust Id:", font=1)
lablid.grid(row=0, column=0,padx=2,pady=2)

lablage = Label(root, text="Enter Cust Age:", font=1)
lablage.grid(row=1, column=0,padx=2,pady=2)

lablname = Label(root, text="Enter Cust Name:", font=1)
lablname.grid(row=2, column=0,padx=2,pady=2)

varid = StringVar()
entrid = Entry(root, textvariable=varid, font=1)
entrid.grid(row=0, column=1,padx=2,pady=2)

varage = StringVar()
entrage = Entry(root, textvariable=varage, font=1)
entrage.grid(row=1, column=1,padx=2,pady=2)

varname = StringVar()
entrname = Entry(root, textvariable=varname, font=1)
entrname.grid(row=2, column=1,padx=2,pady=2)

btnaddcust = Button(root, text="Add Customer", font=1, command=btnAddClick ,width=20)
btnaddcust.grid(row=3, column=0,padx=2,pady=2)

btnsearchcust = Button(root, text="Search Customer", font=1, command=btnSearchClick,width=20)
btnsearchcust.grid(row=3, column=1,padx=2,pady=2)

btndeletecust = Button(root, text="Delete Customer", font=1, command=btnDeleteClick,width=20)
btndeletecust.grid(row=4, column=0,padx=2,pady=2)

btnmodifycust = Button(root, text="Modify Customer", font=1, command=btnModifyCLick,width=20)
btnmodifycust.grid(row=4, column=1,padx=2,pady=2)

btnallcust = Button(root, text="All Customer", font=1, command=btnDisplayClick,width=20)
btnallcust.grid(row=5, column=0,padx=2,pady=2)

btnsave = Button(root, text="Save in Pickle", font=1, command=btnSaveClick,width=20)
btnsave.grid(row=5, column=1,padx=2,pady=2)

btnload = Button(root, text="Load from Pickle", font=1, command=btnLoadClick,width=20)
btnload.grid(row=6, column=1,padx=2,pady=2)
root.mainloop()
