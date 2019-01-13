from read_ import*

contents = (list_2d())
#for i in range(4):
#    print(contents[i][0])

with open('user_details.txt','r') as ud:
    users = ud.read()    

def user_auth(userName):
    if userName in users:
        print('Welcome',userName,'\n')
        return True
    else:
        print('No user found with given user name')
        usr_selection = input('Do you want to create new user ? y/n \n')
        if usr_selection == 'y':
            with open('user_details.txt','a') as ud:
                formatted_username = ','+ userName
                ud.write(formatted_username)
            print('Welcome\t',userName,'\n')
            return True
        else:
            return False
    

def user_input(userSelection): 

    for i in range (len(contents)):
        for j in range (len(contents)):
            if userSelection in contents[i][0]:
                return True,contents,i
    if userSelection == 'RETURN':
        ret = 'RETURN'
        return ret,contents,i
            
