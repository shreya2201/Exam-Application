import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",passwd="redhat",database="MLdb")
mycursor = mydb.cursor()

def adminLogin(name):
    print("welcome admin, ",name)
    print("Choose your options")
    print("1. List all the questions")
    print("2. Add the questions graphically")
    print("3. Add questions through sql query")
    
    opt = int(input())
    
    if opt == 1:
        mycursor.execute("select * from questions");
        res = mycursor.fetchall()
        print(result)
        
    if opt == 2:
        question = input("enter the question")
        option1 = input("Enter option 1 ")
        option2 = input("Enter option 2 ")
        option3 = input("Enter option 3 ")
        option4 = input("Enter option 4 ")
        correct = int(input("Enter the correct ans "))
        technology = input("Enter the technology of the question ")
        mycursor.execute("insert into question (question, option1,option2,option3,option4, correct, technology) values ('{}','{}','{}','{}','{}',{},'{}')".format(question, option1,option2,option3,option4, correct, technology))
        mydb.commit()
        
    if opt == 3:
        response = input("Enter the query")
        mycursor.execute(response)
        mydb.commit()
        
def userLogin(name):
    count = 0
    print("Welcome student ", name)
    print("Do you want to take the test (y/n)?")
    res = input("Enter your choice : ")
    if(res == 'y'):
        mycursor.execute("select * from question")
        result = mycursor.fetchall()
        print(result)
        for i in result:
        
            print(i[0] ," ", i[1])
            print(i[2])
            print(i[3])
            print(i[4])
            print(i[5])
            user_response = int(input())
            if user_response == i[6]:
                count = count + 1
            print("--------------------------------------------------")
            print("--------------------------------------------------")
    print("Thank you for taking the test")
    print("your score is ", count)
    
def main():
    while(True):
        print("Choose an option")
        print("1. Create admin account")
        print("2. Create user account")
        print("3. Admin Login")
        print("4. User Login")
        print("5. exit")
        try:
            option = int(input())
            if(option > 5 or option < 1):
                print("invalid option")
        except Exception:
            print("invalid option")

        if option == 1:
            aname = input("Enter your name :")
            apassword = input("Enter your password :")
            mycursor.execute("insert into adminacc (name, password) values ('{}','{}')".format(aname,apassword))
            mydb.commit()
            
        if option == 2:
            uname = input("Enter your name :")
            upassword = input("Enter your password :")
            mycursor.execute("insert into useracc (name, password) values ('{}','{}')".format(uname,upassword))
            mydb.commit()
            
        if option == 3:
            al_name = input("Enter your name :")
            al_password = input("Enter your password :")
            mycursor.execute("select * from adminacc where name = '{}' and password = '{}'".format(al_name,al_password))
            result = mycursor.fetchone()
            if result != None:
                print(type(result))
                print("Admin logged in")
                adminLogin(al_name)
            else:
                print("please enter valid user name and password")
                main()
            break
            
        if option == 4:
            ul_name = input("Enter your name :")
            ul_password = input("Enter your password :")
            mycursor.execute("select * from useracc where name = '{}' and password = '{}'".format(ul_name,ul_password))
            result = mycursor.fetchone()
            if result != None:
                print(type(result))
                print(result)
                print("User logged in")
                userLogin(ul_name)
            else:
                print("please enter valid user name and password")
                main()
            break
        
        if option == 5:
            print(" Thank you for using the platform! bye-bye")
            break
            
main()

