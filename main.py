#Imports
import pyshark

#main function

def main():
    dp = input("Enter Display filer: ")
    cap = pyshark.FileCapture('/home/philip/Documents/internship/app/pcaps/LANtest.pcap', display_filter=dp)
    print(cap[0])


#Calling Main
main()
