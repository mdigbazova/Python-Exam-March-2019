# [x for x in a if x not in b]
# True if len(data.split(' -> ')) == 3 else False
# newList = [x for x in list4Play if x not in list4Check]


from abc import ABC, abstractmethod

class BasicMonster(ABC):
    @abstractmethod
    def __init__(self, name, idM, strength, ugliness):
        self.name = name
        self.idM = idM
        self.strength = strength
        self.ugliness = ugliness


class Hydralisk(BasicMonster):
    def __init__(self, name, idM, strength, ugliness, rangeM=None):
        # range - string of any asci character without space and comma
        BasicMonster.__init__(self, name, idM, strength, ugliness)
        self.rangeM = rangeM


class Zergling(BasicMonster):
    def __init__(self, name, idM, strength, ugliness, speed=None):
        # speed – integer number
        BasicMonster.__init__(self, name, idM, strength, ugliness)
        self.speed = speed



class Army:
    def __init__(self, hyd=None, zer=None):
        self.listHyds = []
        self.listZers = []
        self.allSpeed = 0
        self.allStrength = 0
        self.allHyds = 0
        self.allZers = 0
        if hyd:
            self.newHyd(hyd)
        if zer:
            self.newZer(zer)

    def newZer(self, zer):
        self.listZers.append(zer)

    def newHyd(self, hyd):
        self.listHyds.append(hyd)

    def getSpeed(self):
        for obj in self.listZers:
            self.allSpeed += obj.speed
        return self.allSpeed

    def getStrength(self):
        for obj in self.listHyds:
            self.allStrength += obj.strength
        for obj in self.listZers:
            self.allStrength += obj.strength
        return self.allStrength

    def getCountZers(self):
        #for obj in self.listZers:
        self.allZers += len(self.listZers)
        return self.allZers

    def getCountHyds(self):
        #for obj in self.listHyds:
        self.allHyds += len(self.listHyds)
        return self.allHyds





data = input()
army = Army()

while data != 'stopAddingArmy':
    monster = data.split('(')[0]
    restPars = data.split('(')[1][:-1]
    otherL = list (restPars.split (', '))

    # Hydralisk({name}, {id}, {strength}, {ugliness}, {range})
    if monster == "Hydralisk":
        if len(otherL) < 5:
            print (f"__init__() missing 1 required positional argument: 'range'")
        else:
            name, idM, strength, ugliness, rangeM = otherL[0], otherL[1], otherL[2], otherL[3], otherL[4]
            if rangeM.isdigit():
                print(f"Range must be string")
            else:
                hyd = Hydralisk(name, int(idM), int(strength), int(ugliness), rangeM)
                army.newHyd(hyd)

    elif monster == 'Zergling':
        if len(otherL) < 5:
            print ("__init__() missing 1 required positional argument: 'speed'")
        else:
            name, idM, strength, ugliness, speed = otherL[0], otherL[1], otherL[2], otherL[3], otherL[4]
            if not speed.isdigit():
                print(f"Speed must be integer")
            else:
                zer = Zergling(name,  int(idM), int(strength), int(ugliness), int(speed))
                army.newZer(zer)

    elif monster == 'BasicMonster' or monster == 'BaseMonster':
        #otherL = list(restPars.split(', '))
        if len(otherL) == 4:
            print("Can't instantiate abstract class BaseMonster with abstract methods __init__")

    data = input()


#print:
#     • Overall speed of army: {speed}
#     • Overall strength: {strength}
#     • Hydralisk: {count}; Zergling: {count}
speed = army.getSpeed()
strength = army.getStrength()
countHyds = army.getCountHyds()
countZers = army.getCountZers()
print(f"Overall speed of army: {speed}")
print(f"Overall stength: {strength}")
print(f"Hydralisk: {countHyds}; Zergling: {countZers}")
