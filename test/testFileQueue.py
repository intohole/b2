#coding=utf-8



from b2.queue2 import FifoDiskQueue






queue = FifoDiskQueue(".queue",chunksize=5)
queue.push_array(["1","2","3","4","5","6","7","8","9","10","11"])

while len(queue):
    print queue.pop()
queue.push_array(["12","13"])
print queue.pop()
print queue.pop()
queue.close()
