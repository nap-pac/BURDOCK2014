#Imports
import pyshark

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

    df = filt()
    cap = pyshark.FileCapture('/home/philip/Documents/internship/app/pcaps/LANtest.pcap', display_filter=df)

    srcIp = cap[0].ip.src
    dstIp = cap[0].ip.dst
    csv.append([srcIp, dstIp])
    for a in csv:
        print(a[0] + " and " + a[1])

    #Make List of relevant information in order to later print in a .cvs format
    #for packet in cap:
        #srcIp = packet.ip.src
        #dstIp = packet.ip.dst
        #csv.append([srcIp, dstIp])

#Calling Main
main()
