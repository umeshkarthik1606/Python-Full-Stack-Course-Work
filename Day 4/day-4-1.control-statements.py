products=['bread','butter','milk','suger','salt']

for product in products:
    print(f'{product}- Add to fav | Buy now | Add to cart')

sizes = ('xs','s','m','l','xl','xxl',)

for s in sizes:
    print(f'....|{s}|....')


followers = {'ravi','raju','kranthi','kavin','keerthi'}

for i in followers:
    print(f'{i}- |follow back|remove|messsage|')

data={
'ragesh':['c','c++','python'],
'somanth':['python','java','html'],
'srinikaseh':['java','linex','python'],
    }

for i in data:
    print(f"{i}: {data[i]}")

s='Python Programming'

for i in s:
    print(i)

# range(start,stop+1,step) = range(0,n,1)

n= int(input("enter number: "))
print(f"{n}-Table")
for i in range(0,11):
    print(f'{n}*{i}={n*i}')

for i in range(1,10):
    if i==7:
        break
    if i==5:
        continue
    print(i)


i =1
while i<=10:
    print(i)
    i= i+1


moves = 15
winning_point = int(input("Tell me how many moves are required: "))

while moves >= 1:
    if 15 - winning_point == moves:
        print("you won the game")
        break
    print(f"{moves} are left")
    moves = -1

else:
    print("Game over")


bullets = 10
while bullets > 0:
    print(f"you have {bullets} bullets, shoot them")
    bullets-= 1
else:
    print("Gamr over")











































