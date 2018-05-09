是Python函数可变参数 args及kwargs
* *args表示任何多个无名参数，它是一个tuple
* **kwargs表示关键字参数，它是一个dict
```python
def foo(*args,**kwargs):
    print('args=',args)
    print('kwargs=',kwargs)
    print('--------------------')
    
    
if __name__=='__main__':
    foo(1,2,3)
    foo(a=1,b=2,c=3)
    foo(1,2,3,a=1,b=2,c=3)
    foo(1,'b','c',a=1,b='b',c='c')

'''output:
args= (1, 2, 3)
kwargs= {}
--------------------
args= ()
kwargs= {'a': 1, 'b': 2, 'c': 3}
--------------------
args= (1, 2, 3)
kwargs= {'a': 1, 'b': 2, 'c': 3}
--------------------
args= (1, 'b', 'c')
kwargs= {'a': 1, 'b': 'b', 'c': 'c'}
--------------------
'''
```