print("Enter marks obtained in 5 subjects.")
mark1 = int(input("What mark did you get in subject 1."))
mark2 = int(input("What mark did you get in subject 2."))
mark3 = int(input("What mark did you get in subject 3."))
mark4 = int(input("What mark did you get in subject 4."))
mark5 = int(input("What mark did you get in subject 5."))
total = mark1+mark2+mark3+mark4+mark5
ave = total/5
if ave>=91 and ave<=100:
    print("Your grade is A1")
elif ave>=81 and ave<90:
    print("Your grade is A2")
elif ave>=71 and ave<80:
    print("Your grade is B1")
elif ave>=61 and ave<70:
    print("Your grade is B2")
elif ave>=51 and ave<60:
    ("Your grade is C1")
elif ave>=41 and ave<50:
    print("Your grade is C2")
elif ave>=33 and ave<41:
    print("Your grade is D")
elif ave>=21 and ave<33:
    print("Your grade is E1")
elif ave>=0 and ave<21:
    print("Your grade is E2")
else:
    print("Invalid input!")