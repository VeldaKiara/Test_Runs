handle = open("text-write.txt", "w")
handle.write("Hey honeybunch")
handle.close()

#python has a with operator that can simplify how 
# we read and write files.
# The operator creates a context manager 
#that automatically closes the file when you are done.
with open("test.txt","r") as handle:
    data = handle.read()
    print(data)