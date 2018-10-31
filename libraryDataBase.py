#nPLUS CoDec$ : Programmer  ---> Naresh Kumar for Glosys Technology Pvt.Ltd
import sqlite3 as s
import time
from datetime import datetime,timedelta
from getpass import getpass
import os


wire=s.connect('Library.db')
c=wire.cursor()
localtime = time.asctime( time.localtime(time.time()) )


class updation:
    def updatTabledecrease(self,bokname,authn,isb):
        Bokcount=0
        c.execute("select BookCopies,BookName,BookAuthor,ISBNnumber from books")
        for row in c.fetchall():
            if row[1] == bokname and row[2] == authn and row[3] == isb:Bokcount=row[0]-1
        c.execute("update books set BookCopies=? where BookName=? and BookAuthor=? and ISBNnumber=?",(Bokcount,bokname,authn,isb));wire.commit()
    def updateTableIncrease(self,ReBookData,ReBookAuth):
        Bokcount=0
        c.execute("select BookCopies,BookName,BookAuthor from books")
        for row in c.fetchall():
            if row[1] == ReBookData and row[2] == ReBookAuth:Bokcount = row[0]+1
        c.execute("update books set BookCopies=? where BookName=? and BookAuthor=?",(Bokcount,ReBookData,ReBookAuth));wire.commit()
    def updateAdminBoks(self):
        ExistingBook,ExistingAuth = input("Enter The Existig Book Name and Author Name : ").split(',')
        countt = int(input("Enter The Number of Books to Add: "))
        BokCount=0;c.execute("select BookCopies,BookName,BookAuthor from books")
        for row in c.fetchall():
            if row[1] == ExistingBook and row[2] == ExistingAuth:BokCount =row[0]+countt
        c.execute("update books set BookCopies=? where BookName=? and BookAuthor=?",(BokCount,ExistingBook,ExistingAuth));wire.commit()
    def finefun():
            rtime = datetime.now().strftime("%d-%")



class data:
    def student(self):
        print("<<<<<<<<<<<<<<<      Student Portal      >>>>>>>>>>\n")
        while 1:
            print("First Time Users of the Library are required to Register First.. \n1 --> Register\n2 --> Login\n")
            log = input("Enter Your Choice : ")
            if (log == "Register" or log == "1"):print("Register by Providing all details..\n");l.EntryStudentTable();os.system('clear')
            elif(log == "Login" or log  == "2"):os.system('clear');print(":::::::::::::::::LoGiN_PorTaL::::::::::::::");l.UserNameCheck()
            else:return 0
    def admin(self):
        print("<<<<<<<<<< Admin Portal >>>>>>>>>>\n")
        cipher = getpass("Enter admin cipher: ")
        if cipher == "nplus12.3":
            print("\nYou are a $uper User....\n\n")
            while 1:
                log = input("\nRegister New Books --> Press 1\nMonitor Students ----> Press 2\nMonitor Books -------> Press 3\nBorrowed Books  -----> Press 4\nAdd the strength Existing Books --> Press 5\nYour Choice :")
                if (log == "Register" or log == "1"):
                    count = int(input("Registering new books~\nEnter the Number of Books going to Register : "));
                    for i in range(count):print("book Entry - ",i+1,sep="");l.EntryBookTable()
                    print("Pause and ponder while registering new books\n")
                if (log == "Monitor Students" or log == "2" ):os.system('clear');print("Monitor students~\nStudent Name || Department || Register Number || User name || Member Ship Plan ||");l.showStudentTable()
                elif(log == "Monitor Books" or log == "3"):os.system('clear');print("Book Name | Department | Author Name | ISBN Number |Number of Copies");l.showBookTable()
                elif(log == "Borrowed Book Data" or log == "4"):os.system('clear');print("Borrow Book Data\nBorrower Name ||  Book Name || Author Name || Borrowed Time || Borrowed Date || Renew Date || User Name || ISBN Number");l.showBorrwBokTable()
                elif (log == "5"):os.system('clear');print("Adding Existing Books~");l.updateAdminBoks()
                elif(log == "exit" or log == "0"):return 0
        else:print("You Entered a Wrong Password...")



