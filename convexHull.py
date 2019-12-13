from random import randint # for sorting and creating data pts
from math import atan2 # for computing polar angle

def polar_angle(p0,p1=None):
    if p1==None: p1=anchor
    y_span=p0[1]-p1[1]
    x_span=p0[0]-p1[0]
    return atan2(y_span,x_span)



def distance(p0,p1=None):
    if p1==None: p1=anchor
    y_span=p0[1]-p1[1]
    x_span=p0[0]-p1[0]
    return y_span**2 + x_span**2



def det(p1,p2,p3):
    return   (p2[0]-p1[0])*(p3[1]-p1[1]) \
            -(p2[1]-p1[1])*(p3[0]-p1[0])



def quicksort(a):
    if len(a)<=1: return a
    smaller,equal,larger=[],[],[]
    piv_ang=polar_angle(a[randint(0,len(a)-1)]) # select random pivot
    for pt in a:
        pt_ang=polar_angle(pt) # calculate current point angle
        if   pt_ang<piv_ang:  smaller.append(pt)
        elif pt_ang==piv_ang: equal.append(pt)
        else:                   larger.append(pt)
    return   quicksort(smaller) \
            +sorted(equal,key=distance) \
            +quicksort(larger)



def graham_scan(points,show_progress=False):
    global anchor # to be set, (x,y) with smallest y value


    min_idx=None
    for i,(x,y) in enumerate(points):
        if min_idx==None or y<points[min_idx][1]:
            min_idx=i
        if y==points[min_idx][1] and x<points[min_idx][0]:
            min_idx=i


    anchor=points[min_idx]


    sorted_pts=quicksort(points)
    del sorted_pts[sorted_pts.index(anchor)]


    hull=[anchor,sorted_pts[0]]
    for s in sorted_pts[1:]: 
        if len(hull)>=2 :
            
            while det(hull[len(hull)-2],hull[len(hull)-1],s)<=0:
                
                
                del hull[len(hull)-1] # backtrack
                
                if len(hull)<2: break

            hull.append(s)

    return hull





    
