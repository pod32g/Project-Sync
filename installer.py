import os
import platform, getpass

#This will create the necesary folders on linux this should be run as root, on windows as administrator

user = getpass.getuser()


if platform.system() == 'Windows':
	os.system('mkdir C:\sync')
	os.system('mkdir C:\sync\repos')
	
elif platform.system() == 'Linux':
	os.system('mkdir /home/' + user + '/.sync/')
	os.system('mkdir /home/' + user + '/.sync/repos')
	pass