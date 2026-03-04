n=int(input('Enter the number of students: '))
names,gpas=[],[]
max_vl=0
max_name=''
min_val=10
min_name=''
for i in range(n):
    print(f"------------Students-{i+1}-------------------")
    names = input('enter the name: ')
    gpa = float('enter the gpa: ')

    if gpa>max_val:
        max_name=name
        max_val=gpa
    if gpa<min_val:
        min_name=name
        min_val=gpa
        
    names.append(name)
    gpas.append(gpa)

print(f'{"Names".ljust(15)}{"GPA".ljust(5)}')
print('-'*20)
for i in range(len(names)):
    print(f'{names[i].ljust(14)}|{str(gpas[i]).ljust(5)}')


