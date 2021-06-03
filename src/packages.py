import os

def list_of_packages():

	file = open('files/list_of_packages.txt',"w")
	netstat = os.popen('adb shell pm list packages ').read()
	file.write(netstat + "\n")
	file.close()
	print('Done!')


	fh = open("files/list_of_packages.txt", "r")
	lines = fh.readlines()
	fh.close()
	lines = filter(lambda x: not x.isspace(), lines)
	fh = open("files/list_of_packages.txt", "w")
	for line in lines:
	    if line.strip("\n") != "line1":
	    	fh.write("".join(lines))



# This function will get you the list of packages permissions for each package!

def package_permissions():
	file  = open('files/list_of_packages.txt', 'r')
	file_permissions  = open('files/list_of_packages_permissions.txt', 'w')
	for line in file:
		line = line.strip()
		line = line.split(":")
		command =' adb shell "dumpsys package {} | grep permission" '.format(line[1])
		result = os.popen(command).read()
		file_permissions.writelines("--------------------------------------------"+"\n")
		file_permissions.writelines(line[1]+"\n")
		file_permissions.writelines("--------------------------------------------"+"\n")
		file_permissions.writelines(result+"\n")
	file_permissions.close()
	file.close()


if __name__ == '__main__':

	package_permissions()
