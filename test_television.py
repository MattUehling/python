from television import Television


class test_television:

    def __init__(self):
        self.tv1 = Television()
        actual_output = str(self.tv1)
        expected_output = "Power = False, Channel = 0, Volume = 0"
        assert actual_output == expected_output
        self.test_power()
        self.reset()
        self.test_mute()
        self.reset()
        self.test_volume_up()
        self.reset()
        self.test_volume_down()
        self.reset()
        self.test_channel_up()
        self.reset()
        self.test_channel_down()

    def reset(self):
        del self.tv1
        self.tv1 = Television()

    def test_power(self):
        self.tv1.power()
        actual_output = str(self.tv1)
        expected_output = "Power = True, Channel = 0, Volume = 0"
        assert actual_output == expected_output

        self.tv1.power()
        actual_output = str(self.tv1)
        expected_output = "Power = False, Channel = 0, Volume = 0"
        assert actual_output == expected_output

    def test_mute(self):
        self.tv1.power()
        self.tv1.volume_up()
        self.tv1.mute()
        actual_output = str(self.tv1)
        expected_output = "Power = True, Channel = 0, Volume = 0"
        assert actual_output == expected_output

        self.tv1.mute()
        actual_output = str(self.tv1)
        expected_output = "Power = True, Channel = 0, Volume = 1"
        assert actual_output == expected_output

        self.tv1.power()
        self.tv1.mute()
        actual_output = str(self.tv1)
        expected_output = "Power = False, Channel = 0, Volume = 1"
        assert actual_output == expected_output

        self.tv1.mute()
        actual_output = str(self.tv1)
        expected_output = "Power = False, Channel = 0, Volume = 1"
        assert actual_output == expected_output

    def test_volume_up(self):
        self.tv1.volume_up()
        actual_output = str(self.tv1)
        expected_output = "Power = False, Channel = 0, Volume = 0"
        assert actual_output == expected_output

        self.tv1.power()
        self.tv1.volume_up()
        actual_output = str(self.tv1)
        expected_output = "Power = True, Channel = 0, Volume = 1"
        assert actual_output == expected_output

        self.tv1.volume_up()
        self.tv1.volume_up()
        actual_output = str(self.tv1)
        expected_output = "Power = True, Channel = 0, Volume = 2"
        assert actual_output == expected_output

        self.tv1.mute()
        self.tv1.volume_up()
        actual_output = str(self.tv1)
        expected_output = "Power = True, Channel = 0, Volume = 2"
        assert actual_output == expected_output

    def test_volume_down(self):
        self.tv1.volume_down()
        actual_output = str(self.tv1)
        expected_output = "Power = False, Channel = 0, Volume = 0"
        assert actual_output == expected_output

        self.tv1.power()
        self.tv1.mute()
        self.tv1.volume_down()
        actual_output = str(self.tv1)
        expected_output = "Power = True, Channel = 0, Volume = 0"
        assert actual_output == expected_output

        self.tv1.volume_down()
        self.tv1.volume_down()
        actual_output = str(self.tv1)
        expected_output = "Power = True, Channel = 0, Volume = 0"
        assert actual_output == expected_output

    def test_channel_up(self):
        self.tv1.channel_up()
        actual_output = str(self.tv1)
        expected_output = "Power = False, Channel = 0, Volume = 0"
        assert actual_output == expected_output

        self.tv1.power()
        self.tv1.channel_up()
        actual_output = str(self.tv1)
        expected_output = "Power = True, Channel = 1, Volume = 0"
        assert actual_output == expected_output

        self.tv1.channel_up()
        self.tv1.channel_up()
        self.tv1.channel_up()
        actual_output = str(self.tv1)
        expected_output = "Power = True, Channel = 0, Volume = 0"
        assert actual_output == expected_output

    def test_channel_down(self):
        self.tv1.channel_down()
        actual_output = str(self.tv1)
        expected_output = "Power = False, Channel = 0, Volume = 0"
        assert actual_output == expected_output

        self.tv1.power()
        self.tv1.channel_down()
        actual_output = str(self.tv1)
        expected_output = "Power = True, Channel = 3, Volume = 0"
        assert actual_output == expected_output


if __name__ == "__main__":
    test_television()
