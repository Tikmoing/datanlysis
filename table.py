import csv
from operator import length_hint
from numpy import isin 
import prettytable
import numpy
from datanlysis import typecv

    
def _toFloat(variable):
    # This function is used for judge whether the varible is interger or float
    try:
        return float(variable)
    except:
        return variable

def _arrayToString(array):
    res = array.copy()
    for i in range(0,len(res)):
        res[i] = str(res[i])
    return res

class Table:
    def __init__(self,source,head=True):
        self.__source = source
        self.__table = {}
        self.__head = self.__source[0].copy()
        self.type_list = []
        if(head):
            for i in range(0,len(self.__head)):
                self.__table[ self.__head[i] ] = []
                for j in range(1,len(self.__source)):
                    self.__source[j][i] = _toFloat( self.__source[j][i] )
                    self.__table[ self.__head[i] ] .append( self.__source[j][i])
        else:
            for i in range(0,len(self.__head)):
                self.__head[i] = "col-" + str(i+1)
                self.__table[ self.__head[i] ] = []
                for j in range(1,len(self.__source)):
                    self.__source[j][i] = _toFloat( self.__source[j][i] )
                    self.__table[ self.__head[i] ] .append( self.__source[j][i])
            self.__source.insert( 0,self.__head )
        
        for i in range(0,len(self.__head)):
            self.type_list.append( type( self.__source[1][i] ) )

    def output(self):
        PrintTool = prettytable.PrettyTable()
        PrintTool.field_names = self.__head

        for i in range(1,len(self.__source)):
            PrintTool.add_row(  self.__source[i]  )
        print(PrintTool)

    def head(self,index):
        return self.__table[index]

    def row(self,index):
        return self.head( self.__head[index] )

    def col(self,index):
        return self.__source[index]

    #only add one column now
    def add_col(self,data,head=""):
        head = str(head)
        if( len(head) == 0 ):
            head = "col-" + str(len(self.__head))
        self.__head.append( head )
        # try:
        #     self.__table[head] = data
        # except:
        #     print("The dimension of new data is different to the original for row.")
        self.__table[head] = data
        for i in range( len(data) , len(self.__source) - 1 ):
            self.__table[head].append(None)
        
        self.__source[0].append( head )
        for i in range(1,len(self.__source)):
            self.__source[i].append( self.__table[head][i-1] )

        self.type_list.append(type(self.__source[1][  len(self.__head) - 1 ]))
        
    
    def add_row(self,data):
        # data_type = [ type(i) for i in data ]
        # bool_a
        # for i in range(0, len(data) ):
        #     bool_a = bool_a and ( data_type[i] == self.type_list )
        # if(bool_a):
        #     for i in range(0,len(  ))

        for i in range(0,len(data)):
            self.__table[self.__head[i]].append(data[i])
            
        self.__source.append(data)
        for i in range(len(data),len(self.__head)):
            self.__table[self.__head[i]].append(None)
            self.__source[ len(self.__source) - 1 ].append(None)


        

def open_csv(path,mod='r',head=True):
    fcsv = csv.reader(open(path,mod))
    listcsv = [i for i in fcsv]
    return Table(listcsv,head)


def open_excel():
    pass

