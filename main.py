#Imports
import pyshark

#input function
def filt():
    userInput = input("Ender Display filter: ")
    return userInput

#main function
def main():
    df = filt()
    cap = pyshark.FileCapture('/home/philip/Documents/internship/app/pcaps/LANtest.pcap', display_filter=df)
    for packet in cap:
        print(packet.ip)

#Calling Main
main()
