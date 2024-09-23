# ---------------------------------- append ---------------------------------- #

f = open("demo1.txt", "a")
f.write("Now the file has more content!\n")
f.close()

f = open("demo1.txt", "r")
print(f.read())
f.close()

# ----------------------------------- write ---------------------------------- #

f = open("demo2.txt", "w")
f.write("Woops! I have deleted the content!\n")
f.close()

f = open("demo2.txt", "r")
print(f.read())
f.close()

# ---------------------------------- create ---------------------------------- #

f = open("myfile1.txt", "x")

# or

f = open("myfile2.txt", "w")

# or

f = open("myfile3.txt", "a")
