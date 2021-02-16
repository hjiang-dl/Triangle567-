#coding=utf-8
#author:Hao Jiang
#HW02
import unittest
def classifyTraingle(a,b,c):
    if a <= 0 or b <=0 or c <=0:
        return("Invalid Input")
    elif a + b < c or b +c <a or a +c < b: 
        return("Not A Triangle")
    elif a > 200 or b > 200 or c > 200:
        return("Invalid Input")
    else:             #If the length of three sides conforms to the triangle, continue to judge what type of triangle it is
        if a == b == c:
            return("Equilateral")
        elif a == b or a == c or b==c:
            return("Isosceles")
        elif (a*a + b*b)==c*c or (b*b + c*c)==a*a or (a*a +c*c)==b*b:
            return("Right")
        else:
            return("Scalene")
    

if __name__=='__main__':  
    print("Input lengths of the triangle sides: ")
    a = int(input("a: "))
    b = int(input("b: "))
    c = int(input("c: "))
    d = classifyTraingle(a,b,c)
    print(d)
   