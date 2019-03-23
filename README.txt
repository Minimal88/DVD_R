## Install dependencies 
sudo apt-get update
sudo apt-get install dvd+rw-tools

## Execute program
# if script is in /home/documents/DVD_scripts
# execute from console with the following commands:
python /home/documents/DVD_scripts/program_1.py
python /home/documents/DVD_scripts/program_2.py

# NOTE: you can't do "cd /home/documents/DVD_scripts" and then "python program_1.py"

## Configurable by user program_1.py
# variable "folder_path" specifies the location where files are generated before burning 
# default setting stores it in a folder located in ~/DVD_files:
folder_path = "/home/"+username+"/DVD_files"

#NOTE: please only change "DVD_files", otherwise the script would need root permissions


## Configurable by user program_2.py
# "folder_path" variable is the same as in "program_1.py"
# "write_file_name" variable defines the name of the file for burning
# "debug", variable in True, enables print in console (for debugging)
# "time_delay", variable defines the seconds between executions of the script

