f = open("D:/Python_workplace/jumptopy/Chap04/temp\myfile/newfile.txt",'a')

for i in range(11,20):
    data = "%d 번쨰 줄입니다.\n" %i
    f.write(data)

f.close()