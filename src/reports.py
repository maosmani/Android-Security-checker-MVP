
from fpdf import FPDF 
from tkinter.filedialog import asksaveasfile
"""
pdf = FPDF() 

pdf.add_page() 

pdf.set_font("Arial", size = 12) 

f = open("out.txt", "r") 

for x in f: 
	pdf.cell(100, 50, txt = x, ln = 1, align = 'L') 
pdf.output("doc/love.pdf")
"""
#function that save report of connections
def connections_report():
	
	f = open("files/out.txt", "r") 
	
	#file = asksaveasfile(defaultextension=".txt")
	file = asksaveasfile(defaultextension=".txt")
	file.write(f)
    
