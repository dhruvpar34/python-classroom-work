print ("-"*50)
print ("-"*50)
print ("SMARTCAMPUS UTILITY & ACCESS PASS GENERATOR")
print ("-"*50)
print ("-"*50)

print ("1.student")
print ("2.faculty/staff")
ch = int (input("choice the category from the given option above :"))

print("-"*50)
if (ch==1):
    name = input ("Enter your name :")
    age = int(input("Enter your age :"))
    roll_number = int (input ("Enter the roll no :"))
    CGPA = float(input("Enter the CGPA(CGPA should be between 0.0 to 10.0 :)"))
    cl= input ("Enter class from the (A,B,C,D,E) :")
    print("1.UG")
    print("2.PG")
    sub_cateogry = int (input("choice the sub cateogry from the above option :"))
    if (sub_cateogry==1):
        base_fee = 500
        if (CGPA>=8.5):
            d = 20
            merit_discount= base_fee*0.2
        elif (CGPA<=8.49 and CGPA>=7.5):
            d=10
            merit_discount= base_fee*0.1
        elif (CGPA<0):
            print ("[ERROR] cgpa cannot be negative")
        else:
            print ("[ERROR]")
    elif(sub_cateogry==2):
        base_fee = 350
        if (CGPA>=8.5):
            d=20
            merit_discount = base_fee*0.2
        elif (CGPA<=8.49 and CGPA>=7.5):
            d=10
            merit_discount = base_fee*0.1
        elif (CGPA<0):
            print ("[ERROR] cgpa cannot be negative")
        else:
            print ("[ERROR]")
    print ("Do you own a vehicle y/n :")
    option = input()
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
    elif (option=="n"):
        parking_fee = 0
    else:
            print ("[ERROR]")   
    print ("Do you live in hostile y/n :")
    hostile = input()
    if (hostile == int):
        print ("[ERROR]")
    elif (hostile == "y"):
        print ("give the number of electricity you consumed every month (in kwh):")
        electricity_unit = int(input())
        if (electricity_unit<=100):
            electricity_fee = electricity_unit*3.00 + 50
        elif (electricity_unit>100):
            electricity_fee = electricity_unit*5.00 +100
        elif (electricity_unit>300):
            electricity_fee = electricity_unit*7.50 +150
        elif (electricity_unit >500):
            electricity_fee = electricity_unit*10.00 + 250
        elif(electricity_unit<0):
            print("[error] electricity consumed cannot be negative.")
    elif (hostile == "n"):
        print()
        electricity_unit = 0
        electricity_fee = 0
elif(ch==2):
    name = input ("Enter your name :")
    age = int(input("Enter your age :"))
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
        if (year>10):
            d = 15
            merit_discount = base_fee*0.15
    elif (sub_cateogry == 2):
        merit_discount = 1200
        if (year>10):
            d= 15
            merit_discount = base_fee*0.15
    print ("Do you own a vehicle y/n :")
    option = input()
    if (option=="y"):
        print("1.Two wheeler")
        print("2.Four wheeler")
        vehicle = int (input ("enter the option given above :"))
        if (vehicle==1):
            parking_fee = 200
        elif (vehicle==2):
            parking_fee = 600
        else:
            print ("wrong option entered")
    elif (option=="n"):
        parking_fee = 0
    else:
            print ("[ERROR]")
    print ("Do you live in quarter y/n :")
    quarter = input()
    if (quarter == int):
        print ("[ERROR]")
    elif (quarter == "y"):
        print ("give the number of electricity you consumed every month (in kwh):")
        electricity_unit = int(input())
        if (electricity_unit<=100):
            electricity_fee = electricity_unit*3.00 + 50
        elif (electricity_unit>100):
            electricity_fee = electricity_unit*5.00 +100
        elif (electricity_unit>300):
            electricity_fee = electricity_unit*7.50 +150
        elif (electricity_unit >500):
            electricity_fee = electricity_unit*10.00 + 250
        elif(electricity_unit<0):
            print("[error] electricity consumed cannot be negative.")
    elif (quarter=="n"):
        print()
        electricity_unit = 0
        electricity_fee = 0
elif (ch):
    print ("[ERROR]")

print ("-"*50)
print ("CALCULATED INVOICE BREAKDOWN")
print ("-"*50)
print ("Base Access Pass Fee :", "₹",base_fee)
print ("Merit discount ","(",d,")",":","₹",merit_discount)

print ("parking fee :","₹",parking_fee)
peak_surchage = 0
if (ch==1 ):
    if (option=="y" and vehicle ==2):
        print ("student peak surcharge :","₹",peak_surchage)
elif (ch==1 ):
    if (option=="y" and vehicle==1):
        peak_surchage = 0
        print ("student peak surcharge :","₹",peak_surchage)
else:
    peak_surchage=0

total = base_fee - merit_discount + parking_fee + peak_surchage

print ("Net Pass & Parking Total :","₹",total)
print ("-"*50)
print ( "Electricity Bill ",electricity_unit,":","₹",electricity_fee,"(slab calculated + fixed charges)")
print ("-"*50)
print ("TOTAL MONTHLY PAYABLE :","₹",total+electricity_fee)
print ("-"*50)
print ("-"*50)

