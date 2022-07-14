#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time,math

# 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
def lianxi1():
    for a in range(1,5):
        for b in range(1,5):
            for c in range(1,5):
                if (a !=b) and (a !=c) and (c !=b):
                    print(a,b,c)

# lianxi1()

# 企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？
def lianxi2():
    a = [1000000,600000,400000,200000,100000,0]
    b = [0.01,0.015,0.03,0.05,0.075,0.1]
    ticheng =0
    lirun =int(input("输入利润："))
    for i in range(0,6):
        if lirun >a[i]:
            print(a[i])
            ticheng +=(lirun-a[i])*b[i]
            lirun = a[i]
    return ticheng

# print(lianxi2())

# 输入某年某月某日，判断这一天是这一年的第几天？
def lianxi4():
    year =int(input("year:\n"))
    month = int(input("month:\n"))
    day = int(input("day:\n"))
    days = 0
    months = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334)
    if ((year%4 ==0) or (year%400==0and year%100 !=0)) and month >2:
        days = months[month]+day +1
    else:
        days = months[month] + day
    return days
# print(lianxi4())

#输入三个整数x,y,z，请把这三个数由小到大输出。
def lianxi5():
    l=[]
    for i in range(3):
        a = int(input("输入整数：\n"))
        l.append(a)
    l.sort()
    return l

# print(lianxi5())

# 斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34
# def lianxi6():
# 普通方法
#     n = int(input())
#     a,b=1,1
#     for i in range(n-1):
#         a,b = b,a+b
#         print(a)
#     return a

# print(lianxi6())

# 递归法
def lianxi6(n):
    if n == 1 or n == 2:
        return 1
    return lianxi6(n-1) +lianxi6(n-2)

# print(lianxi6(10))

# 将一个列表的数据复制到另一个列表中。
def lianxi7():
    a =[3,4,5,6,7]
    b =a[:]
    return b

# print(lianxi7())

# 输出 9*9 乘法口诀表。
def lianxi8():
    for x in range(1,10):
        print()
        for y in range(1,x+1):
            a = x*y
            print(f"{x}X{y}={a} ", end="")
    return a

# lianxi8()

# 暂停一秒输出。
def lianxi9():
    myD = {1: 'a', 2: 'b'}
    for key, value in dict.items(myD):
        print(key, value)
        time.sleep(2)

# lianxi9()

# 暂停一秒输出，并格式化当前时间。
def lianxi10():
    print(time.strftime('%Y-%m-%d %H:%M:%S'))
    time.sleep(2)
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
# lianxi10()


def lianxi12():
    T =0
    for i in range(101,201):
        k = int(math.sqrt(i))+1
        print(k)
        for j in range(2,k):
            if i%j !=0:
                print(i)



# lianxi12()


leap = 1
from math import sqrt
from sys import stdout
for m in range(101,201):
    k = int(sqrt(m + 1))
    for i in range(2,k + 1):
        if m % i == 0:
            leap = 0
            break
    if leap ==1:
        print(m)
    leap =1