##############
# Question 3 #
##############
# Second file for Q3

class TV:
    def __init__(self, channel = 1, volumeLevel = 1, on = False):
        self.channel = channel
        self.volumeLevel = volumeLevel
        self.on = on
    
    def turnOn(self):
        self.on = True
    def turnOff(self):
        self.on = False
    
    def getChannel(self):
        return self.channel
    def setChannel(self, channel):
        self.channel = channel
    def channelUp(self):
        self.channel += 1
    def channelDown(self):
        self.channel -= 1
    
    def getVolume(self):
        return self.volumeLevel
    def setVolume(self, volumeLevel):
        self.volumeLevel = volumeLevel
    def volumeUp(self):
        self.volumeLevel += 1
    def volumeDown(self):
        self.volumeLevel -= 1
    