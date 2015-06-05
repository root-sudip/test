import sys
from colorama import Fore, Back, Style
import time
string = str(sys.argv[1])
print(Fore.WHITE+" ")
print(Fore.GREEN+"Name of the file is : "+string)

print (Fore.WHITE+"")


_fo=open(string,"r")
_fo_symbol=open("symbol","r")

line=_fo.readline()

while line:
	print(Fore.GREEN+"Reading Line ... ")

	for i in range(1,5):
		time.sleep(0.4)
	for j in line:
		print(j)

	print(Fore.RED+line)
	print(Fore.WHITE+" ")

	line=_fo.readline()
	
print(Fore.WHITE+" ")

