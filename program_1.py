#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

#Need to install dvd+rw-tools with the following command:
# 'sudo apt-get install dvd+rw-tools'

import os
import os.path

username = os.popen("echo $USER").read().strip()

## Configurable by the User ##
folder_path = "/home/"+username+"/DVD_files"
##############################


##Check if the folder path exists
if (os.path.isdir(folder_path)==False):
	print("> Folder path doesn't exists!")
	print("> Creating folder...")
	os.makedirs(folder_path)

##Check if the folder 'read' exists
if (os.path.isdir(folder_path+"/read")==False):
	print("> Folder 'read' doesn't exists!")
	print("> Creating 'read' folder...")
	os.makedirs(folder_path+"/read")

##Check if the folders readme.txt exists
if (os.path.isfile(folder_path+"/read/readme.txt")==False):
	print("> File 'read/readme.txt' doesn't exists!")
	print("> Creating 'read/readme.txt' file...")
	f = open(folder_path+"/read/readme.txt","w+")
	f.write("readme")
	f.close()


##Verify there is a DVD-R inserted:
dvd_response = str(os.popen("dvd+rw-mediainfo /dev/sr0").read().strip())
if "DVD-R" not in dvd_response:	
	print("> NO DVD-R detected!")
	print("> Exiting program...")
	exit()

elif "DVD-R" in dvd_response:
	print("> DVD-R detected!")

##Verify DVD is blank
	if "Disc status:           blank" not in dvd_response:
		print("> DVD is not blank!")
		print("> Ejecting DVD...")
		os.system("eject /dev/sr0")
		print("> Exiting program...")
		exit()

	elif "Disc status:           blank" in dvd_response:
		print("> DVD is blank!")
		print("> Starting burning process...")	
		
		#Initiate burning process
		os.system("growisofs -Z /dev/sr0 " + folder_path + " -speed=2")
		print("> Exiting program...")