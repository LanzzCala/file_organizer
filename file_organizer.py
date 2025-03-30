import os

print (f"I am working in this directory. {os.getcwd()}")
os.chdir("c:\\Users\\lanzz\\OneDrive\\Desktop")
print(f"Now i will work in this directory: {os.getcwd()}")
print (os.listdir())
with open('test files', 'r', encoding="utf-8") as x:
    read_files = x.read()

