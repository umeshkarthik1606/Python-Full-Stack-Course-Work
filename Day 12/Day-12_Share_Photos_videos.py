#gx corner
media = ['beach.png','waves.mp4','mountains.jpg','bike.jpg','dance.mp4','sunset.jpg'
         'party.png','songs.mp4','sound.mp4']

photos=[]
videos=[]
for i in media:
    if i.endswith('.mp4'):
        videos.append(i)
    else:
        photos.append(i)
print('\n---------Photos----------------')
for i in photos:
    print(i)
print('\n---------videos----------')
for i in videos:
    print(i)

select = set(input("Enter files to share (using comma): ").split(','))
for i in select:
    if i in media:
        print(f'{i}-sent')
    else:
        print(f'not present in media')
