name = input("Enter your name: ")
age = int(input("Enter your age: "))
year = 2026
birth_year = year - age
print("Hello,", name)
print("You were born in", birth_year)
if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")
