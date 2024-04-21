class Television:
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self, status: bool = False, muted: bool = False, volume: int = MIN_VOLUME, channel: int = MIN_CHANNEL) -> None:
        """
        Initializes the Television object.
        """
        self.__status = status
        self.__muted = muted
        self.__volume = volume
        self.__channel = channel
        self.saved_volume = volume

    def power(self) -> None:
        """
        Turns the television on and off.
        """
        if not self.__status:
            self.__status = True
        else:
            self.__status = False

    def mute(self) -> None:
        """
        Unmutes and mutes the television.
        """
        if self.__status:
            if not self.__muted:
                self.__muted = True
                self.saved_volume = self.__volume
                self.__volume = Television.MIN_VOLUME
            else:
                self.__muted = False
                self.__volume = self.saved_volume

    def channel_up(self) -> None:
        """
        Increases the __channel number by one.
        """
        if self.__status:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self) -> None:
        """
        Decreases the __channel number by one.
        """
        if self.__status:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self) -> None:
        """
        Increase the __volume level by one.
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = self.saved_volume
            if self.__volume != Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        Decrease the __volume level by one.
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = self.saved_volume
            if self.__volume != Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        Returns a string with the values of the television object.
        """
        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
