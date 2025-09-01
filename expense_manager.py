import mysql.connector
import datetime
x=mysql.connector.connect(host="localhost",user="root",passwd="")

y=x.cursor()
y.execute("create database if not exists main")
y.execute("use main")
y.execute("create table if not exists logintable(USERNAME varchar(15),PASSWORD varchar(8))")

def signup():
    global tablevar
    username=input("ENTER USERNAME-> ")
    password=input("ENTER PASSWORD-> ")
    yn=input("CONFIRM? (Y/N)--> ")
    if yn.upper()=='Y':
        try:
            tablevar=username+'_account'
            crb="create table "+ tablevar +"(serial int not null auto_increment,account char(10),date date,category char(20),description char(150),pl CHAR(10),amount decimal(30,2),cheque char(20),primary key(serial))"
            y.execute(crb)
            crb="alter table "+tablevar+" auto_increment=10000"
            y.execute(crb)
            y.execute
            a="insert into logintable values('" + username + "','" + password + "')"
            y.execute(a)
            x.commit()
            login()
        except mysql.connector.errors.ProgrammingError:
            print("!!USERNAME ALREADY EXISTS!!")
            home()
    else:
        home()
    
def login():
    y.execute("select * from logintable")
    ft=y.fetchall()
    user=input("USERNAME-> ")
    passwd=input("PASSWORD-> ")
    d=[]
    e=[]
    for i in ft:
        q=i[0]
        w=i[1]
        d.append(q)
        e.append(w)
    if (user in d) and (passwd in e):
        global tabvar
        print("LOGGED IN SUCCESSFULLY!")
        print("WELCOME ",user)
        tabvar=user+"_account"
        Dashboard()
    else:
        print("!!INVALID USERNAME OR PASSWORD!!")
        yn=input("TRY AGAIN?(Y/N)-> ")
        if yn.upper()=="Y":
            login()
        elif yn.upper()=="N":
            home()
        else:
            print("ENTER VALID!!")
            home()
            
def Dashboard():
    y.execute("select * from "+tabvar+" ;")
    f=y.fetchall()
    L,P=0,0
    for i in f:
        if i[5]=='EXPENSE':
            L+=i[6]
        else:
            P+=i[6]
    S=P-L
    print("==========================================================================================================================")
    print("NEW TRANSACTION     ->  1\t\t\t\t|\t\t\tINCOME      = ",str(P).rjust(15))
    print("VIEW TRANSACTIONS   ->  2\t\t\t\t|\t\t\tEXPENSE     = ",str(L).rjust(15))
    print("UPDATE TRANSACTION  ->  3\t\t\t\t|\t\t\tNET BALANCE = ",str(S).rjust(15))
    print("DELETE TRANSACTIONS ->  4\t\t\t\t|")
    print("LOGOUT              ->  5\t\t\t\t|")
    print("==========================================================================================================================")
    inp=input("ENTER RESPONSE-> ")
    if inp=='1':
        addentry()
    elif inp=='2':
        view()
    elif inp=='3':
        update()
    elif inp=='4':
        delete()
        Dashboard()
    elif inp=='5':
        print("LOGGED OUT SUCCESSFULLY")
        home()
    else:
        print("ENTER VALID!")
        Dashboard()

def addentry():
    global amount
    global description
    global date
    
    addentry_proloss()
    addentry_cc()
    amount=input("ENTER AMOUNT                         -> ")
    addentry_category()
    description=input("ENTER DESCRIPTION                    -> ")
    date=input("ENTER DATE OF TRANSACTION(YYYY-MM-DD)-> ")
    addentry_finaladd()

def addentry_category():
    global des
    print("FOOD   - 1\tSOCIAL    - 4\t\tBEAUTY  - 7\tTRANSPORT - 10")
    print("CULTURE- 2\tHOUSEHOLD - 5\t\tAPPAREL - 8\tFESTIVAL  - 11")
    print("HEALTH - 3\tEDUCATION - 6\t\tGIFT    - 9\tOTHERS    - 12")
    cate=input("CHOOSE CATEGORY                      -> ")
    if cate=='1':
        des='FOOD..'
    elif cate=='2':
        des='CULTURE'
    elif cate=='3':
        des='HEALTH'
    elif cate=='4':
        des='SOCIAL'
    elif cate=='5':
        des='HOUSEHOLD'
    elif cate=='6':
        des='EDUCATION'
    elif cate=='7':
        des='BEAUTY'
    elif cate=='8':
        des='APPAREL'
    elif cate=='9':
        des='GIFT..'
    elif cate=='10':
        des='TRANSPORT'
    elif cate=='11':
        des='FESTIVAL'
    elif cate=='12':
        des='OTHERS'
    else:
        print("!INVALID!")
        addentry_category()

