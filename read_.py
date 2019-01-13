
lis2d = []
def list_2d():
    with open('book_details.txt','r') as mf:
        book_list = mf.readlines()
        for i in (book_list):
            j = i.replace('\n','').split(',')
            lis2d.append(j)
        return lis2d


def get_user_name():
    userName = input('ENTER YOUR USER NAME').upper()
    return userName

def get_user_selection():
    userSelection = input("ENTER THE NAME OF BOOK: ").upper()
    return userSelection




    




    
