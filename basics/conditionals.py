age = int(input("Please enter your age: "))

current_year = 2026

if age < 0:
    print("Invalid age")
elif age > 120:
    print("Hmm... that seems unlikely")
else:
    birth_year = current_year - age
    print("You were likely born in", birth_year)