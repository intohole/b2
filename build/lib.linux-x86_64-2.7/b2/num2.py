#coding=utf-8


from random import randint
import time


def get_random_seq(seq_len):
    rand_num = str(randint(0 , 10 ** (seq_len ) - 1))
    seq_str = ['0' for _ in range(seq_len)]
    for i in range(len(rand_num)):
        seq_str[seq_len-i -1] = rand_num[i]
    return ''.join(seq_str)


def get_random_seq1(seq_len):
    rand_num = str(randint (0 , 10 ** seq_len - 1))
    return '%s%s' % ('0' * (seq_len - len(rand_num)) , rand_num)



if __name__ == '__main__':
    print get_random_seq(6)
    print get_random_seq1(6)






