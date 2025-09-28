# university student informaiton, student ID, name, age, grade
# if student ID is correct, grade above 85, student is eligible for a Grocery card of $50

# 1- student veriffication 
ID = "LU102025"
university_student_ID = input("Enter your university student ID: ")

# 2- boolean condition to check if the student ID is correct
if university_student_ID == ID:
    print("Access Granted")
else:
    print("Access Denied")

Name = input("Enter your name: ")
Age = input("Enter your age: ")
grade = int(input("Enter your grade: "))

# 3- check if the student is eligible for a Grocery card
Grocery_card = 50
Grocery_card_Code= "LU50102025"

if grade >= 85:
    print("Student is eligible for a Grocery card")
    print("Hello " + Name + ", you are " + str(Age) + " of age and a university student in LU according to your ID " + str(university_student_ID)) 
    print("Your GPA is " + str(grade) + " Which makes me eligible for a Grocery card for the month of September")
    print("please use the code " + Grocery_card_Code + " to redeem your Grocery card of $" + str(Grocery_card) + " at the LU stores")

else :
    print("Student is not eligible for a Grocery card")
    exit()
