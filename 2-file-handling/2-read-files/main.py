f = open("demofile.txt", "r")

print(f)
print(f.read())

f.seek(0) # reset the cursor

print(f.read(5)) # read 5 characters in the file

f.seek(0) # reset the cursor

print(f.readline()) # read 1 line

f.seek(0) # reset the cursor

for line in f:
    print(line, end='')

f.close()
