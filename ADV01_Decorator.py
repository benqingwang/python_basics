【1】解释什么是decorator
- @是decorator notation。Decorator是快捷方法来应用higher-order functions于其他functions or methods. 
- 简单说decorator就是给一个普通的function添加一些functionality并且return it. Decorator可以暗戳戳的应用这些functionality，不需要改变原有的普通function. 
- 可见decorator的好处是可以以clean, elegant, expressive way来添加new capabilities

【2】先看一个例子: 
- 我们下面的例子中，普通的function是print_numbers()
- decorator function有2个:  @timer and @reporter
# ------------------------------------------------------------
import functools 
import time

report_bin={}
def reporter(func):
    """store the function's docstring in a dictionary"""
    @functools.wraps(func)
    def wrapper_reporter(*args, **kwargs):
        value = func(*args, **kwargs) #这步就是让普通function运行返回结果
        report_bin[func.__name__] = func.__doc__  # 把function的documentation存入global variable report bin
        return value
    return wrapper_reporter

def timer(func): 
    """Print the runtime of the decorated function""" 
    @functools.wraps(func) 
    def wrapper_timer(*args, **kwargs): 
        start_time = time.perf_counter() # 1 
        value = func(*args, **kwargs) # run your function 
        end_time = time.perf_counter() # 2 
        run_time = (end_time - start_time)*(10**6) # 3 
        print(f"Finished {func.__name__!r} in {run_time:.4f} m secs") 
        return value
    return wrapper_timer

@timer
@reporter
def print_numbers():
    "I am printing numbers"
    return 1*2
# ------------------------------------------------------------
【3】需要的package (Python标准package)
import functools 

【4】先看普通的function: 就是简单的计算1*2
def print_numbers():
    "I am printing numbers"
    return 1*2

【5】如何define一个 decorator
# 1 决定你decorator的名字
def reporter(func): 
  
    # 2 call functools.wraps
    @functools.wraps(func)
  
  # 3 define一个wrapper可以接受func的argument
    def wrapper_reporter(*args, **kwargs):
   
        # 4 让普通func运行并返回结果
        value = func(*args, **kwargs) #这步就是让普通function运行返回结果
        
        # 5 让decorator做自己想做的      
        report_bin[func.__name__] = func.__doc__  # 把function的documentation存入global variable report bin

        # 6 return普通 func的结果
        return value

    # 7 运行 decor
    return wrapper_reporter

【6】如果我们run下面的，会发现report_bin添加了一个新item:
{'print_numbers': 'I am printing numbers'}
# ------------------------------------------------------------
import functools 
report_bin={}
@reporter
def print_numbers():
    "I am printing numbers"
    return 1*2
# ------------------------------------------------------------

【7】再看一个timer的例子
# ------------------------------------------------------------
import time
# 1 决定你decorator的名字
def timer(func): 
    """Print the runtime of the decorated function""" 

     # 2 call functools.wraps
    @functools.wraps(func) 

   # 3 define一个wrapper可以接受func的argument
    def wrapper_timer(*args, **kwargs): 
        start_time = time.perf_counter() # 1 
        
        # 4这个是原function的运行
        value = func(*args, **kwargs) # run your function 
        end_time = time.perf_counter() # 2 
        run_time = (end_time - start_time)*(10**6) # 3 
        print(f"Finished {func.__name__!r} in {run_time:.4f} m secs") 
        return value
    return wrapper_timer
# ------------------------------------------------------------