def addentry_finaladd():
    con=input("CONFIRM? (Y/N)--> ")
    if con.upper()=='Y':
        a="insert into "+tabvar+"(Account,date,category,description,pl,amount,cheque) values('" + c + "','" + date + "','" + des + "','" + description + "','" + pol +"'," + amount + ",'" + chequeno +"')"
        y.execute(a)
        x.commit()
        print("UPDATED SUCCESSFULLY!!")
        Dashboard()
    elif con.upper()=='N':
        addentry()
    else:
        print("!!ENTER VALID RESPONSE!!")
        addentry_finaladd()
    

def addentry_proloss():
    global pol
    pl=input("PRESS 1 FOR INCOME AND 2 FOR EXPENSE -> ")
    if pl=='1':
        pol="INCOME"
    elif pl=='2':
        pol="EXPENSE"
    else:
        print("!!ENTER VALID RESPONSE!!")
        addentry_proloss()

def addentry_cc():
    global c
    global chequeno
    p2=input("PRESS 1 FOR CASH AND 2 FOR CHEQUE    -> ")
    if p2=='1':
        c="  CASH"
        chequeno="NONE"
    elif p2=='2':
        c="CHEQUE"
        chequeno=input("ENTER CHEQUE NO                      -> ")
    else:
        print("!!ENTER VALID RESPONSE!!")
        addentry_cc()

def printmethod():
    y.execute(exe)
    ft=y.fetchall()
    print("--------------------------------------------------------------------------------------------------------------------------")
    print("SERIAL\t  ACCOUNT\t    DATE\t CATEGORY\t    DESCRIPTION\t\t   TYPE\t\t AMOUNT\t\tCHEQUE NO")
    print("--------------------------------------------------------------------------------------------------------------------------")
    for i in ft:
        de=''
        if len(i[4])>=15:
            for q in range(0,15):
                de=de+i[4][q]
            de=de+'..'
        else:
            qt=15-len(i[4])
            s=''
            for z in range(qt):
                s=s+' '
            de=s+i[4]
        xe=''
        pe=str(i[6])
        if len(pe)<6:
            xe=pe+'\t'
        else:
            xe=i[6]
        print(i[0],"\t",i[1],"\t",i[2],"\t",i[3],"\t",de,"\t",i[5],"\t",xe,"\t",i[7])
    

def view():
    global exe
    print("VIEW ALL TRANSACTIONS        -> 1")
    print("VIEW CUSTOMISED TRANSACTIONS -> 2")
    print("BACK TO Dashboard            -> 3")
    vinp=input("ENTER RESPONSE -> ")
    if vinp=='1':
        exe="select * from "+tabvar+" order by date desc;"
        y.execute(exe)
        ft=y.fetchall()
        if len(ft)==0:
            print("NO RECORDS WERE FOUND!!")
            view()
        printmethod()
        print(len(ft)," RECORDS.")
        
        view()
    elif vinp=='2':
        print("TRANSACTIONS BY DATE     -> 1")
        print("TRANSACTIONS BY CATEGORY -> 2")
        print("VIEW PARTICULAR RECORD   -> 3")
        print("BACK                     -> 4")
        v1inp=input("ENTER RESPONSE-> ")
        if v1inp=='1':
            view_date()
        elif v1inp=='2':
            view_category()
        elif v1inp=='3':
            view_detail()
        elif vlinp=='4':
            view()
        else:
            print("!!ENTER VALID RESPONSE!!")
            view()
    elif vinp=='3':
        Dashboard()
    else:
        print("!!ENTER VALID RESPONSE!!")
        view()

def view_detail():
    vd=input("ENTER THE SERIAL NUMBER OF RECORD TO BE VIEWED-> ")
    exe="select * from "+tabvar+" where serial="+vd+" ;"
    y.execute(exe)
    ft=y.fetchall()
    if len(ft)==0:
        print("!!NO RECORD FOUND!!")
        view()
    for i in ft:
        print("SERIAL      ->",i[0])
        print("ACOOUNT     ->",i[1])
        print("DATE        ->",i[2])
        print("CATEGORY    ->",i[3])
        print("DESCRIPTION ->",i[4])
        print("TYPE        ->",i[5])
        print("AMOUNT      ->",i[6])
        print("CHEQUE NO   ->",i[7])
    view()
def view_date():
    global exe
    startdate=input("ENTER START DATE(IN YY-MM-DD)-> ")
    stopdate=input("ENTER STOP DATE(IN YY-MM-DD) -> ")
    exe="select * from "+tabvar+" where date between'"+startdate+"' and '"+stopdate+"' order by date desc;"
    y.execute(exe)
    ft=y.fetchall()
    if len(ft)==0:
        print("NO RECORDS WERE FOUND!!")
        view()
    printmethod()
    print("\n")
    view()
    
def view_category():
    global exe
    addentry_category()
    exe="select * from "+tabvar+" where category='"+des+"' order by date desc;"
    y.execute(exe)
    ft=y.fetchall()
    if len(ft)==0:
            print("NO RECORDS WERE FOUND!!")
            view()
    printmethod()
    print("\n")
    view()

