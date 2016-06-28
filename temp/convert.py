import datetime
import sys


def main():
    f = open("superfile.txt", "a")
    d = datetime.datetime.now()
    print "juhu ", str(d)
    f.writelines(str(d) + " arg count: " + str(len(sys.argv)) +
                 " args: " + str(sys.argv) + "\n")


if __name__ == '__main__':
    main()
