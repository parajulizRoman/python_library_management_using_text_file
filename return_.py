from write_ import*
from read_ import*

def return_procress_(userSelection,contents,i):
        contents[i][2] = int(contents[i][2])
        contents[i][2] = contents[i][2] + 1
        return contents, True
