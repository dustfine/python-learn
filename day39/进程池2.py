import os
import time
from multiprocessing import Pool

def func(n):
    print('start func %s'%n,os.getpid())
    time.sleep(1)
    print('end func %s' % n,os.getpid())


if __name__ == '__main__':
    p = Pool(5)
    for i in range(10):
        # p.apply(func,args=(i,))
        p.apply_async(func,args=(i,))

    p.close()
    p.join()