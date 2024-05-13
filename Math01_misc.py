"""***********************************************************************
1. Use eval() to calculate math formula in string
***********************************************************************"""
eval('1+1')             #-->2
eval('2*3')             #-->6
eval('min(11,2)')       #-->2
eval('2**3')            #-->8

 
"""***********************************************************************
2. Random function
****需要用random module
***********************************************************************"""
import random 

#----------------------random.random()------------------------------------
#1 Generate a random number between 0 and n
random.random()*100 #random float where the value is between 10 and 100
"62.40316005383818"

#2 Generate a random number between m and n
random.random()*(95-5)+5 #random between 5 and 95
"74.82632293168896"


!!!!! random.choice()是draw with replacement
!!!!! random.sample()是draw without replacement


#----------------------random.choice()------------------------------------
#1 Choice a random item from a list
random.choice(['a','b','c','d','e'])
"'d'"

#2 Choice multiple random items from a list 
random.choices(['a','b','c','d','e'],k=3)
""" ['c', 'a', 'c']"""

#----------------------random.sample()------------------------------------
random.sample(['a','b','c','d','e'],3)
"['c', 'b', 'e']"
"这个和random choices好像一样,但是区别到底是什么呢？"

#----------------------random.randrange()---------------------------------
random.randrange(7,16)
"注意这个出来的是整数，也是："
random.choice(range(7,16))

# ---------------------random.shuffle()--------------------------------------------
myList=[3,6,7,8]
random.shuffle(myList)
myList #-->[7,6,8,3]
