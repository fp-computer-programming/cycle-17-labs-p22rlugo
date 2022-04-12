# Ryan Lugo: RJL 4/12/22

class TV_remote:

    def __init__(self):
        """ Initializing values """
        self.channel = 0
        self.volume = 0
        self.On = False
    
    def to_string(self):
        """ Returns current values for each """
        return "Channel:",self.channel,"Volume:",self.volume,"On:",self.On

    def turn_on(self):
        """ Turns the TV on """
        self.On = True
    
    def turn_off(self):
        """ Turns the TV off """
        self.On = False
    
    def volume_up(self):
        """ Turns the volume up """
        self.volume += 1

    def volume_down(self):
        """ Turns the volume down """
        self.volume -= 1

    def channel_up(self):
        """ Changes the channel to +1 """
        self.channel += 1

    def channel_down(self):
        """ Changes the channel to -1 """
        self.channel -= 1

tv = TV_remote()
print(tv.to_string())
    