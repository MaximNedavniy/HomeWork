CHANNELS = ["BBC", "Discovery", "TV1000"]


class TVController:

    def __init__(self, CHANNELS):
        self.CHANNELS = CHANNELS
        self.set_channels = 0

    def first_channel(self):
        self.set_channels = 0
        print(self.CHANNELS[self.set_channels])
        return self.CHANNELS[self.set_channels]

    def last_channel(self):
        self.set_channels = -1
        print(self.CHANNELS[self.set_channels])
        return self.CHANNELS[self.set_channels]

    def turn_channel(self, N):
        self.set_channels = N - 1
        print(self.CHANNELS[self.set_channels])
        return self.CHANNELS[self.set_channels]

    def next_channel(self):
        try:
            self.set_channels += 1
            print(self.CHANNELS[self.set_channels])
            return self.CHANNELS[self.set_channels]
        except BaseException:
            self.set_channels = 0
            print(self.CHANNELS[self.set_channels])
            return self.CHANNELS[self.set_channels]

    def previous_channel(self):
        self.set_channels -= 1
        print(self.CHANNELS[self.set_channels])
        return self.CHANNELS[self.set_channels]

    def current_channel(self):
        print(self.CHANNELS[self.set_channels])
        return self.CHANNELS[self.set_channels]

    def exists(self, n_or_name):
        if isinstance(n_or_name, int):
            if n_or_name <= len(CHANNELS) and (not n_or_name < 1):
                print("Yes")
            else:
                print("No")
        else:
            if n_or_name in CHANNELS:
                print("Yes")
            else:
                print("No")


controller = TVController(CHANNELS)

controller.first_channel()
controller.last_channel()
controller.turn_channel(1)
controller.next_channel()
controller.previous_channel()
controller.current_channel()
controller.exists("BBC1")
