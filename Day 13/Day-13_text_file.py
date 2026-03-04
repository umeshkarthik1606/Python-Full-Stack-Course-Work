file.close()
'''file = open('sample.text','r')
content1 = file.read()
file.seek(0)
content2 = file.readline()
file.seek(0)
content3 = file.readlines()
file.seek(0)

print(content1,content2,content3,sep='\n\n')


file = open('sample.text','w')

file.write("Hello World")
file.close()

file = open('sample.text','a')

file.write("\nwelcome to the Python class")

file.close()

'''
with open('sample.text','r+') as file:

    file.erite("\nFile Operations")
    file.seek(0)
    print(file.read())


