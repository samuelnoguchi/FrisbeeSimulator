from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

import matplotlib.pyplot as plt
import numpy as np
import math

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


# For each set of style and range settings, plot n random points in the box
# defined by x in [23, 32], y in [0, 100], z in [zlow, zhigh].

g = 9.81
m = 0.175
p = 1.23
A = 0.0568   
CLo = 0.1
CLa = 1.4
CDo = 0.08
CDa = 2.72
alphao = -4

xs = [0]
ys = [0]
zs = [1]

pos = [0,0,1]

################Modify########################
v0 = [10, 0, 2]
alpha = 0
phi = 5
deltaT = 0.01

##############################################

CL = CLo + CLa*alpha*np.pi/180
CD = CDo + CDa*pow((alpha-alphao)*np.pi/180,2)

v = v0

d1 = [math.cos(alpha*np.pi/180),0,math.sin(alpha*np.pi/180)]
d2 = [0,math.cos(phi*np.pi/180),math.sin(phi*np.pi/180)]
k = [0,0,1]
z=pos[2]


while z>=0:
    
    alpha = math.acos(np.dot(v, d1)/(np.linalg.norm(v)*np.linalg.norm(d1))) #remove?
    print(alpha)
    
    CL = CLo + CLa*alpha*np.pi/180
    CD = CDo + CDa*pow((alpha-alphao)*np.pi/180,2)
        
    vmag = np.linalg.norm(v)
     
    L = (0.5*CL*A*p*pow(vmag,2)/m*deltaT)*np.array((np.cross(v,d2)/np.linalg.norm(np.cross(v, d2))))
    D = -(0.5*CD*A*p*vmag/m*deltaT)*np.array(v)
    W = -g*deltaT*np.array(k)
        
    deltaV = L + D + W
    v = v + deltaV
    pos = pos + deltaT*v
    
    xs.append(pos[0])
    ys.append(pos[1])
    zs.append(pos[2])
    
    z = pos[2] 
    
    
    

    
ax.scatter(xs, ys, zs, c='r', marker='o')    

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()