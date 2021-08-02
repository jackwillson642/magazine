import os, shutil
from tkinter import *

root = Tk()
root.title('Dashboard')
root.geometry('800x600')

global source_entry
global bullet_entry
global output_box

def execute():
    execute_button["state"] = 'disabled'
    source = source_entry.get()
    bullet = bullet_entry.get()
    os.chdir(bullet)
    for root, dirs, files in os.walk(".", topdown=True):
        for file in files:
            src = os.path.join(root, file)
            dest = os.path.join(source, root, file)
            shutil.copyfile(src, dest)
            output_box.insert('end', (src + " copied to " + dest + '\n'))
    execute_button["state"] = 'normal'


# source = input("Enter Source code folder path: ")
# bullet = input("Enter client changes folder path: ")

# source = "/home/jack/programming/python/magazine/src"
# bullet = "/home/jack/programming/python/magazine/c1/"

# os.chdir(bullet)
# for root, dirs, files in os.walk(".", topdown=True):
#     for file in files:
#         src = os.path.join(root, file)
#         # dest = source + os.path.join(root, file)
#         dest = os.path.join(source, root, file)
#         print(src+" copied to  "+dest)
#         shutil.copyfile(src, dest)


source_entry = Entry(root, width=100)
source_lbl = Label(root, text="Source code folder path")
bullet_entry = Entry(root, width=100)
bullet_lbl = Label(root, text="Client changes folder path")
source_entry.focus_set()

source_lbl.pack(padx=30, pady=10)
source_entry.pack(padx=30, pady=10)
bullet_lbl.pack(padx=30, pady=10)
bullet_entry.pack(padx=30, pady=10)

execute_button = Button(root,text="Execute", command=execute, width=20, height=3)
execute_button.pack(padx=30, pady=10)

output_lbl = Label(root, text="Output:")
output_box = Text(root, height=20, width=100)

output_lbl.pack(padx=30, pady=10)
output_box.pack(padx=30, pady=10)


root.mainloop()
