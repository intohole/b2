



class N(int):


    def __init__(self , * arg , ** kw):
        int.__init__( arg , kw)



if __name__ == '__main__':
    print N()