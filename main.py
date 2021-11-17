import json
import csv
import sys


building = open(sys.argv[1],'r')
data = json.loads(building.read())

call = open(sys.argv[2])
csv_reader = csv.reader(call)
content = call.readlines()

out = csv.reader(open(sys.argv[2]))
lines = list(out)

num_of_elv=len(data[ "_elevators"])

class Elev:

    def __init__(self, id, speed,closeTime,openTime,startTime,stopTime,min,max):
        self.id = int(id)
        self.speed = float(speed)
        self.closeTime = float(closeTime)
        self.openTime = float(openTime)
        self.startTime = float(startTime)
        self.stopTime = float(stopTime)
        self.status = 0
        self.pos = 0
        self.goto = 0
        self.arrStop=[]


class stop:
    def __init__(self,floor,time,status):
        self.floor=floor
        self.time=time
        self.status=status



class Call:

    def __init__(self,id,time,src,tar):
        self.id = int(id)
        self.time = float(time)
        self.src = int(src)
        self.tar = int(tar)
        self.state = 0
        self.elv=-1


    def dir(self):
        if (int(self.src) > int(self.tar)):
            return 1
        else:
            return -1


def findCurFloor(e,c):
    i=len(e.arrStop)-1
    if i==-1:
        return -1
    else:
        while( e.arrStop[i].time>c.time and i >= 0):
            i-=1
    return i

def addStop(c,e):
    i=findCurFloor(e,c)
    if i==-1:
        time = clcTime(e, c.src, 0)+c.time
    else:
        time=clcTime(e,c.src,e.arrStop[i].floor)+e.arrStop[i].time
    e.arrStop.insert(i+1,stop(c.src,time,c.dir))
    addTime(e,i+2)
    i = len(e.arrStop) - 1
    if c.dir == 1:
        while (e.arrStop[i].floor > c.tar):
            i -= 1
    if c.dir==-1:
        while (e.arrStop[i].floor < c.tar):
            i -= 1
    time=clcTime(e,c.tar,e.arrStop[i].floor)+e.arrStop[i].time
    if(i==len(e.arrStop) - 1):
        dir=0
    else:
        dir=c.dir
    e.arrStop.insert(i+1,stop(c.tar,time,dir))
    addTime(e,i+2)


def addTime(e,i):
    add=e.closeTime + e.startTime + e.stopTime + e.openTime
    for j in range(i,len(e.arrStop)):
        e.arrStop[j].time+=add

def findDis(e,i,c):
    if i==-1:
        return abs(0-c.src)
    return abs(e.arrStop[i].floor-c.src)

def clcTime(e,floorA,floorB):
    df=abs(floorA-floorB)
    return e.closeTime + e.startTime + df/e.speed + e.stopTime + e.openTime

def findElv(c):
    mindis=-1
    minStops=-1

    while(c.elv==-1):
        for e in el:
            i= findCurFloor(e,c)
            if(i==-1 or e.arrStop[i].status==0):
                if mindis==-1:
                    mindis=findDis(e,i,c)
                    c.elv=e
                else:
                    if mindis>findDis(e,i,c):
                        mindis=findDis(e,i,c)
                        c.elv = e
            else:
                if c.dir()==e.arrStop[i].status:
                    if (e.arrStop[i].floor<c.src and c.src<e.arrStop[i+1])or (e.arrStop[i].floor>c.src and c.src>e.arrStop[i+1]):
                        if minStops==-1:
                            minStops=len(e.arrStop)-i
                            c.elv=e
                        else:
                            if minStops<len(e.arrStop)-i:
                                minStops = len(e.arrStop) - i
                                c.elv = e
        c.time+=5
    addStop(c,c.elv)


el = []
k = 0
for i in range(num_of_elv):
    id = k
    speed = data['_elevators'][i]['_speed']
    closeTime = data['_elevators'][i]['_closeTime']
    openTime = data['_elevators'][i]['_openTime']
    startTime = data['_elevators'][i]['_startTime']
    stopTime = data['_elevators'][i]['_stopTime']
    min = data['_elevators'][i]['_minFloor']
    max = data['_elevators'][i]['_maxFloor']
    k+=1

    el.append(i)
    el[i] = Elev(id, speed,closeTime,openTime,startTime,stopTime,min,max)

calls = []
for i in range(len(content)):
    temp = content[i].split(',')
    id = i
    time = temp[1]
    src = temp[2]
    tar = temp[3]
    calls.append(i)
    calls[i] = Call(id, time, src,tar)


for i in calls:
    findElv(i)
    lines[i.id][5] = str(i.elv.id)

writer = csv.writer(open(sys.argv[3], 'w',newline=''))
writer.writerows(lines)





