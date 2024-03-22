def createfile(file):
    try:
        f=open(file,"w")
        f.write("welcome to my world")
    except IOError:
        print("something went wrong")
def readfile(file):
    try:
        f=open(file,"r")
        print(f.read())
    except IOError:
        print("something went wrong")
def writefile(file,text):
    try:
        f=open(file,"w")
        f.write(text)
    except IOError:
        print("something went wrong")
def appendfile(file,text):
    try:
        f=open(file,"a")
        f.write(text)
    except IOError:
        print("something went wrong")
def rename(filename,new_filename):
    try:
        print("the filename is changed from",filename,"to",new_filename)
        filename=new_filename
    except:
        print("something went wrong")
createfile("jit")
readfile("jit")
writefile("jit","overridden")
readfile("jit")
appendfile("jit","appended")
readfile("jit")
rename("jit","jitendra")