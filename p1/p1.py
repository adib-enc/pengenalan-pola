import numpy as np
#data frame
import pandas as pd

def printProps(v):
    print(v)
    print(v.ndim)
    print(v.shape)

    print(v)

def v1():
    # vektor python numpy with range value
    print("vektor default python\n")
    a = np.arange(1,20,1)
    b = np.arange(1,20,2)
    printProps(a)
    printProps(b)
    

def v2():
    print (" \n vektor via numpy \n")

    # vektor via numpy 
    c = np.array([1,2,3,4,5])
    d = np.array([1.5, 2.5, 5, 6, 7])
    printProps(c)
    printProps(d)

def matrix():
    a = np.arange(1,21,1)
    c = a.reshape((4,5))
    print(c)

def list1():
    list1 = ["apple","banana","cherry"]
    list2 = [1,5,7,9,3]
    list3 = [True, False, False]
    list4 = ["abc", 34, True, 40, "male"]

    print(list1)

def df1():
    df = pd.DataFrame(
        np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
        columns=['a', 'b', 'c']
    )

    print(df)

v1()
v2()
matrix()
list1()
df1()