file1 = open("file1.txt","r")
value = int(file1.read())
val = value*20
file2 = open("file2.txt","w")
valie = str(val)
file2.write(valie)
file1.close()
file2.close()
