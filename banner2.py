import socket
import sys
import os 
def retBanner(ip, port):
        try:
                socket.setdefaulttimeout(2)
                s = socket.socket()
                s.connect((ip, port))
                banner = s.recv(1024)
                banners = banner.decode('utf-8')
                return banners
        except:
                return
def checkVulns(banners, filename):
    f = open(filename,"r")
    for line in f.read().splitlines():
    	if line in banners:
    		print("Server is vulnerable "+banners)
def main():
	if len(sys.argv) == 2:
		filename = sys.argv[1]
		print (filename)
		if not os.path.isfile(filename):
			print (filename+' does not exist')
			exit(0)
		if not os.access(filename, os.R_OK):
			print (filename+' access denied')
			exit(0)
		else:	
			print ('Usuage '+str(sys.argv[0]))
			portList = [21,22,25,80,110,443]
			for x in range(128,130):
                		ip = "192.168.118."+str(x)
                		for port in portList:
                        		banner1 = retBanner(ip, port)
                        		if banner1:
                                		print (""+ip+":"+str(banner1))
                                		checkVulns(banner1, filename)
if __name__ == '__main__':
        main()
