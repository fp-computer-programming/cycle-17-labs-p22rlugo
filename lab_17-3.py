# Ryan Lugo: RJL 4/12/22

class TV_remote:

    def __init__(self):
        """ Initializing values """
        self.channel = 0
        self.volume = 0
        self.On = False
    
    def to_string(self):
        return "Channel:",self.channel,"Volume:",self.volume,"On:",self.On

tv = TV_remote()
print(tv.to_string())
    