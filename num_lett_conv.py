import sys

def main():
    if sys.argv[1] is not None:
        try:
            num = int(sys.argv[1])
            fl = num // 26
            sl = num % 26
            if fl == 0:
                return chr(sl + 96)
            elif sl == 0:
                if fl == 1:
                    return chr(int(sys.argv[1]) + 96)
                return chr(fl + 96)
            return chr(fl + 96) + chr(sl + 96)
        except:
            if len(sys.argv[1]) == 1:
                return ord(sys.argv[1]) - 96
            else:
                return (ord(sys.argv[1][0]) - 96)*26 + (ord(sys.argv[1][1]) - 97)

if __name__ == "__main__":
    print(main())