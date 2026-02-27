'''def student_data(info):
    print(f'Name: {info[0]}')
    print(f'Course: {info[1]}')
    print(f'gra_year: {info[2]}')
    print('-----------END---------')
data=[['ram','pfs','2026'],
      ['raju','jfs','2025'],
      ['hritik','ds','2026'],
      ['jasmin','da','2025']
      ]
for i in data:
    student_data(i)

def display(uname,email,password):
    print(f'Username: {uname}')
    print(f'Email: {email}')
    print(f'Password: {password}')
    print('\n')
display(uname='rana',email='rana@gmail.com',password='Uaniandi147')
display(uname='kumba',password='jnvnvwnv557',email='kumba@gmail.com')
display(password='jnoauwwvnnow4442',email='mari@gmail.com',uname='mari')

def display(uname,email,password,status='absent'):
    print(f'Username: {uname}')
    print(f'Email: {email}')
    print(f'Password: {password}')
    print(f'Status: {status}')
    print('\n')
display(uname='rana',email='rana@gmail.com',password='Uaniandi147')
display(uname='kumba',password='jnvnvwnv557',email='kumba@gmail.com')
display(password='jnoauwwvnnow4442',email='mari@gmail.com',uname='mari')

def display (*names):
    for i in names:
        print(i)
    else:
        print('-----------END---------')
display('kaja')
display('khasin','ramesh','suresh','preety')
display('santhu','vikey','mahesh')
display('naresh','sathi')
'''
data={
    123456:{'pin':1564,'balance':5000,'history':[]},
    147852:{'pin':1258,'balance':500,'history':[]},
    369852:{'pin':9852,'balance':70000,'history':[]}
    }
def check_balance():
    Print(f"Your Balance Amount is ${data[acc]['balance']}")
def deposit(acc):
    amount= int(input("Enter the amount: "))
    data[acc]['balance']+=amount
    data[acc]['history'].append(f'{amount} is deposited')
    print(f"{amount} is deposited successfully")
def Withdraw(acc):
    if:
    amount= int(input("Enter the amount: "))
    data[acc]['balance']-=amount
    data[acc]['history'].append(f'{amount} is withdrawn')
    print(f"{amount} is withdrawn successfully")
    else:
        print("You don't have sufficent balance")
def menu():
    print('1. Check Ballence')
    print('2. Deposit')
    print('3. Withdraw')
    print('4. Set Pin')
    print('5. Veiw Transaction')
    print('6. Exit')
acc = int(input("Enter the Account Number: "))
pin = int(input("Enter the Pin: "))
if acc in data and data [acc]['pin'] 
print('Welcome to the ATM')
while True:
    menu()
    ch =int(input("Enter the choise: "))
    if ch==6:
        Print("Thank You")
        break

























