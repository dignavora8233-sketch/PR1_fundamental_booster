print("Welcome to the Interactive Personal Data Collector!!\n")

name=input("please enter your name:")
age=int(input("please enter your age:"))
height=float(input("please enter your height in meters:"))
fav_num=int(input("please enter your favourite number:"))

print("Thank you!Here is the information we collected:")

print("Name:",name,"(Type:",type(name),",Memory Address:",id(name),")")
print("Age:",age,"(Type:",type(age),",Memory Address:",id(age),")")
print("Height:",height,"(Type:",type(height),",Memory Address:",id(height),")")
print("Fav_num:",fav_num,"(Type:",type(fav_num),",Memory Address:",id(fav_num),")")

current_year=2026

birth_year=current_year-age

print(f"Your birth year is approximatery:{birth_year}(based on your age of {age})")

print("Thank you for Using The Personal Data Collector.Goodbye!")

