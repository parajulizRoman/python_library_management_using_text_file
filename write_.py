

'''with open('book_details.txt','r') as mf:
    book_list = mf.read()
    lis = []
    lis.append(book_list)
    #print(lis)
'''

def content_to_write(contents):
    with open('book_details.txt','w') as mf:
        book_contents = str(contents).replace(']','')
        #print(book_contents)
        mf.write(book_contents)

