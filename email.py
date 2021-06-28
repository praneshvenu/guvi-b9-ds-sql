import mysql.connector
import re
con=mysql.connector.connect(host="localhost",user="root",password="",database="emailaccount")
res=con.cursor()
if res:
    print("mysql is connected")
else:
    print("error")
def register(user_name,email_id,password,password1):
    res = con.cursor()
    sql = "select * from accounts where email_id=%s"
    accounts=(email_id,)
    res.execute(sql,accounts)
    result=res.fetchall()
    con.commit()
    if not result:
        if (password == password1):
            l, u, s, d = 0, 0, 0, 0
            if len(password) >= 5 and len(password) <= 16:
                for i in password:
                    if (i.islower()):
                        l += 1
                    if (i.isupper()):
                        u += 1
                    if (i.isdigit()):
                        d += 1
                    if (i == "@" or i == "#" or i == "$" or i == "%" or i == "^" or i == "&" or i == "!" or i == "`" or i == "~"):
                        s += 1
            if (l >= 1 and u >= 1 and s >= 1 and d >= 1):
                   res = con.cursor()
                   sql = "insert into accounts(user_name,email_id,password) values (%s,%s,%s)"
                   accounts = (user_name, email_id, password)
                   res.execute(sql, accounts)
                   con.commit()
                   print("register success")
            else:
                print("invalid password please try again")
        else:
            print("Password doesn't match!,try again")
    else:
        print("Email already exit!")
def login(email_id,password):
    res = con.cursor()
    sql = "select * from accounts where email_id=%s and password=%s"
    accounts = (email_id, password,)
    res.execute(sql, accounts)
    result = res.fetchone()
    con.commit()
    if result:
        print("login success")
    else:
        print("invalid email or password")
def forgotpassword(email_id):
        res = con.cursor()
        sql = "select password from accounts where email_id=%s"
        accounts = (email_id,)
        res.execute(sql, accounts)
        result = res.fetchone()
        con.commit()
        if result:
            print("Your password : ")
            print(result)
        else:
            print("Username Not Found! \n    Please Register Yourself..")
while (True):
    print("Do you have an account? \n    Please enter your choice 1.'Yes' (0r) 2.'No' (0r)\nIf you press 3.'forgotpassword'")
    choice=int(input("Enter your choice: "))
    if choice==1:
        email_id=input("Enter Your Email_id: ")
        password=input("Enter Your Password: ")
        login(email_id,password)
    elif choice==2:
        print("Please Register...")
        user_name = input("Enter Your Name: ")
        email_id  = input("Create Your Email: ")
        pattern = r"\"?([-a-zA-Z0-9.`?{}]+@\w+\.\w+)\"?"
        if not re.match(pattern,email_id):
            print("invalid email,try again")
            break
        password  = input("Enter New Password: ")
        password1 = input("Enter Confirm Password: ")
        register(user_name,email_id,password,password1)
    elif choice == 3:
        email_id = input("Enter Your Email: ")
        forgotpassword(email_id)
    else:
        print("-*-*-Thank You-*-*-")
        exit()
