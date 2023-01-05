#Imports
import pyshark
import socket

# FUNCTION: filt
# ------------------
# used for user input and input sanitisation
def filt():
    userInput = input("Ender Display filter: ")
    return userInput


# MAIN
# -------------
# main function for the program
def main():
    #variables
    i = 0
    csv = []

    #get display filer and then apply to captured packets
    df = "ip.addr==126.128.1.45"
    cap = pyshark.FileCapture('/home/philip/Documents/internship/app/pcaps/LANtest.pcap', display_filter=df)

    print(dir(cap[0].ip))
    m = cap[0].ip.ttl
    print(m)
    #Make List of relevant information in order to later print in a .cvs format
    for packet in cap:
        time = packet.sniff_time
        prot = packet.highest_layer
        size = packet.frame_info.len
        ttl = packet.ip.ttl
        srcIp = packet.ip.src
        dstIp = packet.ip.dst
        csv.append([time, srcIp, dstIp, prot, size, ttl])


#Calling Main
main()
