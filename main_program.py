from write_ import* 
from read_ import* 
from display_ import*
from check_ import*
from borrow_ import*


mainLoop = 'y'

while mainLoop == 'y':
    start_screen()
    print('\t\t\n ENTER [EXIT] TO QUIT \t ENTER [RETURN] TO RETURN BOOK \n')
    #database_book = list_2d()
    
    userSelection = get_user_selection()    
    isBookAvailable,contents,i = user_input(userSelection)

    if (isBookAvailable == True):
        print(userSelection,'BOOK AVAILABLE TO BORROW')
        #print('book index is',i,j)
        userName = get_user_name()
        isUserAvailable = user_auth(userName)
        if (isUserAvailable == True):
            print("Proceed to Book Borrow Porcess\n")
            contents,statusT = borrow_procress_(userSelection,contents,i)
            if statusT == True:
                content_to_write(contents)
                print('Sucess Fully Borrowed')
        
    else:
        print("SORRY, WE COULD NOT PROVIDE SERVICE YOU ASKED FOR\n")
        mainLoop == 'y'

    
    
    
    
    
