#! /usr/bin/env python
from robot_control_class import RobotControl
import numpy as nump

class Microproject:
    def __init__(self,speed,time):
        self.rc=RobotControl()
        self.motion=None
        self.speed=speed
        self.time=time
        self.d=None
    def dist(self):
        return(self.rc.get_laser(360))
    def mov(self):
        distance=self.dist()
        while True:
            while (distance>1):
                self.rc.move_straight()
                distance=self.dist()
                print("The current distance from the wall is: ",distance)
            self.rc.stop_robot()
            self.motion=self.timetoturn()
            self.rc.turn(self.motion,self.speed,self.time)
            distance=self.dist()
    def timetoturn(self):
        self.d=self.rc.get_laser_full()
        l=[]
        m=[]
        count=len(self.d)
        i=0
        j=count/2
        while(i<count/2):
            l.append(self.d[i])
            i=i+1
        while(j<count):
            m.append(self.d[j])
            j=j+1
        v1,v2=self.mean(l,m)
        print("sum of right= ",v1)
        print("sum of left= ",v2)

        if(v1>v2):
            self.d=None
            return "clockwise"
        else:
            self.d=None
            return "counter-clockwise"

    def mean(self,x,y):
        x=np.asarray(x)
        y=np.asarray(y)
        m1=np.sum(x)
        m2=np.sum(y)
        return [m1,m2]

robot=Microproject(speed=0.29,time=5)
robot.mov()


'''count=len(a)
i=0
j=count/2
while(i<count/2):
    l1.append(a[i])
    i=i+1
while(j<count):
    l2.append(a[j])
    j=j+1
l1=np.asarray(l1)
l2=np.asarray(l2)
m1=np.mean(l1)
m2=np.mean(l2)'''



