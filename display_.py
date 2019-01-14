def start_screen():
    with open('book_details.txt','r') as mf:
        print('BOOKS AVAILABLE TO BORROW\n')
        file_contents = mf.read()
        file_contents = file_contents.replace('[','').replace(']','').replace("'","")
        #print(type(file_contents))
        print(file_contents)
    

    


    


