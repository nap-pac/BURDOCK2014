#Imports
import pyshark

#main function
def main():
    cap = pyshark.FileCapture('/home/philip/Documents/internship/app/pcaps/LANtest.pcap')
    print(cap[0])


#Calling Main
main()
