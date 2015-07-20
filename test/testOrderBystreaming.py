#coding



import sys






def sample(sample_key , sample_num , key_index ,split_char = None ):
    line_count = 0 

    for line in sys.stdin:
        line = line.rstrip()
        line_array = line.split(split_char)
        if line_count != 0 and line_count % sample_num == 0:
            print line_array[key_index]
        
