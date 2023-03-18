a = int(input("Enter month number: "))

if a <=3:
    print("Winter")
elif 6 >= a >3:
    print("Spring")
elif 9 >= a >7:
    print("Summer")
elif 10 < a <=12:
    print("Autumn")
else:
    print("This month does not exist")