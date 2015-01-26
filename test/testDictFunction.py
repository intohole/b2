#coding=utf-8




def get_value(data  ,*argv):
    '''
    得到data嵌套属性value
    参数:
        data : 需要找到相应value值object
        argv : 属性名/index/
    返回：
         如果找不到相应属性名
         抛出异常 ， 属性寻址路径
         否则：
             返回相应的value
    '''
    if len(argv) == 0:
        return default
    node = data
    parrent_names = []
    for name in argv:
        if node is None or name is None:
            raise ValueError , 'object %s  is nothing or name %s is nothing!' % (node , name )
        try:
            if isinstance(name , str ) and  hasattr(node , name): 
                node = getattr(node , name)
                parrent_names.append(name)
            elif name and isinstance(name , (int , long)) and hasattr(node , '__item__'):
                node = node[name]
                parrent_names.append(name)
            elif hasattr(node , '__getitem__') and hasattr(node , 'has_key'):
                node = node[name]
            else:
                raise TypeError , 'object node not have nonthing to get value %s' % str(node) 
        except Exception, e:
            raise Exception,(e , 'get object %s attribute %s wrong ' % (node , name ) , 'name path :  [ %s ]' % '->'.join(parrent_names))
    return node 



def get_default_value( data , default , * argv):
    try:
        return get_value(data , *argv) , None , None 
    except Exception, e  :
        return default , e 

def get_deep_dict_value(data , default , *argv):
    node = data
    for name in argv:
        if node.has_key(name):
            node = data[name]
        else:
            return default
    return node if isinstance(node , type(default)) else default




if __name__ == '__main__':
    class Test1(object):

        def __init__(self):

            self.a = {1 : {2 : {3:9}}}


    t = Test1()
    print get_default_value(t , 0 , 'a' , 1 , 2 )
