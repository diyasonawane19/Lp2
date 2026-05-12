#Chatbot

print("=" * 50)
print("     WELCOME TO COLLEGE MANAGEMENT CHATBOT     ")
print("=" * 50)

name = input(" Enter your name: ")
year = input(" Enter your year (FE/SE/TE/BE): ")
roll = input(" Enter your roll number: ")

print("\n" + "=" * 50)
print("Hello", name, " Welcome to College Portal")
print("Year:", year, "| Roll No:", roll)
print("=" * 50)
print(" Type 'menu' to see options")
print(" Type 'bye' to exit\n")

attendance = 85
maths = 78
dsa = 82
dbms = 75

while True:
    user = input(name + ": ").lower()

    if user == "menu":
        print("\n ===== AVAILABLE OPTIONS =====")
        print("1 fees")
        print("2 timetable")
        print("3 attendance")
        print("4 library")
        print("5 exam")
        print("6 notice")
        print("bye\n")

    elif user == "fees":
        print("Bot: Your yearly college fees is ₹80,000")

    elif user == "timetable":
        print("Bot: Classes are from 10:00 AM to 4:00 PM")

    elif user == "attendance":
        print("Bot: Your attendance is", attendance, "%")

    elif user == "library":
        print("Bot: Library is open from 9:00 AM to 6:00 PM")

    elif user == "exam":
        print("Bot: Exams will start from next month")

 
    elif user == "notice":
        print(" Bot: Latest Notice")
        print("Exam form submission ends on 30 March")

    

    elif user == "bye":
        print(" Bot: Goodbye", name, "See you soon!")
        break

    else:
        print(" Bot: Invalid option! Type 'menu' to see choices.")
