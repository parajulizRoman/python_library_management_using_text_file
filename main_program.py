from write_ import* 
from read_ import* 
from display_ import*
from check_ import*
from borrow_ import*
from write_ import*
from msg_ import*
from return_ import*

mainLoop = 'y'

while mainLoop == 'y':
    start_screen()
    print('\t\t\n ENTER [EXIT] TO QUIT \t ENTER [RETURN] TO RETURN BOOK \n')
    
    userSelection = get_user_selection()    
    isBookAvailable,contents,i = user_input(userSelection)

    if (isBookAvailable == True):
        print(userSelection,'BOOK AVAILABLE TO BORROW')
        #print('book index is',i,j)
        userName = get_user_name()
        isUserAvailable = user_auth(userName)
        if (isUserAvailable == True):
            print("Proceed to Book Borrow Porcess\n")
            new_borrow_contents,statusB = borrow_procress_(userSelection,contents,i)
            if statusB == True:
                content_to_write(new_borrow_contents)
                borrow_message_for_user(userName,userSelection)
                print('SucessFully Borrowed')

    elif (isBookAvailable == 'RETURN'):
        print('BOOK RETURNING PROCESS')
        userSelection = get_user_selection()
        userName = get_user_name()
        isUserAvailable = user_auth(userName)
        if (isUserAvailable == True):
            print("PROCEED Book RETURNING PROCESS\n")
            new_return_contents,statusR = return_procress_(userSelection,contents,i)
            if statusR == True:
                content_to_write(new_return_contents)
                return_message_for_user(userName,userSelection)
                print('SucessFully Returned')        
    else:
        print("SORRY, WE COULD NOT PROVIDE SERVICE YOU ASKED FOR\n")
        mainLoop == 'y'

    
    
    
    
    
