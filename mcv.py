import sys
import subprocess

def main():
	pdf = sys.argv[1]
	print(pdf)
	subprocess.call(["magick", "convert", "-resize", "1280x720", pdf + ".pdf ", pdf + " %03d.png"])

if __name__ == "__main__":
	main()