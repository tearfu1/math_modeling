import numpy as np

def fib(n):
    a=0
    b=1
    fn=0
    if n == 0:
        return 0
    elif n > 0:
        for i in np.arange(2,n,1):
            fn = a+b
            a = b
            b = fn
        return(fn)
    else:
        for i in np.arange(n,-2,1):
            fn = a-b
            a = b
            b = fn
        return(fn)
print(fib(-7))