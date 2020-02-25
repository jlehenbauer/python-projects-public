import subprocess
import os
from multiprocessing import Pool
from pathlib import Path

src = "" # Set the source for the directories to be copied. Any directories within the one listed here will be backed up
dest = "" # Backed-up folders will be stored in this directory (WARNING: this directory must already exist)
# home = str(Path.home()) # Needed for referencial paths on linux

def move_all_files(directory):
	print("moving " + src + directory + " to " + dest + directory)
	subprocess.call(["rsync", -arq, src + directory, dest + directory])

if __name__ == "__main__":
	directories = os.listdir(src)

	# Create a Pool with the list of directories to allow multiprocessing
	p = Pool(len(directories))

	p.map(move_all_files, directories)