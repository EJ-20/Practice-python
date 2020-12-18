import os.path

if os.path.isfile("test.txt"):
    print("File exists")
    
    fileout = open("test.txt", "w")
    fileout.write("This is my first line\n")
    fileout.write("This is my second line\n")
    fileout.write("This is my third line\n")
    fileout.write("This is my fourth line\n")
    
    fileout.close()

    filein = open("test.txt", "r")
    line = filein.readline()
    line1 = filein.readline()
    line2 = filein.readline()
    line3 = filein.readline()
    
    print(line)
    print(line1)
    print(line2)
    print(line3)

    filein.seek(0)
    allLines = filein.readlines()
    print(allLines)
    
    filein.close()

    
