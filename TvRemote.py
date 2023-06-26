import random
import time

class TV_Remote():
    def __init__(self, tv_state = "off", tv_volume = 10, channel_list = ["BBC"], channel = "BBC"):
        self.tv_state = tv_state
        self.tv_volume = tv_volume
        self.channel_list = channel_list
        self.channel = channel

    def turn_on_tv(self):
        if (self.tv_state == "on"):
            print("Tv is already on")
        else:
            print("Tv is turning on...")
            time.sleep(1)
            print("Tv is on now.")
            self.tv_state = "on"

    def turn_off_tv(self):
        if (self.tv_state == "off"):
            print("Tv is already off")
        else:
            print("Tv is turning off...")
            time.sleep(1)
            print("Tv is off now.")
            self.tv_state = "off"

    def volume_settings(self):
        while True:
            message = input("Volume up: '>'\nVolume down: '<'\n Exit: 'e'")
            if (message == '>'):
                if (self.tv_volume != 51):
                    self.tv_volume += 1
                    print(("Volume:",self.tv_volume))
            elif (message == '<'):
                if (self.tv_volume != 0):
                    self.tv_volume -= 1
                    print(("Volume:", self.tv_volume))
            else:
                print("Volume updated:",self.tv_volume)
                print(("exiting..."))
                time.sleep(0.8)
                break

    def add_channel(self, channel_name):
        print("Adding the channel...")
        time.sleep(1)
        self.channel_list.append(channel_name)
        print("Channel is added to the list.")

    def random_channel(self):

        randomm = random.randint(0,len(self.channel_list)-1)
        self.channel = self.channel_list[randomm]
        print("Current channel:",self.channel)

    def __len__(self):
        return len(self.channel_list)
    def __str__(self):
        return "TV State: {} \nTV Volume: {} \n Channel List: {} \n Current Channel: {}".format(self.tv_state,self.tv_volume,self.channel_list,self.channel)

remote = TV_Remote()

print("""
        
   ----------TV PROGRAM----------
        
        1. Turn on the TV
        2. Turn off the TV
        3. Volume settings
        4. Add channel
        5. Switch to a random channel
        6. Number of channels
        7. TV states
        
        To exit, please press q.      
        """)
while True:

    process = input("What would you like to do?:")
    if (process == "q"):
        print("Exiting...")
        time.sleep(1)
        print("Logged out.")
        break
    elif (process == "1"):
        remote.turn_on_tv()
    elif ( process == "2"):
        remote.turn_off_tv()
    elif (process == "3"):
        remote.volume_settings()
    elif (process == "4"):
        channel_names = input("Please type the channel separeted by ',' :")
        channel_list = channel_names.split(",")
        for x in channel_list:
            remote.add_channel(x)
    elif (process == "5"):
        remote.random_channel()
    elif (process == "6"):
        print("You have",len(remote),"channels")
    elif (process == "7"):
        print(remote)
    else:
        print("Invalid transaction!")