class portals(data,updation):
    varUser,varUserName,fla,planing="","",0,""
    def EntryBookTable(self):
        c.execute("CREATE TABLE IF NOT EXISTS books (BookName TEXT,BookDept Text,BookAuthor TEXT,ISBNnumber INTEGER,BookCopies INTEGER,BookPrice INTEGER)")
        bookname,dept,author,isbn,copies,bookPrice=input("Enter The BookName : "),input("Enter the Department : "),input("Enter Author Name: "),int(input("Enter the ISBN Number: ")),int(input("Enter The Number of Copies of the Book: ")),int(input("Enter The Price of the Book : ₹."))
        c.execute("INSERT INTO books(BookName,BookDept,BookAuthor,ISBNnumber,BookCopies,BookPrice) VALUES(?,?,?,?,?,?)",(bookname,dept,author,isbn,copies,bookPrice))
        wire.commit()
    def showBookTable(self):
            c.execute("SELECT * FROM books");[print(*x,sep="  ||  ",end="\n\n") for x in c.fetchall()]
    def showBorrwBokTable(self):
        c.execute("SELECT * FROM BorrowBookData");[print(*x,sep=" || ",end="\n\n") for x in c.fetchall()]
    def showStudentTable(self):
        c.execute("SELECT * FROM Students");[print(*x) for x in c.fetchall()]
    def EntryStudentTable(self):
        c.execute("CREATE TABLE IF NOT EXISTS Students (StudentName TEXT,Dept Text,RegisterNumber INTEGER,UserName TEXT,Password TEXT,MembershipPlans TEXT)");wire.commit();x=3
        t=3
        while t>0:
            d = int(input('''Member Ship Plans :
                    1.Classic Reading
                    2.Standard Reading
                    3.Premium  Reading
                    choice = '''))
            if d == 1:print('''You are Limited to Take Books of Price Within ₹999''');t-=1
            elif d == 2:print("You Have Advantage of borrowing books of prices above ₹999 and below ₹2500");t-=1
            elif d == 3:print('''You are the premium user of the Library,You Can borrow the Books independent of prices 
                                and return with extend time period...''');t-=1
            if d == 0:break
        while x>0:
            name,dept,reg_no,memplans,usr_name,password,conf_pass = input("Enter The Name : "),input("Enter The Department : "),int(input("Enter the Register Number : ")),input("Enter The Membership Plan You Needed: "),input("Create Your UserName : "),getpass("Create Your password: "),getpass("Confirm Password : ")
            if password == conf_pass:c.execute("INSERT INTO Students (StudentName,Dept,RegisterNumber,UserName,Password,MembershipPlans) VALUES(?,?,?,?,?,?)",(name,dept,reg_no,usr_name,password,memplans));wire.commit();x=0
            else:print("passwords mismatch");x-=1
    def UserNameCheck(self):
        user_name = input("Enter Your User Name : ");portals.varUserName = user_name
        c.execute("SELECT UserName,StudentName FROM Students");f=0
        for row in c.fetchall():
            if user_name == row[0]:
                portals.varUser=row[1]
                for i in range(3):
                    time.sleep(1)
                    hashj = getpass("\n\nUserName Exists...\nEnTer Your Password: ");l.passwordCheck(hashj);f=1
                    if portals.fla == 1:return 0
        if f==0:print("User Name Does Not Exists Please Register your name in our Library..")
    def passwordCheck(self,hashj):
        c.execute("SELECT Password,MembershipPlans FROM Students");flag=0
        for row in c.fetchall():
            if hashj == row[0]:print("LOGIN Successfully...\n");portals.planing = row[1];flag=1
        if flag==1:print("Name : ",portals.varUser,"\nUser Name :",portals.varUserName,"\nBook Name | Department | Author Name | ISBN Number |Number of Copies");l.showBookTable();l.BorrowReturn()
        else:print("You have Entered Wrong password...")
    def BorrowReturn(self):
        option = input("1 --->Borrow\n2 ---->Return\nYour Choice : ")
        if ((option == "1") or (option == "Borrow")):
            count = int(input("Enter The Number of Books Your Going to Borrow : "))
            for i  in range(count):
                os.system('clear');print("Borrow Menu ~\n\n");l.BorrwBook(localtime)
        elif ((option ==  "2") or (option == "Return")):print("Return Menu ~\n\n");l.ReturnBook()
        elif(option == "0"):return 0
    def BorrwBook(self,localtime):
        temp=[]
        c.execute("CREATE TABLE IF NOT EXISTS BorrowBookData(Name TEXT,BookName TEXT,AuthorName TEXT,BorrowTime TEXT,BorrowDate TEXT,RenewTime TEXT,UserName TEXT,bookISBN INTEGER)")
        bookQuery,AuthQuery = input("Enter The Book Name and Author Name : ").split(",")
        c.execute("select * from books")
        for row in c.fetchall():
            if bookQuery == row[0]:
                print("Book is Available Searching for Requested Author...");time.sleep(1)
                if AuthQuery == row[2]:
                    print("The Requested Book of Desired Author is Available...");[temp.append(i) for i in row];l.BorrowProcess(temp,localtime);return 0
                else:
                    x=input("Book is Available,Try Different Author..\nPress 1 if you want to Search other Author :")
                    if x=="1":l.BorrwBook(localtime)
    def BorrowProcess(self,temp,localtime):
        BorrowerName,tempUser = portals.varUser,portals.varUserName
        bokname,authn,isb = temp[0],temp[2],temp[3]
        varBorrowTime = datetime.now().strftime("%d-%m-%y")
        if portals.planing == "Premium":addDate = 10
        elif portals.planing == "Standard":addDate = 5
        elif portals.planing == "Classic":addDate = 3
        varRenewTime = (datetime.now()+ timedelta(days = addDate)).strftime("%d-%m-%y")
        c.execute("INSERT INTO BorrowBookData(Name,BookName,AuthorName,BorrowTime,BorrowDate,RenewTime,UserName,bookISBN) VALUES(?,?,?,?,?,?,?,?)",(BorrowerName,bokname,authn,localtime,varBorrowTime,varRenewTime,tempUser,isb));print(localtime);portals.fla = 1;wire.commit()
        l.updatTabledecrease(bokname,authn,isb)
        return portals.fla
    
    def ReturnBook(self):
        c.execute("SELECT * FROM BorrowBookData")
        [print("You have Borrowed ",row[1], '@', row[3]) for row in c.fetchall() if portals.varUser == row[0]]
        x = int(input("Enter The Number of Books You Are Going to Return : "))
        for i in range(x):
            ReBookData,ReBookAuth = input("Enter The Book Name,Author Name : ").split(',')
            c.execute("SELECT * from BorrowBookData")
            for row in c.fetchall():
                if (row[0]  == portals.varUser) and (row[1] == ReBookData) and (row[2] == ReBookAuth):
                    c.execute("DELETE FROM BorrowBookData Where Name=? and BookName=? and AuthorName=?",(portals.varUser,ReBookData,ReBookAuth));wire.commit()
                    #l.finefun()
                    l.updateTableIncrease(ReBookData,ReBookAuth)


if __name__ == "__main__":
    os.system('clear')
    l =  portals()
    time.sleep(1);print("\n\n_____________nPLUS TecHnoLoGiCaL LiBraRy_______________\n")
    key = 1
    while key:
        ch=input("Are You Student if Yes Press ---------> 2\nIf You are a Admin of Library Press --> 1\n\nYour Option : ")
        if (ch == "admin" or ch == "ADMIN" or ch == "1"):
            print("Welcome Mr.Librarian....\n");l.admin()
        elif (ch == "student" or ch == "STUDENT" or ch == "2"):
            print("Welcome Student....\n ");l.student()
        elif(ch == "0"):key = 0
        else:
            print("Enter The Appropriate Choice...!!!!\n\n")
