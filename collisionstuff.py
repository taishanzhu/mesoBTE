# MUST REPLACE VARIABLES WITH APPROPRIATE EQUIVALENTS IN ACTUAL CODE

from math import *

dp = [4,4]
vx = 2
vy = -4
xpos = 1
ypos = 3

# OUR ATTEMPT TO SOLVE THE INVISIBLE BOUNCING PROBLEM AND THE INTERSECTION PROBLEM

def counterclockwise(ax,ay,bx,by,cx,cy):
    return (cy-ay)*(bx-ax)>(by-ay)*(cx-ax)

def intersect(ax,ay,bx,by,cx,cy,dx,dy):
    lhs = counterclockwise(ax,ay,cx,cy,dx,dy) != counterclockwise(bx,by,cx,cy,dx,dy)
    rhs = counterclockwise(ax,ay,bx,by,cx,cy) != counterclockwise(ax,ay,bx,by,dx,dy)
    return (lhs and rhs)

def intersectionx(ax,ay,bx,by,cx,cy,dx,dy):
    bottomdet = (ax-bx)*(cy-dy)-(ay-by)*(cx+dx)
    topterm = ((ax*by)-(ay*bx))*(cx-dx)-(ax-bx)*((cx*dy)-(cy*dx))
    return (topterm/bottomdet)

def intersectiony(ax,ay,bx,by,cx,cy,dx,dy):
    bottomdet = (ax-bx)*(cy-dy)-(ay-by)*(cx+dx)
    topterm = ((ax*by)-(ay*bx))*(cy-dy)-(ay-by)*((cx*dy)-(cy*dx))
    return (topterm/bottomdet)

# ALL OF THE BELOW SHOULD BE EXECUTED WHEN VELOCITY VECTOR AND LINE INTERSECT

intptx = intersectionx(xpos,ypos,xpos+vx*dt,ypos+vx*dt,pointsArray[edge[x][0]][0],pointsArray[edge[x][0]][1],pointsArray[edge[x][0]][0]+dp[x][0]*dt,pointsArray[edge[x][0]][1]+dp[x][1]*dt)
intpty = intersectiony(xpos,ypos,xpos+vx*dt,ypos+vx*dt,pointsArray[edge[x][0]][0],pointsArray[edge[x][0]][1],pointsArray[edge[x][0]][0]+dp[x][0]*dt,pointsArray[edge[x][0]][1]+dp[x][1]*dt)

timebeforecollision = abs((intptx-xpos)/vx*dt)
timeaftercollision = dt - timebeforecollision

velvec = [vx,vy]
dpvec = [dp[0],dp[1]]
dpvecmag = sqrt((dpvec[0])*(dpvec[0])+(dpvec[1])*(dpvec[1]))
bhat = [dpvec[0]/dpvecmag,dpvec[1]/dpvecmag]
# calculate projection
dptemp = velvec[0]*bhat[0]+velvec[1]*bhat[1]
parallel = [bhat[0]*dptemp,bhat[1]*dptemp]
perp = [velvec[0]-parallel[0],velvec[1]-parallel[1]]
# flip perpendicular component
newvec = [parallel[0]-perp[0],parallel[1]-perp[1]]
print newvec

# NOW ADJUST THE POSITION USING THE NEW VX/VY AND REPLACING 'DT' with 'TIMEAFTERCOLLISION'
