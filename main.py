import os, shutil

source = input("Enter Source code folder path: ")
bullet = input("Enter client changes folder path: ")

# source = "/home/jack/programming/python/magazine/src"
# bullet = "/home/jack/programming/python/magazine/c1/"

os.chdir(bullet)
for root, dirs, files in os.walk(".", topdown=True):
    for file in files:
        src = os.path.join(root, file)
        # dest = source + os.path.join(root, file)
        dest = os.path.join(source, root, file)
        print(src+" copied to  "+dest)
        shutil.copyfile(src, dest)
