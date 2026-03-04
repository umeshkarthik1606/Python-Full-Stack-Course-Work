data = {
        'naresh@gmail.com':'nari#123',
        'mahadev@gmail.com':'mahe@15',
        'prasad@gmail.com':'prasad@123',
        'mahesh@gmail.com':'maha@123',
        'kiran@gmail.com':'kiran@123'
        }

email=[]
int(input("enter the email: "))
if email in data:
    print("Enter the Password:")
    if password in data:
        print('Welcome')
    else:
        print('wrng password')
else:
    print("no email found")
