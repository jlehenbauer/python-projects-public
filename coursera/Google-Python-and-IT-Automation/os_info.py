#!"C:\Program Files\Python37\python.exe"
import shutil
import psutil

def check_disk_usage(disk):
	du = shutil.disk_usage(disk)
	free = du.free / du.total * 100
	fig = px.pie(px.data, values=[free, 1-free], names=['Free', 'Used'])
	fig.show()
	return free > 20

def check_cpu_usage():
	usage = psutil.cpu_percent(1)
	cpu_usage = [usage * 100, (1-usage) * 100]
	return usage < 75

if not check_disk_usage("C:/") or not check_cpu_usage():
	print("Check your machine usage!")
else:
	print("Everything's good here!")