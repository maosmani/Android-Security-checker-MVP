from tkinter import *
from tkinter import ttk

import getconnections as connection
import top 
import whoisip
from ipwhois import IPWhois
import socket
 
from ipaddress import ip_address, IPv4Address
  
def validIPAddress(IP: str) -> str:
    try:
        return "IPv4" if type(ip_address(IP)) is IPv4Address else "IPv6"
    except ValueError:
        return "Invalid"

import time


def IPAddress(IP: str) -> str: 
    return "Private" if (ip_address(IP).is_private) else "Public"
#This new function will show you what are the services that your device is connected to
def Proc():
    line = " List of The Processes that are running on your device is : "
    print(line)
    Text.delete(1.0,END)
    Text.insert(END, line + "\n")
    top.top()
    top.saveTop()
    fh = open('procfinal.txt','r')
    for line in fh:
        Text.insert(END, line + "\n")

def portConnectedTo():
    Text.delete(1.0,END)
    line = "Wellcome!!!"
    Text.insert(END, line + "\n") 
    f = open("out.txt", "r")
    for line in f:
        lineSplit = line.split()
        ip = lineSplit[4].split(":")
        #Print the last elements
        protocol = lineSplit[0]
       
        portNumber = ip[-1]
       
        if portNumber != "*":
            try:
                portNumber = int(ip[-1])
                serviceName = socket.getservbyport(portNumber, protocol)
                
                message = "Name of the service running at port number %d : %s"%(portNumber, serviceName)
                message = str(message)
                Text.insert(END, message + "\n")
                root.update_idletasks()
            except OSError:
                
                message = "No matching port number with this protocol"
                message = str(message)
                Text.insert(END, message + "\n")
                root.update_idletasks()
        else:
            print('this is local address')
        """    
        message = str(message)
        Text.insert(END, message + "\n")
        root.update_idletasks()
        """



def conn():
    Text.delete(1.0,END)
    line = "Hello man"
    Text.insert(END, line + "\n") 
     
    connection.get()
   
    f = open("out.txt", "r")
    for line in f:
      
        lineSplit = line.split()
        ip = lineSplit[4].split(":")

        ipLook = ""
        if len(ip) > 2:
            ipLook = ip[0]+":"+ip[1]+":"+ip[2]+":"+ip[3]
        else:
            ipLook = ip[0]
       
        #sprint(validIPAddress(ipLook)) 

        if ipLook != ':::*':
            ipLook = ipLook
        else:
            ipLook = '0:0:0:0:0:0:0:0'

        #ipLook = socket.gethostbyname(ipLook)
        ipType =    IPAddress(ipLook)
        r = ""
        if ipType == "Public":
           
            obj = IPWhois(ipLook)
            try:
                results = obj.lookup_whois()
            except:
                results = "Network erreur!!"
             
            
            #print(type(results['asn_description']))
            message = "  The ip address : "+ ipLook +" Belong to " + results['asn_description']
            message = str(message)
            Text.insert(END, message + "\n")
            root.update_idletasks()
            #time.sleep(2)
          
            #pprint(obj.lookup_whois())
            #print(socket.getfqdn(ipLook))#This part of the code will get you the domains and ip addresses where your device is connected to

        else:
            
            
            message ="  The Address :" + ipLook + "is a pravite ip address!"
            Text.insert(END, message + "\n")
            root.update_idletasks()
            #time.sleep(2)
           


"""    
 
def Check():
    if (var1.get() == 1) & (var2.get() == 1):
        Text.delete(1.0,END)
        connection.get()
        #top.top()
        #top.saveTop()
        f = open("out.txt", "r")
        for line in f:
            Text.insert(END, line + "\n") 
        fh = open('procfinal.txt','r')
        for line in fh:
            Text.insert(END, line + "\n")
    elif (var1.get() == 1) & (var2.get() == 0):
        Text.delete(1.0, END)
        connection.get()
        f = open("out.txt","r")
        for line in f:
            Text.insert(END, line + "\n")
    elif (var1.get() == 0) & (var2.get() == 1):
        Text.delete(1.0, END)
        top.top()
        top.saveTop()
        fh = open("procfinal.txt","r")
        for line in fh:
            Text.insert(END, line + "\n")
    else:
        Text.delete(1.0, END)
        text = " You did not chose the information that we can show you man!"
        Text.insert(END, text + "\n")
       
def whoisAddress():
    whoisip.whoisip()
    Text.delete(1.0, END)
    fh = open('public_ip_to_websites.txt',"r")
    for line in fh:
        Text.insert(END, line + "\n")
"""

root = Tk()
root.title("ADB test ")
#root.geometry("1200x500")
#root.resizable(width=False, height=False)
# !this part of the code is to declare two frames

frameCommand = Frame(root)
frameCommand.pack(fill = BOTH , expand = True)

frameText = Frame(root) 
frameText.pack(fill = BOTH, expand = True) 

#end of frames 
"""
Label(root, text = 'GeeksforGeeks',  
      font =('Verdana', 15)).pack(side = TOP, pady = 10) 

var1 = IntVar()
var2 = IntVar()
CheckbuttonOne= Checkbutton(root, text='Network connections',variable=var1, onvalue=1, offvalue=0)
CheckbuttonOne.pack()
CheckbuttonTwo= Checkbutton(root, text='Processes',variable=var2, onvalue=1, offvalue=0)
CheckbuttonTwo.pack()
  
Button(root, text = 'Check box exection code !', command=Check ).pack(side = TOP) 
Button(root, text = 'Whois your device connected to ', command=whoisAddress ).pack(side = TOP) 

Text = Text(root) 
Text.pack(expand=True, fill='both', side=LEFT)
scroll_bar = Scrollbar(root)
scroll_bar.pack(side=RIGHT, fill=Y)
Text.config(yscrollcommand=scroll_bar.set)
scroll_bar.config(command=Text.yview)

"""
Label(frameCommand, text = 'Android Connections Checker',  
      font =('Verdana', 15)).grid(row = 0, column = 0,sticky = W, pady = 5, padx=10) #pack(side = TOP, pady = 10) 
portConnectedTo
var1 = IntVar()
var2 = IntVar()
#CheckbuttonOne= Checkbutton(frameCommand, text='Network connections',variable=var1, onvalue=1, offvalue=0)
#CheckbuttonOne.grid(row = 1, column = 0,sticky = W, pady = 5, padx=10) #pack()
#CheckbuttonTwo= Checkbutton(frameCommand, text='Processes',variable=var2, onvalue=1, offvalue=0)
#CheckbuttonTwo.grid(row = 2, column =0, sticky = W, pady = 5, padx=10) #pack()
Button(frameCommand,text = 'IP Connections', command=conn, relief=RAISED, height = 2, 
          width = 15).grid(row = 3, column = 0, sticky = W, pady = 5, padx=10) #.pack(side = TOP) 
Button(frameCommand, text = 'Services', command=portConnectedTo, relief=RAISED,height = 2, 
          width = 15).grid(row = 4, column = 0, sticky = W, pady = 5, padx=10) #pack(side = TOP) 
Button(frameCommand, text = 'Processes', command=Proc, relief=RAISED,height = 2, 
          width = 15).grid(row = 3, column = 1, sticky = W, pady = 5, padx=10) #pack(side = TOP) 


Text = Text(frameText) 
Text.pack(expand=True, fill='both', side=LEFT)
scroll_bar = Scrollbar(frameText)
scroll_bar.pack(side=RIGHT, fill=Y)
Text.config(yscrollcommand=scroll_bar.set)
scroll_bar.config(command=Text.yview)


root.mainloop()