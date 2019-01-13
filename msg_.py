from datetime import datetime

timeStamp = str(datetime.now())


def borrow_message_for_user(userName,userSelection):
    with open(userName +'.txt','w') as mf:
        message = userName+' BORROWED '+userSelection+' AT '+ timeStamp
        mf.write(message)

def return_message_for_user(userName,userSelection):
    with open(userName +'.txt','a') as mf:
        message = userName+' RETURNED '+userSelection+' AT '+ timeStamp
        mf.write(message)
