followers= []
print(f"before followers: {followers}")

status = True
if status:
    followers.append("ram")

print(f"after followers: {followers}")

score = 85

if score >= 90:
    grade = "A"
elif score >= 75:
    grade = "B"
elif score >= 60:
    grade = "C"
else:
    grade = "F"

print("Grade:", grade)

user = {
    "role": "admin",
    "logged_in": True
}

if user["logged_in"]:
    if user["role"] == "admin":
        print("Admin access")
    else:
        print("User access")
else:
    print("Please log in")

students = [
    {"name": "Arjun", "marks": 45},
    {"name": "Pooja", "marks": 78},
    {"name": "Kiran", "marks": 92}
]

for s in students:
    if s["marks"] >= 50:
        print(s["name"], "Pass")
    else:
        print(s["name"], "Fail")

