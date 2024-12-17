class TV:
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        self.channels = []
        self.volume = 0
    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def set_channel(self, new_channel_no):
        self.channel_no = new_channel_no

    def set_channels(self, channels_list):
        self.channels=channels_list

    def volume_increase(self, how_much):
        self.volume += how_much
        if self.volume > 10:
            self.volume = 10

    def volume_decrease(self, how_much):
        self.volume -= how_much
        if self.volume < 0:
            self.volume = 0

    def show_channels(self):
        if len(self.channels)!=0:
            print("Channel list:")
            for i in range(len(self.channels)):
                print(i+1,self.channels[i])
        else:
            print("No channels programmed")

    def show_status(self):
        if self.is_on:
            try:
                print(f"TV is on, channel {self.channel_no}({self.channels[self.channel_no-1]}), current volume: {self.volume}")
            except:
                print(f"TV is on, channels not programmed, current volume: {self.volume}")
        else:
            print("TV is off")