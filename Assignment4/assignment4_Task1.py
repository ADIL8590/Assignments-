#test read mode
import os
file1= "sample.txt"
if os.path.exists(file1):
    fh = open(file1,"rt")
    content = fh.read()
    fh.close()
    print(content)
else:
    print(f"Error:The file '{file1}' was not found.")