print ("================================================================")
print ("=======================Calculator===============================" )
print ("================================================================")
try :
    a = int (input ("enter the 1st number = "))
    b = int ( input ("enter the 2nd number "))

    print ("1. enter + for the addition \n 2.  enter - for the subtraction \n 3. enter * for the multiplication \n 4. enter / for the dividision  ")

    ch = input ("enter your choice : ")
    match ch:
        case "+" :
            print(f"The result is : {a+b}")
        case "-" :
            print(f"The result is : {a-b}")
        case "*" :
            print(f"The result is : {a*b}")
        case "/" :
            print(f"The result is : {a/b}")
        case default :
            print ("the choice is worng.")


except Exception as e :
    print ("enter the valid number.")