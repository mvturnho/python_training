
# we hebben een auto = Car
# de auto heeft een motor = Engine
# aan de motor zit een versnellingsbak = Gear
# aan de versnellingsbak zitten wielen = Wheel

class Wheel:
    def __init__(self, name, radius):
        self.name = name
        self.radius = radius  # in inch
        self.color = "black"
        self.rpm = 0

    def setRpm(self,rpm):
        self.rpm = rpm
        print( self.name + " rpm=" + str(rpm) + " snelheid is: " + str(self.getSpeed()))

    def getSpeed(self):
        # bereken de km/h obv de rpm en de wiel radius 
        # rpm is omwentelingen per minuut dat moet je omzetten naar rounds per hour
        # de wiel radius moet je omzetten naar omtrek in km
        #TODO: OLAF
        return 100

# Motor class
class Engine:
    def __init__(self, max_rpm):
        self.max_rpm = max_rpm
        self.rpm = 0  # engine rpm/min
        self.usage = 0  # 1 liter for 20 km

    def attachGear(self, gear):
        self.gear = gear

    def setRpmPercent(self, percent):
        self.rpm = self.max_rpm * (percent / 100)
        self.gear.setInputRpm(self.rpm)

# Gear class
class ManualGear:
    def __init__(self, max_gear):
        self.active_gear = 0  # neutral reverse = -1
        self.max_gear = max_gear
        self.inputRpm = 0
        self.wheels = []

    def addWheel(self, wheel):
        self.wheels.append(wheel)

    def setInputRpm(self, rpm):
        self.inputRpm = rpm
        self.updateOutputRpm()
    
    def setGear(self,gear_select):
        self.active_gear = gear_select
        self.updateOutputRpm()

    def updateOutputRpm(self):
        rpm = 0
        print (self.active_gear)
        if(self.active_gear == 0): #neutral
            rpm = 0
        elif(self.active_gear == -1): #reverse
            rpm = -10
        else:
            rpm = self.inputRpm * (self.active_gear / self.max_gear)

        #zet de outputRpm door naar de wielen
        for wheel in self.wheels:
            wheel.setRpm(rpm)

class Car:
    def __init__(self):
        wheel_lfront = Wheel("wheel 1",20)
        wheel_rfront = Wheel("wheel 2",20)
        wheel_lrear =  Wheel("wheel 3",20)
        wheel_rrear =  Wheel("wheel 4",20)

        self.engine = Engine(1000)

        self.gear = ManualGear(6)
        self.gear.addWheel(wheel_lfront)
        self.gear.addWheel(wheel_rfront)
        self.gear.addWheel(wheel_lrear)
        self.gear.addWheel(wheel_rrear)

        self.engine.attachGear(self.gear)

    def setThrottle(self, percent):
        self.engine.setRpmPercent(percent)

    def selectGear(self, gear_select):
        self.gear.setGear(gear_select)


# hier maken we de auto
car = Car()

#kies een versnelling
gear_select = input("\nwelke versnelling wil je? ")
car.selectGear(int(gear_select))

#trap op het gas en de auto gaat rijden
throttle = input("\ngaspedaal in procent? ")
car.setThrottle(int(throttle))
