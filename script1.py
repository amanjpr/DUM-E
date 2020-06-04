#!/usr/bin/python3

import math as m
import numpy as np

p0 = []
p2 = []
for i in range(0,2):
    ele = float(input())
    p0.append(ele)
for i in range(0,2):
    ele = float(input())
    p2.append(ele)
#print(p0, p2)
l1 = float(input())
l2 = float(input())
p0 = np.asarray(p0)
p2 = np.asarray(p2)
alpha = m.atan(p2[1]/p2[0])
l3 = m.hypot((p2[0]-p0[0]),(p2[1]-p0[1]))
theta2 = m.acos((l3**2-l1**2-l2**2)/(2*l1*l2))
beta = m.atan((l2*m.sin(theta2))/(l1+l2*m.cos(theta2)))
theta1 = alpha - beta
p1 = np.zeros(2)
p1[0] = l1*m.cos(theta1)
p1[1] = l1*m.sin(theta1)
print("theta1: ",theta1)
print("theta2: ",theta2)
p1 = np.asarray(p1)
print(p1)
