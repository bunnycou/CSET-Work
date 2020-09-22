##############
# Question 3 #
##############
# python code for tvs with umls

from Q3_2 import TV

def main():

    tv = TV()
    print(f"Initial Status\nPower: {tv.on}\nChannel: {tv.getChannel()}\nVolume: {tv.getVolume()}")

    tv.turnOn()
    tv.setChannel(71)
    tv.channelDown()
    tv.channelDown()
    tv.channelDown()
    tv.channelDown()
    tv.channelUp()
    tv.channelUp()

    tv.setVolume(4)
    tv.volumeUp()
    tv.volumeUp()
    tv.volumeDown()

    print(f"\nSecond Status\nPower: {tv.on}\nChannel: {tv.getChannel()}\nVolume: {tv.getVolume()}")

main()