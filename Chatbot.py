print("🎓 Welcome to College Management Chatbot")


name = input("Enter your name: ")
year = input("Enter your year (FE/SE/TE/BE): ")
roll = input("Enter your roll number: ")

print("\nHello", name, "😊 Welcome to College Portal")
print("Type 'menu' to see options or 'bye' to exit\n")


attendance = 85
marks = {
    "Maths": 78,
    "DSA": 82,
    "DBMS": 75
}

notices = [
    "📢 Exam form last date: 30 March",
    "📢 Sports event on 5 April",
    "📢 Holiday on Friday"
]

events = [
    "🎉 Tech Fest",
    "🎤 Cultural Day",
    "🏆 Sports Week"
]

def calculate_gpa(marks):
    avg = sum(marks.values()) / len(marks)
    if avg >= 85:
        return "9.0 GPA"
    elif avg >= 70:
        return "8.0 GPA"
    elif avg >= 60:
        return "7.0 GPA"
    else:
        return "6.0 GPA"

while True:
    user = input(name + ": ").lower()

    if user == "menu":
        print("\n📋 Available Options:")
        print("1. fees")
        print("2. timetable")
        print("3. attendance")
        print("4. marks")
        print("5. gpa")
        print("6. notices")
        print("7. events")
        print("8. library")
        print("9. exam")
        print("Type option name\n")

    elif "fees" in user:
        print("Bot:", name + ", your fees is ₹80,000 per year")

    elif "timetable" in user:
        print("Bot:", name + ", classes are from 10 AM to 4 PM")

    elif "attendance" in user:
        print("Bot:", name + ", your attendance is", str(attendance) + "%")

    elif "marks" in user:
        print("Bot:", name + ", your marks are:")
        for sub, m in marks.items():
            print(sub, ":", m)

    elif "gpa" in user:
        print("Bot:", name + ", your GPA is", calculate_gpa(marks))

    elif "notices" in user:
        print("Bot: Latest Notices:")
        for n in notices:
            print(n)

    elif "events" in user:
        print("Bot: Upcoming Events:")
        for e in events:
            print(e)

    elif "library" in user:
        print("Bot: Library is open from 9 AM to 6 PM")

    elif "exam" in user:
        print("Bot:", name + ", exams will start from next month")

    elif user == "bye":
        print("Bot: Goodbye", name + "! 👋")
        break

    else:
        print("Bot: Type 'menu' to see available options")
