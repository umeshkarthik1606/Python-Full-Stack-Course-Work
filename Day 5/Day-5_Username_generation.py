# username generation

name = input("Enter the name: ")
dob = input("Enter the dob[YYYY-MM-DD]: ")

username = name[:5]+name[-5]+dob[-2:]+dob[2:4]

print(f"Hi {name}!\nYour Usernaame: {username}")

