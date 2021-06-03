
import os

def package_per():
	i = 1 


	file  = open('list_of_packages.txt', 'r')
	file_permissions  = open('list_of_packages_permissions.txt', 'w')
	for line in file:
		line = line.strip()
		line = line.split(":")
		command =' adb shell "dumpsys package {} | grep permission" '.format(line[1])
		result = os.popen(command).read()
		file_permissions.writelines(line[1]+"\n")
		file_permissions.writelines("\n")
		file_permissions.writelines(result+"\n")
		i = i + 1 
		if i == 5 :
			break
	file_permissions.close()
	file.close()




    #netstat = os.popen(' adb shell "dumpsys package dz.condor.sav | grep permission" ').read()
    #print(netstat)
     
if __name__ == '__main__':
	package_per()

	