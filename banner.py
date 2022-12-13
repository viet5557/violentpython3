import socket
def retBanner(ip, port):
	try:
		socket.setdefaulttimeout(2)
		s = socket.socket()
		s.connect((ip, port))
		banner = s.recv(1024)
		return banner
	except:
		return
def checkVulns(banner):
	if b'FileZilla' in banner:
		print ("FileZIlla is vuln")
	elif b'3Com 3CDaemon FTP Server Version 2.0' in banner:
		print ("3Com 3CDaemon is vuln)")
	elif b'Ability Server 2.34' in banner:
		print ("Ability is vuln)")
	elif b'Sami FTP Server 2.0.2' in banner:
		print ("Sami is vuln)")
	else:
		print ("FTP Server is not vulnerable.")
	return

def main():
	portList = [21,22,25,80,110,443]
	for x in range(245,248):
		ip = "192.168.1."+str(x)
		for port in portList:
			banner1 = retBanner(ip, port)
			if banner1:
				print (""+ip+":"+str(banner1))
				checkVulns(banner1)
if __name__ == '__main__':
	main()	

	