def update():
    global exe
    print("SEARCH VIA PARTICULAR DATE -> 1")
    print("SEARCH IN ALL TIME RECORD  -> 2")
    print("DASHBOARD                  -> 3")
    uinp=input("ENTER RESPONSE-> ")
    if uinp=='1':
        u1inp=input("ENTER NEW DATE(IN YY-MM-DD)->  ")
        exe="select * from "+tabvar+" where date='"+u1inp+"';"
        y.execute(exe)
        ft=y.fetchall()
        if len(ft)==0:
            print("NO RECORDS WERE FOUND!!")
            update()
        printmethod()
        print("\n")
    elif uinp=='2':
        exe="select * from "+tabvar+";"
        y.execute(exe)
        ft=y.fetchall()
        if len(ft)==0:
            print("NO RECORDS WERE FOUND!!")
            update()
        printmethod()
        print("\n")
    elif uinp=='3':
        Dashboard()
    else:
        update()
    u2inp=input("ENTER THE SERIAL NUMBER OF RECORD TO BE UPDATED-> ")
    print("SELECT COLUMN TO BE UPDATED")
    print("ACCOUNT/CHEQUE NO-> 1\t DATE       -> 2\t CATEGORY-> 3")
    print("DESCRIPTION      -> 4\t PROFIT/LOSS-> 5\t AMOUNT  -> 6")
    u3inp=input("ENTER RESPONSE -> ")
    if u3inp=='1':
        addentry_cc()
        exe="update "+tabvar+" set cheque='"+chequeno+"',account='"+c+"' where serial="+u2inp+";"
        y.execute(exe)
        x.commit()
        print("UPDATED SUCCESSFULLY!!")
    elif u3inp=='2':
        udate=input("ENTER NEW DATE(IN YY-MM-DD) -> ")
        exe="update "+tabvar+" set date='"+udate+"' where serial="+u2inp+";"
        y.execute(exe)
        x.commit()
        print("UPDATED SUCCESSFULLY!!")
    elif u3inp=='3':
        addentry_category()
        print(des)
        exe="update "+tabvar+" set category='"+des+"' where serial="+u2inp+";"
        y.execute(exe)
        x.commit()
        print("UPDATED SUCCESSFULLY!!")
    elif u3inp=='4':
        udescription=input("ENTER NEW DESCRIPTION-> ")
        exe="update "+tabvar+" set description='"+udescription+"' where serial="+u2inp+";"
        y.execute(exe)
        x.commit()
        print("UPDATED SUCCESSFULLY!!")
    elif u3inp=='5':
        addentry_proloss()
        exe="update "+tabvar+" set pl='"+pol+"' where serial="+u2inp+";"
        y.execute(exe)
        x.commit()
        print("UPDATED SUCCESSFULLY!!")
    elif u3inp=='6':
        uamount=input("ENTER NEW AMOUNT-> ")
        exe="update "+tabvar+" set amount='"+uamount+"' where serial="+u2inp+";"
        y.execute(exe)
        x.commit()
        print("UPDATED SUCCESSFULLY!!")
    update()


def delete():
    global exe
    print("SEARCH VIA PARTICULAR DATE -> 1")
    print("SEARCH IN ALL TIME RECORD  -> 2")
    print("DASHBOARD                  -> 3")
    dinp=input("ENTER RESPONSE-> ")
    if dinp=='1':
        d1inp=input("ENTER NEW DATE(IN YY-MM-DD)-> ")
        exe="select * from "+tabvar+" where date='"+d1inp+"';"
        y.execute(exe)
        ft=y.fetchall()
        if len(ft)==0:
            print("NO RECORDS WERE FOUND!!")
            delete()
        printmethod()
        print("\n")
    elif dinp=='2':
        exe="select * from "+tabvar+";"
        y.execute(exe)
        ft=y.fetchall()
        if len(ft)==0:
            print("NO RECORDS WERE FOUND!!")
            delete()
        printmethod()
        print("\n")
    elif dinp=='3':
        Dashboard()
    else:
        print("!!ENTER VALID RESPONSE!!")
        delete()
    d2inp=input("ENTER THE SERIAL NUMBER OF RECORD TO BE DELETED -> ")
    exe="delete from "+tabvar+" where serial="+d2inp+";"
    y.execute(exe)
    x.commit()
    print("RECORD DELETED SUCCESSFULLY")
    delete()

def home():
    print("================================================WELCOME TO DAILY EXPENSE MANAGER==========================================")
    print("TO LOGIN PRESS   ->  1")
    print("TO SIGNUP PRESS  ->  2")
    print("==========================================================================================================================")
    inp=input("ENTER RESPONSE-> ")
    if inp=='1':
        login()
    elif inp=='2':
        signup()
    else:
        print('INVALID! TRY AGAIN')
        home()
home()
























