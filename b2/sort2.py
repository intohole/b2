#coding

from exceptions2 import judge_len
from exceptions2 import judge_type
from exceptions2 import judge_null


def insertSort(a , key = None): 
    for i in range(len(a)-1): 
        for j in range(i+1,len(a)):
            if key :
                if key(a[i]) > key(a[j]):
                    temp = a[i] 
                    a[i] = a[j] 
                    a[j] = temp
            else:
                 if a[i] > a[j]:
                    temp = a[i] 
                    a[i] = a[j] 
                    a[j] = temp



def sort_map_key(d , desc = True):
    judge_null(d)
    judge_len(d,0)
    judge_type(d , 'must be dict' , (dict))
    return sorted(d.items(), key = lambda x : x[0] , reverse = desc)


def sort_map_value(d , desc = True):
    judge_null(d)
    judge_len(d,0)
    judge_type(d , 'must be dict' , (dict))
    return sorted(d.items() , key = lambda x : x[1] , reverse = desc)

def sort_list_object( l , attr = None , desc = True):
    '''
    对输入的list object 对象进行排序 ， 根据对象属性排序
    '''
    judge_null(l)
    judge_type(l , 'type must be list' , (list))
    judge_null(attr)
    judge_type(attr  , 'attr type must be  str' , (str))
    return sorted(l , lambda x : getattr(x , attr) ,  reverse = desc) 






if __name__ == '__main__':
    a = [(3,3),(4,2),(1,4),(2,8)]
    insertSort(a , key = lambda x : x[1])
    b = {1 : 3 , -1 : 4 , 4 : 5 , 0 :2}
    print sort_map_key(b)