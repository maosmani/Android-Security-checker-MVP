import os

def get():

	file = open('files/empty.txt',"w")
	netstat = os.popen('adb shell netstat ').read()
	file.write(netstat + "\n")
	file.close()
	fh = open("files/empty.txt", "r")
	lines = fh.readlines()
	fh.close()
	lines = filter(lambda x: not x.isspace(), lines)
	fh = open("files/out.txt", "w")
	for line in lines:
	    if line.strip("\n") != "line1":
	    	fh.write("".join(lines))

	fh.close()
	lines = open('files/out.txt', 'r').readlines() 
	lines =lines[1:] 
	open('files/out.txt', 'w').writelines(lines) 


