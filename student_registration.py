#file acts like database
print("Choose option wisely")
while True:
    n=input("Enter:1.Register\t2.Exit: ")
    if n=="1":
        print("Enter your details properly")
        name=input("Enter your name:")
        surname=input("Enter your surname:")
        while True:
            roll_no=input("Enter your roll_no:")
            if len(roll_no)!=4 or not roll_no.isdigit():
                print("Enter your 4 digit roll_number")
            else:
                break
        city=input("Enter your city:")
        while True:
            phone=input("Enter your contact number:")
            if len(phone)!=10 or not phone.isdigit():
                print("Enter your 10 digit contact number:")
            else:
                break
        print("------------------------")
        print("Your details")
        print("Name:",name)
        print("Surname:",surname)
        print("Roll_no:",roll_no)
        print("City:",city)
        print("Phone:",phone)
        with open("student_db.csv","a") as f:
            f.write(f"{name},{surname},{roll_no},{city},{phone}\n")
        print("Detaills saved to file successfully")
            
    elif n=="2":
        print("Exit is success")
        break
    else:
        print("Inavlid input, strings or number other than 1 or 2 are rejected")
