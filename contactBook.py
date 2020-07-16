def add(name,num):
    with open('data.txt','a+') as data:
        data.writelines(name+' '+str(num)+'\n')

def get_old_one():
    noah = {}
    with open('data.txt','r+') as data:
        for line in data:
            key,value = line.split()
            noah[key] = value
    c_names = list(noah.keys())
    nameList = str(c_names) #Just styling the way in which names will be printed
    for i in nameList:
        if i=='[' or i==']' or i=="'":
            nameList = nameList.replace(i,'')
        if i==',':
            nameList = nameList.replace(i,' |') #Styling finished here. xD
    print('\nContact names :',nameList)
    person = input("Whose's number you want? :")
    while person not in c_names:
        person = input("\nYou entered wrong name !\nPlease enter correct name :")
    print(person+"'s Number :",noah[person])     

        
def start():
    print('\n*******************************')
    print('*<<<WELCOME TO CONTACT BOOK>>>*')
    print('*******************************\n')
    print('<<<Credits : Members of Fantastic 4 Group>>>\n')
    print('<1: Add new Contact>')
    print('<2: Get old Contact>\n')
    choice=input('<Enter your choice(1 or 2)> :')
    if choice=='1':
        print('\n<<<***Please enter the following particulars of your Contact***>>>')
        name=input('<<<Enter the Contact Name>>> :')
        num=input('<<<Enter phone number>>> :')
        while num.isdigit() == False:
            print('invalid input,try again')
            num=input('<<<Enter a valid number>>> : ')
        add(name,num)
        print('\n<<<***Your Contact Saved successfully***>>>\n')

    elif choice=='2':
        get_old_one()
        
start()

    
