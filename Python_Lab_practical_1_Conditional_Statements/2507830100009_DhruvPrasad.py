print ("="*50)
print ("="*50)
print ("SMARTCAMPUS UTILITY & ACCESS PASS GENERATOR")
print ("="*50)
print ("="*50)

base_fee = 0
parking_fee = 0
peak_surchage = 0
electricity_fee = 0
electricity_unit = 0


print ("1.student")
print ("2.faculty/staff")
ch = int (input("choice the category from the given option above :"))

print("="*50)
if (ch==1):
    name = input ("Enter your name :")
    age = int(input("Enter your age :"))
    if (age<0 or age>100):
        print("[ERROR] Age must be between 0 and 100.")
        exit()
    roll_number = int (input ("Enter the roll no :"))
    if roll_number <= 0:
        print("[ERROR] Roll number must be positive.")
        exit()
    CGPA = float(input("Enter the CGPA(CGPA should be between 0.0 to 10.0 :)"))
    if CGPA < 0 or CGPA > 10:
        print("[ERROR] CGPA must be between 0.0 and 10.0")
        exit()
    cl= input ("Enter class from the (A,B,C,D,E) :")
    if cl not in ["A", "B", "C", "D", "E"]:
        print("[ERROR] Invalid class.")
        exit()


    print("1.UG")
    print("2.PG")
    sub_cateogry = int (input("choice the sub cateogry from the above option :"))
    if (sub_cateogry==1):
        base_fee = 500
        merit_discount = 0
        d = 0
        if (CGPA>=8.5):
            d = 20
            merit_discount= base_fee*0.2
        elif CGPA >= 7.5:
            d = 10
            merit_discount = base_fee * 0.10
        elif (CGPA<0):
            print ("[ERROR] cgpa cannot be negative")
    elif(sub_cateogry==2):
        base_fee = 350
        merit_discount = 0
        d = 0
        if (CGPA>=8.5):
            d = 20
            merit_discount= base_fee*0.2
        elif CGPA >= 7.5:
            d = 10
            merit_discount = base_fee * 0.10
        elif (CGPA<0):
            print ("[ERROR] cgpa cannot be negative")
    else:
     print("[ERROR] Invalid student category.")
     exit()


    print ("Do you own a vehicle y/n :")
    option = input().lower()
    if (option=="y"):
        print("1.Two wheeler")
        print("2.Four wheeler")
        vehicle = int (input ("enter the option given above"))
        if (vehicle==1):
            parking_fee = 200
        elif (vehicle==2):
            parking_fee = 600
            peak_surchage = 150
        else:
            print ("[ERROR]")
            exit()

    elif (option=="n"):
        parking_fee = 0
    else:
         print("[ERROR] Invalid vehicle option.")
         exit()


    print ("Do you live in hostile y/n :")
    hostile = input().lower()
    if (hostile == "y"):
        print ("give the number of electricity you consumed every month (in kwh):")
        electricity_unit = int(input())
        if electricity_unit < 0:
            print("[ERROR] Electricity consumption cannot be negative.")
            exit()
        elif electricity_unit <= 100:
              electricity_fee = electricity_unit * 3.00 + 50
        elif electricity_unit <= 300:
             electricity_fee = electricity_unit * 5.00 + 100
        elif electricity_unit <= 500:
             electricity_fee = electricity_unit * 7.50 + 150
        else:
            electricity_fee = electricity_unit * 10.00 + 250
    elif (hostile == "n"):
        print()
        electricity_unit = 0
        electricity_fee = 0
    else:
        print("[ERROR] Please enter y or n.")
        exit()


elif(ch==2):
    name = input ("Enter your name :")
    age = int(input("Enter your age :"))
    if (age<0 or age>100):
        print("[ERROR] Age must be between 0 and 100.")
        exit()
    subject = input ("Enter the subject you teach :")
    year = int(input("Enter for how many year you're teach at the college :"))
    if (year<0):
        print ("[ERROR] year cannot be negative so re-enter the year of service")
        year = int(input("Enter for how many year you're teach at the college :"))
    print("1.resident faculty")
    print("2.visiting / Guest faculty")
    sub_cateogry = int (input("choice the sub cateogry you teach to from the above option :"))
    if (sub_cateogry==1):
        base_fee = 800
        merit_discount = 0
        d = 0
        if (year>10):
            d = 15
            merit_discount = base_fee*0.15
    elif (sub_cateogry == 2):
        base_fee = 1200
        merit_discount = 0
        d = 0
        if (year>10):
            d= 15
            merit_discount = base_fee*0.15
    else:
     print("[ERROR] Invalid student category.")
     exit()

    
    print ("Do you own a vehicle y/n :")
    option = input().lower()
    if (option=="y"):
        print("1.Two wheeler")
        print("2.Four wheeler")
        vehicle = int (input ("enter the option given above :"))
        if (vehicle==1):
            parking_fee = 200
        elif (vehicle==2):
            parking_fee = 600
        else:
            print ("[ERROR]")
            exit()
    elif (option=="n"):
        parking_fee = 0
    else:
            print("[ERROR] Invalid vehicle option.")
            exit()
            


    print ("Do you live in quarter y/n :")
    quarter = input().lower()
    if (quarter == "y"):
        print ("give the number of electricity you consumed every month (in kwh):")
        electricity_unit = int(input())
        if electricity_unit < 0:
            print("[ERROR] Electricity consumption cannot be negative.")
            exit()
        elif electricity_unit <= 100:
              electricity_fee = electricity_unit * 3.00 + 50
        elif electricity_unit <= 300:
             electricity_fee = electricity_unit * 5.00 + 100
        elif electricity_unit <= 500:
             electricity_fee = electricity_unit * 7.50 + 150
        else:
            electricity_fee = electricity_unit * 10.00 + 250
    elif (quarter=="n"):
        print()
        electricity_unit = 0
        electricity_fee = 0
    else:
         print("[ERROR] Please enter y or n.")
         exit()
else :
    print("[ERROR] Invalid category.")
    exit()

print ("="*50)
print ("CALCULATED INVOICE BREAKDOWN")
print ("="*50)
print ("Base Access Pass Fee :", "₹",base_fee)
print ("Merit discount ","(",d,")",":","₹",merit_discount)

print ("parking fee :","₹",parking_fee)

if (ch==1 ):
    if (option=="y" and vehicle ==2):
        print ("student peak surcharge :","₹",peak_surchage)
elif (ch==1 ):
    if (option=="y" and vehicle==1):
        print ("student peak surcharge :","₹",peak_surchage)
else:
    peak_surchage=0

total = base_fee - merit_discount + parking_fee + peak_surchage

print ("Net Pass & Parking Total :","₹",total)
print ("="*50)
print ( "Electricity Bill ","(",electricity_unit,")",":","₹",electricity_fee,"(slab calculated + fixed charges)")
print ("="*50)
print ("TOTAL MONTHLY PAYABLE :","₹",total+electricity_fee)
print ("="*50)
print ("="*50)

