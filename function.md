b2
=======================


+ consle2.py  


:::python           
     
    if __name__ == '__main__':
        s = SimpleProgressBar() #使用控制台 ， 显示进度条
        for i in range(101): 
            s.update(i) #更新进度条
        print get_system_info()
        print get_python_version()[:3]
    
        
        t = ColorText() # 终端输出有色字体
        print t.ForeRed + "red" #输出红色字体
        print t.Default + "default" # 输出终端默认字体颜色
        print t.BlinkSet+ t.ForeRed + t.BackGreen + "red green" + t.Default #红字绿底
        print 'a' + t.Default #测试
        print t.Default



+ file2.py  


:::python     
    
    mkdir_p('d:/work_space/p2')
    reload_utf8()
    print walk_folder('D:\\workspace\\b2', lambda x:  x.endswith('py'))
    print create_folder_map('d:\\workspace\\b2', lambda x:  x.endswith('py') , limit_level = 1)
    a = lambda x : x.endswith('bb')
    print a('aa')
    print a('bb')
    print 'D:\\workspace\\b2\\.git\\COMMIT_EDITMSG'.endswith('py')
    for line  in Files(dirpath='D:\\workspace\\b2', file_filter=lambda x:  x.endswith('py')):
        print line 
