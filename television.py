class Television:
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self, status: bool = False, muted: bool = False, volume: int = MIN_VOLUME, channel: int = MIN_CHANNEL) -> None:
        """
        Initializes the Television object.
        """
        self.status = status
        self.muted = muted
        self.volume = volume
        self.channel = channel
        self.savedVolume = volume

    def power(self) -> bool:
        """
        Turns the television on and off.
        """
        if not self.status:
            self.status = True
        else:
            self.status = False
        return self.status

    def mute(self) -> bool:
        """
        Unmutes and mutes the television.
        """
        if self.status:
            if not self.muted:
                self.muted = True
                self.savedVolume = self.volume
                self.volume = 0
            else:
                self.muted = False
                self.volume = self.savedVolume
        return self.muted

    def channel_up(self) -> int:
        """
        Increases the channel number by one.
        """
        if self.status:
            if self.channel == self.MAX_CHANNEL:
                self.channel = self.MIN_CHANNEL
            else:
                self.channel += 1
        return self.channel

    def channel_down(self) -> int:
        """
        Decreases the channel number by one.
        """
        if self.status:
            if self.channel == self.MIN_CHANNEL:
                self.channel = self.MAX_CHANNEL
            else:
                self.channel -= 1
        return self.channel

    def volume_up(self) -> int:
        """
        Increase the volume level by one.
        """
        if self.status:
            if self.muted:
                self.muted = False
                self.volume = self.savedVolume
            if self.volume != self.MAX_VOLUME:
                self.volume += 1
        return self.volume

    def volume_down(self) -> int:
        """
        Decrease the volume level by one.
        """
        if self.status:
            if self.muted:
                self.muted = False
                self.volume = self.savedVolume
            if self.volume != self.MIN_VOLUME:
                self.volume -= 1
        return self.volume

    def __str__(self) -> str:
        """
        Returns a string representation of the Television object.
        """
        return f'Power = {self.status}, Channel = {self.channel}, Volume = {self.volume}'
