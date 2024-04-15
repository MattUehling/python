class Television:
    MIN_VOLUME =0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3
    def __init__(self, status = False, muted = False, volume = MIN_VOLUME, channel = MIN_CHANNEL):
        self.status = status
        self.muted = muted
        self.volume = volume
        self.channel = channel
        self.savedVolume = volume
    def power(self):
        if self.status == False:
            self.status = True
        else:
            self.status = False
    def mute(self):
        if self.status == True:
            if self.muted == False:
                self.muted = True
                self.savedVolume = self.volume
                self.volume = 0
            else:
                self.muted = False
            
    def channel_up(self):
        if self.status == True:
            if self.channel == self.MAX_CHANNEL:
                self.channel = self.MIN_CHANNEL
            else:
                self.channel+=1

    def channel_down(self):
        if self.status == True:
            if self.channel == self.MIN_CHANNEL:
                self.channel = self.MAX_CHANNEL
            else:
                self.channel-=1

    def volume_up(self):
        if self.status == True:
            if self.muted == True:
                self.muted = False
                self.volume = self.savedVolume
            if self.volume != self.MAX_VOLUME:
                self.volume+=1

    def volume_down(self):
        if self.status == True:
            if self.muted == True:
                self.muted = False
                self.volume = self.savedVolume
            if self.volume != self.MIN_VOLUME:
                self.volume-=1
    def __str__(self):
        return  f'Power = {self.status}, Channel = {self.channel}, Volume {self.volume}'

            