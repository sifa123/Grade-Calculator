print("Enter your Subject wise Number")


Math = int(input("Enter Your Math Number:"))
if Math>=80 and Math<=100:
    print("Grade A+")
elif Math>=75 and Math<=80:
    print("Grade A")
elif Math >= 70 and Math <= 75:
    print("Grade A-")
elif Math >= 65 and Math <= 70:
    print("Grade B+")
elif Math >= 60 and Math <= 65:
    print("Grade B")
elif Math >= 55 and Math <= 60:
    print("Grade B-")
elif Math >= 50 and Math <= 55:
    print("Grade C+")
elif Math >= 50 and Math <= 45:
    print("Grade C")
elif Math >= 40 and Math <= 45:
    print("Grade D")
elif Math<40:
    print("Grade F")


Physics = int(input("Enter Your Physics Number: "))
if Physics>=80 and Physics<=100:
    print("Grade A+")
elif Physics>=75 and Physics<=80:
    print("Grade A")
elif Physics >= 70 and Physics <= 75:
    print("Grade A-")
elif Physics>= 65 and Physics<= 70:
    print("Grade B+")
elif Physics>= 60 and Physics<= 65:
    print("Grade B")
elif Physics>= 55 and Physics<= 60:
    print("Grade B-")
elif Physics>= 50 and Physics<= 55:
    print("Grade C+")
elif Physics>= 50 and Physics<= 45:
    print("Grade C")
elif Physics>= 40 and Physics<= 45:
    print("Grade D")
elif Physics<40:
    print("Grade F")


Chemistry = int(input("Enter Your Chemistry Number: "))
if Chemistry>=80 and Chemistry<=100:
    print("Grade A+")
elif Chemistry>=75 and Chemistry<=80:
    print("Grade A")
elif Chemistry>= 70 and Chemistry<= 75:
    print("Grade A-")
elif Chemistry>= 65 and Chemistry<= 70:
    print("Grade B+")
elif Chemistry>= 60 and Chemistry<= 65:
    print("Grade B")
elif Chemistry>= 55 and Chemistry<= 60:
    print("Grade B-")
elif Chemistry>= 50 and Chemistry<= 55:
    print("Grade C+")
elif Chemistry>= 50 and Chemistry<= 45:
    print("Grade C")
elif Chemistry>= 40 and Chemistry<= 45:
    print("Grade D")
elif Chemistry<40:
    print("Grade F")


Biology = int(input("Enter Your Biology Number: "))
if Biology>=80 and Biology<=100:
    print("Grade A+")
elif Biology>=75 and Biology<=80:
    print("Grade A")
elif Biology>= 70 and Biology<= 75:
    print("Grade A-")
elif Biology>= 65 and Biology<= 70:
    print("Grade B+")
elif Biology>= 60 and Biology<= 65:
    print("Grade B")
elif Biology>= 55 and Biology<= 60:
    print("Grade B-")
elif Biology>= 50 and Biology<= 55:
    print("Grade C+")
elif Biology>= 50 and Biology<= 45:
    print("Grade C")
elif Biology>= 40 and Biology<= 45:
    print("Grade D")
elif Biology<40:
    print("Grade F")


English = int(input("Enter Your English Number: "))
if English>=80 and English<=100:
    print("Grade A+")
elif English>=75 and English<=80:
    print("Grade A")
elif English>= 70 and English<= 75:
    print("Grade A-")
elif English>= 65 and English<= 70:
    print("Grade B+")
elif English>= 60 and English<= 65:
    print("Grade B")
elif English>= 55 and English<= 60:
    print("Grade B-")
elif English>= 50 and English<= 55:
    print("Grade C+")
elif English>= 50 and English<= 45:
    print("Grade C")
elif English>= 40 and English<= 45:
    print("Grade D")
elif English<40:
    print("Grade F")


total = Math+Physics+Chemistry+Biology+English
print("Your Total Mark: ", total)

Avg = total/5
if Avg>=80 and Avg<=100:
    print("Your Average Grade is: A+")
elif Avg>=75 and Avg<=80:
    print("Your Average Grade is: A")
elif Avg>= 70 and Avg<= 75:
    print("Your Average Grade is:A-")
elif Avg>= 65 and Avg<= 70:
    print("Your Average Grade is: B+")
elif Avg>= 60 and Avg<= 65:
    print("Your Average Grade is:B")
elif Avg>= 55 and Avg<= 60:
    print("Your Average Grade is: B-")
elif Avg>= 50 and Avg<= 55:
    print("Your Average Grade is: C+")
elif Avg>= 50 and Avg<= 45:
    print("Your Average Grade is: C")
elif Avg>= 40 and Avg<= 45:
    print("Your Average Grade is: D")
elif Avg<40:
    print("Your Average Grade is: F")
