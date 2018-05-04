import random

IP="1.1.1.1"
used=[ ]

def getIP():
        return str(random.randint(1,255))+"."+str(random.randint(1,255))+"."+str(random.randint(1,255))+"."+str(random.randint(1,255))
def checkIP():
        for x in range(len(used)):
                if used[x] == str(IP):
                        print(str(IP))
                        getIP()
                        checkIP()
        used.append(str(IP))
        if len(used) == 0:
                used.append(str(IP))
for x in range(10):
        IP=str(getIP())
        checkIP()

for x in range(len(used)):
        print(used[x])
