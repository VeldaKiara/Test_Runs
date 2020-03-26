handle = open("test.txt", "r")

#reading the whole text
data = handle.read()
print(data)

#reading a single line
data2 = handle.readline()
print(data2)

# reading multiple lines
data3 = handle.readlines()
print(data3)

#looping in a file
data4 = handle.read()
counter = 0
for word in data4.split():
    if word == "Python":
        counter += 1
print(counter)

handle.close()


