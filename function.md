b2
=======================


+ consle2.py  

:::python           
     
    if __name__ == '__main__':
        s = SimpleProgressBar()
        for i in range(101):
            s.update(i)
        print get_system_info()
        print get_python_version()[:3]
        print 'hello world!'
        today = '奇怪'
    
        
        t = ColorText()
        print t.ForeRed + "red"
        print t.Default + "default"
        print t.BlinkSet+ t.ForeRed + t.BackGreen + "red green" + t.Default
        print 'a' + t.Default
        print t.Default