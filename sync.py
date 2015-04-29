import os
import json
import sys, getpass, platform, time
from random import randint

name = randint(0, 99999)

def sys_sep():
	if platform.system() == 'Windows':
		return '\\'
	else:
		return os.path.sep

def get_sys_folder():
	user = getpass.getuser()
	if platform.system() == "Windows":
		return str('C:\\sync\\repos')
	elif platform.system() == "Linux":
		rtn = '/home/' + user + '/.sync/repos/'
		return str(rtn)

def setRepos(path, server):
	
	dic = {'local' : path, 'remote' : server}

	fldr = str(get_sys_folder())

	with open(fldr + sys_sep() + str(name) + '.json', 'w') as out:
		json.dump(dic, out)
	print('Repo added')

def sync_repos():
	repos = os.listdir(get_sys_folder())
	msg = 'Commit: ' + str(time.strftime("%c"))
	path = get_sys_folder() + sys_sep()
	for x in repos:
		data = open(path + x).read()
		json_p = json.loads(data)
		os.system('cd ' + json_p['local'] + ' & git add . & git commit -m auto_commit & git pull & git push')
	print(repos)

def main():	 
	if len(sys.argv) >= 2:
		path = ''
		servr = ''
		isSync = False
		for x in range(0, len(sys.argv)):
			if sys.argv[x] == '-l':
				path = sys.argv[x+1]
			elif sys.argv[x] == '-sv':
				servr = sys.argv[x+1]
			elif sys.argv[x] == '-s':
				sync_repos()
				isSync = True
		if not isSync:
			setRepos(path, servr)
	else:
		print("Usage: " + sys.argv[0] + " -l Adds local repo path -sv Adds Remote Server")

if __name__ == '__main__':
	main()