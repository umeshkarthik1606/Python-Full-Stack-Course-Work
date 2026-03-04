notes = {}

name= input('Enter your name: ')

while True:
    print(f'Hey {name} welcome to the notes...!')
    
    if notes:
        for i in notes:
            print(i.ljust(15,''),':',notes[i])
    else:
        print('Empty Notes')

    print('[A]dd Note')
    print('[U]pdate Note')
    print('[D]elet Note')
    print('[B]ack')

    ch = input('Enter your choise:').upper()
    if ch== 'A':
        note_name = input('Enter the note name: ').title()
        content = input('Write your thoughts.....: ')
        notes[note_name] = content
    elif ch == 'U':
        note_name = input('enter the note name to edit: ').title()
        if note_name in notes:
            new_content = input('Write your thoughts...!')
            notes[note_name] += new_content
        else:
            print(f'No {note_name} is not avilable')
    elif ch == 'D':
        note_name = input('Enter the note name to delete: ').title()
        if note_name in notes:
            notes.pop(note_name)
            print(f'{note_name} is deleted successfully')
        else:
            print(f'There is no notes on this name')
    elif ch == 'B':
        print(f'Thank you {name}')
    
