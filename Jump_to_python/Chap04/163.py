f = open("D:/Python_workplace/jumptopy/Chap04/temp\myfile/newfile.txt",'r')

while True:
    line=f.readline()
    if not line: break
    print(line)

f.close()