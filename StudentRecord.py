from tkinter import *
from tkinter import ttk,messagebox
import time
import datetime
import random
import os
import tempfile

class StudentRecordHardCopy:
    def __init__(self,root):
        self.root = root
        self.root.title('Student Record System')
        self.root.geometry('1350x750+0+0')

        #===================================================variables================================================
        self.iDate=StringVar()
        self.iDate.set(time.strftime("%d/%m/%Y"))

        self.var1 = StringVar()
        self.var2 = StringVar()
        self.var3 = StringVar()
        self.var4 = IntVar()
        self.var5 = IntVar()
        self.var6 = IntVar()

        self.Firstname = StringVar()
        self.Surname = StringVar()
        self.Address = StringVar()
        self.PostCode = StringVar()
        self.Telephone = StringVar()
        self.Ref = StringVar()
        self.Date=StringVar()
        self.ULNumber = StringVar()
        self.RegNumber = StringVar()
        self.NextofNick = StringVar()
        self.StudentID = StringVar()
        self.StudentLoan = StringVar()
        self.Degree = StringVar()

        self.StudentLoan = StringVar()
        self.StudentLoan.set("0")
        self.InternationalFees=StringVar()
        self.InternationalFees.set("0")
        self.AccommodationFees=StringVar()
        self.AccommodationFees.set("0")

        #===================================================Frames================================================
        self.MainFrame=Frame(self.root)
        self.MainFrame.grid()

        self.Tops = Frame(self.MainFrame,bd=10,relief=RIDGE)
        self.Tops.pack(side=TOP)

        self.lblTitle=Label(self.Tops,width=30,font=('arial',39,'bold'),text='Student Record System',justify=CENTER)
        self.lblTitle.grid(padx=150)

        self.MemberName_F = LabelFrame(self.MainFrame,text='Student Name',bd=10,width=1300,height=400,relief=RIDGE,font=('arial', 12, 'bold'))
        self.MemberName_F.pack(padx=38,side=TOP)

        self.Receipt_buttonFrame = LabelFrame(self.MainFrame, text='Details', bd=10, width=1300, height=200,
                                       relief=RIDGE, font=('arial', 12, 'bold'))
        self.Receipt_buttonFrame.pack(padx=38, side=TOP)

        # ===================================================First column========================================

        self.lblStudentID = Label(self.MemberName_F, font=('arial', 16, 'bold'), text='StudentID',bd=7)
        self.lblStudentID.grid(row=0,column=0,sticky=W)
        self.txtStudentID = Entry(self.MemberName_F,font=('arial', 13, 'bold'),textvariable=self.StudentID,insertwidth=2,bd=7,state=DISABLED)
        self.txtStudentID.grid(row=0, column=1)

        self.lblFirstname = Label(self.MemberName_F, font=('arial', 16, 'bold'), text='First Name',  bd=7)
        self.lblFirstname.grid(row=1, column=0, sticky=W)
        self.txtFirstname = Entry(self.MemberName_F, font=('arial', 13, 'bold'), textvariable=self.Firstname,
                                  insertwidth=2, bd=7)
        self.txtFirstname.grid(row=1, column=1)

        self.lblSurname = Label(self.MemberName_F, font=('arial', 16, 'bold'), text='Surname', bd=7)
        self.lblSurname.grid(row=2, column=0, sticky=W)
        self.txtSurname = Entry(self.MemberName_F, font=('arial', 13, 'bold'), textvariable=self.Surname,
                                  insertwidth=2, bd=7)
        self.txtSurname.grid(row=2, column=1)

        self.lblAddress = Label(self.MemberName_F, font=('arial', 16, 'bold'), text='Address', bd=7)
        self.lblAddress.grid(row=3, column=0, sticky=W)
        self.txtAddress = Entry(self.MemberName_F, font=('arial', 13, 'bold'), textvariable=self.Address,insertwidth=2, bd=7)
        self.txtAddress.grid(row=3, column=1)

        self.lblPostCode = Label(self.MemberName_F, font=('arial', 16, 'bold'), text='Post Code', bd=7)
        self.lblPostCode.grid(row=4, column=0, sticky=W)
        self.txtPostCode = Entry(self.MemberName_F, font=('arial', 13, 'bold'), textvariable=self.PostCode,
                                  insertwidth=2, bd=7)
        self.txtPostCode.grid(row=4, column=1)

        self.CheckButtonLoan=Checkbutton(self.MemberName_F,text='Student Loan',variable=self.var4,onvalue=1,offvalue=0,
                                         font=('arial', 16, 'bold'),command=self.student_loan).grid(row=5, column=0,sticky=W)
        self.txtStudentLoan = Entry(self.MemberName_F, font=('arial', 13, 'bold'), textvariable=self.StudentLoan,
                                 insertwidth=2, bd=7,state=DISABLED,justify=RIGHT)
        self.txtStudentLoan.grid(row=5, column=1)

        # ===================================================2nd column========================================

        self.lblTelephone = Label(self.MemberName_F, font=('arial', 16, 'bold'), text='Telephone', bd=7)
        self.lblTelephone.grid(row=0, column=2, sticky=W)
        self.txtTelephone = Entry(self.MemberName_F, font=('arial', 13, 'bold'), textvariable=self.Telephone,
                                  insertwidth=2, bd=7)
        self.txtTelephone.grid(row=0, column=3)

        self.lblDate = Label(self.MemberName_F, font=('arial', 16, 'bold'), text='Date', bd=7)
        self.lblDate.grid(row=1, column=2, sticky=W)
        self.txtDate = Entry(self.MemberName_F, font=('arial', 13, 'bold'), textvariable=self.iDate,insertwidth=2,bd=7)
        self.txtDate.grid(row=1, column=3)

        self.lblProve_of_ID = Label(self.MemberName_F, font=('arial', 16, 'bold'), text='Prove Of ID', bd=7)
        self.lblProve_of_ID.grid(row=2, column=2, sticky=W)
        self.cboProve_of_ID = ttk.Combobox(self.MemberName_F, font=('arial', 13, 'bold'),state='readonly',textvariable=self.var1,width=19)
        self.cboProve_of_ID['value']=('','Pilot Licence','Driving Licence','Passport','Student ID')
        self.cboProve_of_ID.current(0)
        self.cboProve_of_ID.grid(row=2, column=3)

        self.lblType_of_Degree = Label(self.MemberName_F, font=('arial', 16, 'bold'), text='Address', bd=7)
        self.lblType_of_Degree.grid(row=3, column=2, sticky=W)
        self.cboType_of_Degree =ttk.Combobox(self.MemberName_F, font=('arial', 13, 'bold'), textvariable=self.var2,state='readonly',width=19)
        self.cboType_of_Degree['value'] = ('','Undergraduate', 'Postgraduate', 'Doctoral Degree')
        self.cboType_of_Degree.current(0)
        self.cboType_of_Degree.grid(row=3, column=3)

        self.lblMethod_of_Payment = Label(self.MemberName_F, font=('arial', 16, 'bold'), text='Method of Payment', bd=7)
        self.lblMethod_of_Payment.grid(row=4, column=2, sticky=W)
        self.cboMethod_of_Payment = ttk.Combobox(self.MemberName_F, font=('arial', 13, 'bold'), textvariable=self.var3,state='readonly',width=19)
        self.cboMethod_of_Payment['value'] = ('','Visa Card', 'Master Card', 'Debit Card','Cash')
        self.cboMethod_of_Payment.current(0)
        self.cboMethod_of_Payment.grid(row=4, column=3)

        self.CheckAccommodation = Checkbutton(self.MemberName_F, text='Accommodation', variable=self.var5, onvalue=1,
                                           offvalue=0,font=('arial', 16, 'bold'),command=self.Accomodation).grid(row=5, column=2, sticky=W)
        self.txtAccommodation = Entry(self.MemberName_F, font=('arial', 13, 'bold'), textvariable=self.AccommodationFees,
                                    insertwidth=2, bd=7, state=DISABLED, justify=RIGHT)
        self.txtAccommodation.grid(row=5, column=3)

    #=============================================3rd column====================================================
        self.lblRegNumber = Label(self.MemberName_F, font=('arial', 16, 'bold'), text='Reg Number', bd=7)
        self.lblRegNumber.grid(row=0, column=4, sticky=W)
        self.txtRegNumber = Entry(self.MemberName_F, font=('arial', 13, 'bold'), textvariable=self.RegNumber, insertwidth=2,
                                  bd=7, state=DISABLED)
        self.txtRegNumber.grid(row=0, column=5)

        self.lblULNumber = Label(self.MemberName_F, font=('arial', 16, 'bold'), text='ULN Number', bd=7)
        self.lblULNumber.grid(row=1, column=4, sticky=W)
        self.txtULNumber = Entry(self.MemberName_F, font=('arial', 13, 'bold'), textvariable=self.ULNumber,
                                  insertwidth=2, bd=7)
        self.txtULNumber.grid(row=1, column=5)

        self.lblNextOfNick = Label(self.MemberName_F, font=('arial', 16, 'bold'), text='Next of Nick', bd=7)
        self.lblNextOfNick.grid(row=2, column=4, sticky=W)
        self.txtNextOfNick = Entry(self.MemberName_F, font=('arial', 13, 'bold'), textvariable=self.NextofNick,
                                insertwidth=2, bd=7)
        self.txtNextOfNick.grid(row=2, column=5)

        self.lblAddress = Label(self.MemberName_F, font=('arial', 16, 'bold'), text='Address', bd=7)
        self.lblAddress.grid(row=3, column=4, sticky=W)
        self.txtAddress = Entry(self.MemberName_F, font=('arial', 13, 'bold'), textvariable=self.Address, insertwidth=2,
                                bd=7)
        self.txtAddress.grid(row=3, column=5)

        self.lblPostCode = Label(self.MemberName_F, font=('arial', 16, 'bold'), text='Post Code', bd=7)
        self.lblPostCode.grid(row=4, column=4, sticky=W)
        self.txtPostCode = Entry(self.MemberName_F, font=('arial', 13, 'bold'), textvariable=self.PostCode,
                                 insertwidth=2, bd=7)
        self.txtPostCode.grid(row=4, column=5)

        self.CheckMembership = Checkbutton(self.MemberName_F, text='International Student Fees', variable=self.var6, onvalue=1,
                                           offvalue=0,font=('arial', 16, 'bold'),command=self.International).grid(row=5, column=4, sticky=W)
        self.txtinternational = Entry(self.MemberName_F, font=('arial', 13, 'bold'), textvariable=self.InternationalFees,
                                    insertwidth=2, bd=7, state=DISABLED, justify=RIGHT)
        self.txtinternational.grid(row=5, column=5)

        #==================================================Text Area========================================
        self.txtReceipt=Text(self.Receipt_buttonFrame,width=181,height=10,font=('arial', 10, 'bold'))
        self.txtReceipt.grid(row=0,column=0,columnspan=4)
        self.txtReceipt.insert(END,"Student ID\t\t Firstname\t\t Surname\t\t Address\t\t Post Code\t\t Student Loan\t\t Telephone\t\t Date\t\t Degree\t\t ULN Number\t\t Next of Nick\t\n")

        # ==================================================Buttons========================================
        self.btnReceipt=Button(self.Receipt_buttonFrame,bd=7,text="Receipt",font=('arial', 16, 'bold'),width=13,command=self.Receipt).grid(row=1,column=0,pady=12)
        self.btnReset = Button(self.Receipt_buttonFrame, bd=7, text="Reset", font=('arial', 16, 'bold'),
                                 width=13,command=self.iReset).grid(row=1, column=1, pady=12)
        self.btnPrint = Button(self.Receipt_buttonFrame, bd=7, text="Print", font=('arial', 16, 'bold'),
                                 width=13,command=self.iPrint).grid(row=1, column=2, pady=12)
        self.btnExit = Button(self.Receipt_buttonFrame, bd=7, text="Exit", font=('arial', 16, 'bold'),
                                 width=13,command=self.iExit).grid(row=1, column=3, pady=12)

        #==============================================Functions=============================================
    def iExit(self):
        iexit = messagebox.askyesno('Quite System','Do You Want Quit?')
        if iexit >0:
            self.root.destroy()
            return
    def iPrint(self):
        q = self.txtReceipt.get('1.0','end-1c')
        filename=tempfile.mktemp(".txt")
        open(filename,'w').write(q)
        os.startfile(filename,'print')

    def iReset(self):
        jReset = messagebox.askyesno('Quite System', 'Do You Want Quit?')
        if jReset > 0:
            self.Firstname.set("")
            self.Surname.set("")
            self.Address.set("")
            self.PostCode.set("")
            self.Telephone.set("")
            self.Ref.set("")
            self.Date.set("")
            self.ULNumber.set("")
            self.RegNumber.set("")
            self.NextofNick.set("")
            self.StudentID.set("")
            self.StudentLoan.set("")

            self.var1.set("")
            self.var2.set("")
            self.var3.set("0")
            self.var4.set(0)
            self.var5.set(0)
            self.var6.set(0)

            self.StudentLoan.set("0")
            self.InternationalFees.set("0")
            self.AccommodationFees.set("0")

            self.txtStudentLoan.configure(state=DISABLED)
            self.txtinternational.configure(state=DISABLED)
            self.txtAccommodation.configure(state=DISABLED)

            self.cboProve_of_ID.current(0)
            self.cboType_of_Degree.current(0)
            self.cboMethod_of_Payment.current(0)
            self.Ref_No()
            self.txtReceipt.delete("2.0",END)
            return

    def Ref_No(self): #taking random number for student id
        self.Number_Ref=StringVar()
        x=random.randint(10908,500876)
        randomRef=str(x)
        self.Number_Ref.set(randomRef)
        self.StudentID.set(randomRef)

    def Receipt(self):
        self.Ref_No()
        self.txtReceipt.insert(END,self.StudentID.get()+ "\t\t" + self.Firstname.get()+ "\t\t" + self.Surname.get()+ "\t\t" + self.Address.get()+ "\t\t" + self.PostCode.get()+ "\t\t" + self.StudentLoan.get()+ "\t\t" + self.Telephone.get()+ "\t\t" + self.iDate.get()+ "\t\t" + self.var2.get()+ "\t\t" + self.ULNumber.get()+ "\t\t" + self.NextofNick.get()+ "\n")

    def student_loan(self):
        if self.var4.get()==1:
            self.txtStudentLoan.configure(state=NORMAL)
            item1=float(25550)
            self.StudentLoan.set("Rs"+str(item1))
            self.paid1=self.StudentLoan.get()
        elif self.var4.get()==0:
            self.txtStudentLoan.configure(state=DISABLED)
            self.StudentLoan.set(0)

    def Accomodation(self):
        if self.var5.get()==1:
            self.txtAccommodation.configure(state=NORMAL)
            item2=float(8000)
            self.AccommodationFees.set("Rs"+str(item2))
            self.paid2=self.StudentLoan.get()
        elif self.var5.get()==0:
            self.AccommodationFees.configure(state=DISABLED)
            self.StudentLoan.set(0)

    def International(self):
        if self.var6.get()==1:
            self.txtinternational.configure(state=NORMAL)
            item3=float(120000)
            self.InternationalFees.set("Rs"+str(item3))
            self.paid3=self.StudentLoan.get()
        elif self.var6.get()==0:
            self.txtinternational.configure(state=DISABLED)
            self.InternationalFees.set(0)




if __name__ == '__main__':
    root=Tk()
    application=StudentRecordHardCopy(root)
    root.mainloop()