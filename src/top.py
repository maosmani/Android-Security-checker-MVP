import time, os

def top():
    f = open('files/process.txt', 'w')
    top  = os.popen(' adb shell top -n 1 ').read()
    f.write(top + "\n")
    f.close()

def saveTop():
	fh = open("files/process.txt", "r")
	lines = fh.readlines()
	fh.close()
	lines = filter(lambda x: not x.isspace(), lines)
	fh = open("files/prout.txt", "w")
	for line in lines:
	    if line.strip("\n") != "line1":
	    	fh.write("".join(lines))

	fh.close()
	lines = open('files/prout.txt', 'r').readlines() 
	lines =lines[1:] 
	open('files/procfinal.txt', 'w').writelines(lines) 
