'''
n= int(input("Enter the size: "))
num= 1
for row in range(n):
    for col in range(n):
        if (row+col)%2==0:
            print('0',end='')
        else:
            print('X',end='')
        
        num+=1
    print()
    
n= int(input("Enter the size: "))
num= 1
for row in range(n):
    for col in range(n):
        print(row+col,end='0')
         num+=1
    print()

n= int(input("Enter the size: "))
num= 1
for row in range(n):
    for col in range(row+1):
           print('*',end='')
    print()

n= int(input("Enter the size: "))
num= 1
for row in range(n):
    for col in range(n-row):
           print('*',end='')
    print()

n= int(input("Enter the size: "))
num= 1
for row in range(n):
    for src in range(n-row+1):
        print(' ',end=' ')
    for col in range(row-1):
           print('*',end=' ')
    print()

n= int(input("Enter the size: "))
num= 1
for row in range(n):
    for src in range(n+row):
        print(' ',end=' ')
    for col in range(n-row):
           print('*',end=' ')
    print()

n= int(input("Enter the size: "))
for row in range(n*2):
    if row <n:
        print('*'*(row+1))
    else:
        print('*'*(2*n-row))
    print()
'''
'''
  0 1 2 3 4 
0 * * * * *
1 *       *
2 *       *
3 *       *
4 * * * * *



n= int(input("Enter the size: "))
for row in range(n):
    for col in range(n):
        if row==0 or col==0 or row==n-1 or col==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

n= int(input("Enter the size: "))
for row in range(n):
    for col in range(n):
        if row==0 or col==0 or row==n-1 or col==n-1 or row==n//2 or col==n//2:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

n= int(input("Enter the size: "))
for row in range(n):
    for col in range(n):
        if row==0 or row==n-1 or row+col==n-1 :
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''
n= int(input("Enter the size: "))
for row in range(n):
    for col in range(n):
        if row+col==n-1 or row==col:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
