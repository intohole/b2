#coding=utf-8


def update_config(config , **kw):
    for key , val in kw.items():
        if key in config.keys():
            config[key] = val 
    return config 


a = {'a' : 1 }


update_config(a , a='2' , b ='2')


print a 