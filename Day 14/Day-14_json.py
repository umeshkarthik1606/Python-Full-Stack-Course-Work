import json
'''
with open('sample.json','w') as file:
    data=[
	{'id':'1','name':'DK'},
	{'id':'2','name':'KL'},
	{'id':'3','name':'Sharma'},
	{'id':'4','name':'Kohli'},
	{'id':'5','name':'rutu'},
        {'id':'5','name':'Dhoni'}
    ]
    json.dump(data,file,indent=4)
    print("data saved sucessfully: ")
'''
with open('sample.json','r') as file:
    data = json.load(file)
data.append({'id':'6','name':'Pandya'})
with open('sample.json','w') as file:
    json.dump(data,file,indent=4)
    for i in data:
        print(i)

