#!/usr/bin/python3

import math as m
import numpy as np
import numpy.matlib

l1,l2,l3 = 1,1,1
m0 = []
m1 = []
m2 = []
m3 = []
print("Enter the coordinates x,y,z for m0:")
for i in range(0,3):
    ele = float(input())
 
    m0.append(ele)
m0.append(1)
print("Enter the coordinates x,y,z for m1:")
for i in range(0,3):
    ele = float(input())
 
    m1.append(ele)
m1.append(1)
print("Enter the coordinates x,y,z for m2:")
for i in range(0,3):
    ele = float(input())
 
    m2.append(ele)
m2.append(1)
print("Enter the coordinates x,y,z for m3:")
for i in range(0,3):
    ele = float(input())
 
    m3.append(ele)
m3.append(1)
m0 = np.asarray(m0); m0.shape = (4,1)
m1 = np.asarray(m1); m1.shape = (4,1)
m2 = np.asarray(m2); m2.shape = (4,1)
m3 = np.asarray(m3); m3.shape = (4,1)
#x = np.array([[0],[0],[0],[1]])
m0 = m0-m0
m1 = m1-m0
m2 = m2-m0
m3 = m3-m0
#angle theta0, theta1, theta2, theta3 are respectively a0,a1,a2,a3
a0 = m.atan2(m3[1],m3[0])

c0 = m.cos(a0); s0 = m.sin(a0)
A1 = np.array([[c0,0,s0,0],[s0,0,-c0,0],[0,1,0,0],[0,0,0,1]])
A1inv = np.linalg.inv(A1)
p1 = np.dot(A1inv,m1)
p1 = np.around(p1, decimals=2)
#print(p1)

if p1[0]<0 and p1[0]>=-1:
   a1 = m.acos(p1[0]/l1)
else:
   a1 = m.asin(p1[1]/l1)

c1 = m.cos(a1); s1 = m.sin(a1)
A2 = np.array([[c1,-s1,0,l1*c1],[s1,c1,0,l1*s1],[0,0,1,0],[0,0,0,1]])
A2inv = np.linalg.inv(A2)
p2 = np.dot(A2inv,A1inv)
p2 = np.dot(p2,m2)
p2 = np.around(p2, decimals=2)
#print(p2)

if p2[0]<0 and p2[0]>=-1:
   a2 = m.acos(p2[0]/l1)
else:
   a2 = m.asin(p2[1]/l1)

c2 = m.cos(a2); s2 = m.sin(a2)
A3 = np.array([[c2,-s2,0,l2*c2],[s2,c2,0,l2*s2],[0,0,1,0],[0,0,0,1]])
A3inv = np.linalg.inv(A3)
p3 = np.dot(A3inv,A2inv)
p3 = np.dot(p3,A1inv)
p3 = np.dot(p3,m3)
p3 = np.around(p3, decimals=2)
#print(p3)

if p3[0]<0 and p3[0]>=-1:
   a3 = m.acos(p3[0]/l1)
else:
   a3 = m.asin(p3[1]/l1)


a0 = m.degrees(a0)
a1 = m.degrees(a1)
a2 = m.degrees(a2)
a3 = m.degrees(a3)

print("theta0 :",a0)
print("theta1 :",a1)
print("theta2 :",a2)
print("theta3 :",a3)



















