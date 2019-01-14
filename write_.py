from datetime import datetime

timeStamp = str(datetime.now())

with open('book_details.txt','r') as mf:
    book_list = mf.read()
    lis = []
    lis.append(book_list)



'''
A function to write contents passed as parameter to file
The function opens book_details.txt file in write mode
Writes the passed parameter to the file
Function content_to_write
Gets a Parameter
returns None
'''

def content_to_write(new_contents):
    with open('book_details.txt','w') as mf:
        for list_item in new_contents:
            mf.write('%s\n'%list_item)
'''
A function to write borrow message in a file named with username
takes Username and UserSelection as parameters
Returns None
'''

def borrow_message_for_user(userName,userSelection):
    with open(userName +'.txt','a') as mf:
        message = userName+' BORROWED '+userSelection+' AT '+ timeStamp + "\n"
        mf.write(message)

def return_message_for_user(userName,userSelection):
    with open(userName +'.txt','a') as mf:
        message = userName+' RETURNED '+userSelection+' AT '+ timeStamp + "\n"
        mf.write(message)
