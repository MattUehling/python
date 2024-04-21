from television import Television
import pytest


class TestTelevision:

    @pytest.fixture
    def tv1(self):
        return Television()

    def test_initial_state(self, tv1):
        actual_output = str(tv1)
        expected_output = "Power = False, Channel = 0, Volume = 0"
        assert actual_output == expected_output

    def test_power(self, tv1):
        tv1.power()
        actual_output = str(tv1)
        expected_output = "Power = True, Channel = 0, Volume = 0"
        assert actual_output == expected_output

        tv1.power()
        actual_output = str(tv1)
        expected_output = "Power = False, Channel = 0, Volume = 0"
        assert actual_output == expected_output

    def test_mute(self, tv1):
        tv1.power()
        tv1.volume_up()
        tv1.mute()
        actual_output = str(tv1)
        expected_output = "Power = True, Channel = 0, Volume = 0"
        assert actual_output == expected_output

        tv1.mute()
        actual_output = str(tv1)
        expected_output = "Power = True, Channel = 0, Volume = 1"
        assert actual_output == expected_output

        tv1.power()
        tv1.mute()
        actual_output = str(tv1)
        expected_output = "Power = False, Channel = 0, Volume = 1"
        assert actual_output == expected_output

        tv1.mute()
        actual_output = str(tv1)
        expected_output = "Power = False, Channel = 0, Volume = 1"
        assert actual_output == expected_output

    def test_volume_up(self, tv1):
        tv1.volume_up()
        actual_output = str(tv1)
        expected_output = "Power = False, Channel = 0, Volume = 0"
        assert actual_output == expected_output

        tv1.power()
        tv1.volume_up()
        actual_output = str(tv1)
        expected_output = "Power = True, Channel = 0, Volume = 1"
        assert actual_output == expected_output

        tv1.volume_up()
        tv1.volume_up()
        actual_output = str(tv1)
        expected_output = "Power = True, Channel = 0, Volume = 2"
        assert actual_output == expected_output

        tv1.mute()
        tv1.volume_up()
        actual_output = str(tv1)
        expected_output = "Power = True, Channel = 0, Volume = 2"
        assert actual_output == expected_output

    def test_volume_down(self, tv1):
        tv1.volume_down()
        actual_output = str(tv1)
        expected_output = "Power = False, Channel = 0, Volume = 0"
        assert actual_output == expected_output

        tv1.power()
        tv1.mute()
        tv1.volume_down()
        actual_output = str(tv1)
        expected_output = "Power = True, Channel = 0, Volume = 0"
        assert actual_output == expected_output

        tv1.volume_down()
        tv1.volume_down()
        actual_output = str(tv1)
        expected_output = "Power = True, Channel = 0, Volume = 0"
        assert actual_output == expected_output

    def test_channel_up(self, tv1):
        tv1.channel_up()
        actual_output = str(tv1)
        expected_output = "Power = False, Channel = 0, Volume = 0"
        assert actual_output == expected_output

        tv1.power()
        tv1.channel_up()
        actual_output = str(tv1)
        expected_output = "Power = True, Channel = 1, Volume = 0"
        assert actual_output == expected_output

        tv1.channel_up()
        tv1.channel_up()
        tv1.channel_up()
        actual_output = str(tv1)
        expected_output = "Power = True, Channel = 0, Volume = 0"
        assert actual_output == expected_output

    def test_channel_down(self, tv1):
        tv1.channel_down()
        actual_output = str(tv1)
        expected_output = "Power = False, Channel = 0, Volume = 0"
        assert actual_output == expected_output

        tv1.power()
        tv1.channel_down()
        actual_output = str(tv1)
        expected_output = "Power = True, Channel = 3, Volume = 0"
        assert actual_output == expected_output


if __name__ == "__main__":
    pytest.main()
