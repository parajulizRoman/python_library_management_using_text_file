with open('book_details.txt','r') as mf:
    book_list = mf.read()
    lis = []
    lis.append(book_list)


def content_to_write(new_contents):
    with open('book_details.txt','w') as mf:
        for list_item in new_contents:
            mf.write('%s\n'%list_item)

