from write_ import*
from read_ import*

def borrow_procress_(userSelection,contents,i):
        contents[i][2] = str(int(contents[i][2]) - 1 )
        content_to_write(contents)
        return contents, True
