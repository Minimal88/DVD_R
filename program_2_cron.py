#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

#Need to install dvd+rw-tools with the following command:
# 'sudo apt-get install dvd+rw-tools'

import os
import os.path
import time


username = os.popen("echo $USER").read().strip()
dvd_mnt_path = "/media/" + username + "/CDROM"


## Configurable by the User ##
folder_path = "/home/"+username+"/DVD_files"
write_file_name = "filename.txt"
DEBUG = True;	##To print DEBUGging define true
TIME_DELAY = 1 ##Every seconds the script is executed
NUM_ATT = 10 ## Number of attemps to burn DVD-R
##############################

dvd_detected = False
dvd_scanned = False
attempts = 0
print("\n> Waiting for DVD...\n")

while attempts<NUM_ATT:
##Check if the folder path exists
	if (os.path.isdir(folder_path)==False):
		print("> Folder path doesn't exists!")
		print("> Creating folder...")
		os.makedirs(folder_path)

##Check if the folders 'write' exists
	if (os.path.isdir(folder_path+"/write")==False):
		print("> Folder 'write' doesn't exists!")
		print("> Creating 'write' folder...")
		os.makedirs(folder_path+"/write")
	
##Check if the folders write_file_name exists
	if (os.path.isfile(folder_path+"/write/"+write_file_name)==False):
		if DEBUG:	
			print("> File '" + write_file_name + "' doesn't exists!")
			print("> Creating '" + write_file_name + "' file...")
		f = open(folder_path+"/write/"+write_file_name,"w+")
		f.write("some data or text")
		f.close()

##Verify there is a DVD-R inserted:	
	dvd_response = str(os.popen("udevadm info -q env -n /dev/sr0").read().strip())
	if "ID_CDROM_MEDIA_DVD_R" not in dvd_response:				
		##print("> NO DVD-R detected!")
		dvd_detected=False
		dvd_scanned = True
		
	elif "ID_CDROM_MEDIA_DVD_R" in dvd_response:
		#TODO: Verify mount is ok in dvd_mnt_path
		dvd_detected=True
		dvd_scanned = True
		time.sleep(5)
		if DEBUG:	
			print("> DVD-R detected!")


##Verify DVD is blank
		dvd_status = str(os.popen("dvd+rw-mediainfo /dev/sr0").read().strip())
		if "Disc status:           blank" in dvd_status:
			if DEBUG:	
				print("> DVD is blank!")			
				print("> Ejecting DVD...")
			os.system("eject /dev/sr0")		

		elif "Disc status:           blank" not in dvd_status:
			if DEBUG:	
				print("> DVD is not blank!")

##Check that readme.txt exists in 'read'
			read_file = str(os.popen("ls "+ dvd_mnt_path + "/read").read().strip()) 
			if read_file=="readme.txt":
				if DEBUG:	
					print("> File 'readme.txt' exists!")
				
##Check 'write' folder doesn't exists
			write_folder = str(os.popen("ls "+ dvd_mnt_path ).read().strip()) 				
			if "write" not in write_folder:	# Remove this if always burn
				if DEBUG:
					#print("> 'Write' folder doesn't exists!")				
					print("> Starting burning process...")			
			#Initiate burning process				
			os.system("growisofs -M /dev/sr0 " + folder_path  + " -speed=2")

	if dvd_detected&dvd_scanned:
		dvd_detected=False
		dvd_scanned = False
		print("\n> Waiting for DVD...\n")

##Check for a DVD every 1 second
	time.sleep(TIME_DELAY)
	attempts=attempts+1
	print("Attempt: " + str(attempts))

				