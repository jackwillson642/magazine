import os
import shutil
import time
from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter import messagebox as mb

# def execute(source_entry, bullet_entry, execute_button, output_box, bar):
def execute(root, source_entry, bullet_entry, execute_button, output_box):

    execute_button["state"] = 'disabled'   # Disabling button till process is complete

    source = source_entry.get()
    bullet = bullet_entry.get()

    try:
        bar_and_window = pgbar(root)
        bar = bar_and_window[0]
        bar_window = bar_and_window[1]
        bar.start(10)
        os.chdir(bullet)
        for root, dirs, files in os.walk(".", topdown=True):
            for file in files:
                src = os.path.join(root, file)
                dest = os.path.join(source, root, file)
                output_box.insert('end', (f"Copying '{src}' to '{dest}'"))
                shutil.copyfile(src, dest)
                output_box.insert('end', ("  Done\n"))
        bar.stop()
        bar_window.destroy()
        bar_window.update()
        mb.showinfo(title="Message", message="Process Completed.")
        source_entry.delete(0)
        bullet_entry.delete(0)
    except FileNotFoundError:
        bar_window.destroy()
        bar_window.update()
        mb.showinfo(title="Warning", message="Something is wrong with the directory paths entered")

    execute_button["state"] = 'normal'  # Enabling button


def source_get_path(root):
    path = fd.askdirectory(title="Please select the source code folder")
    source_entry.insert(0, (path))

def bullet_get_path(root):
    path = fd.askdirectory(initialdir="/home/jack", title="Please select the folder containing the changes")
    bullet_entry.insert(0, (path))


def layout(root):
    global source_entry
    global bullet_entry
    global execute_button

    # Defining elements
    source_lbl = Label(root, text="Source code folder path")
    source_entry = Entry(root, width=80)
    source_browse = Button(root, text="Browse", command=lambda: source_get_path(root))
    bullet_lbl = Label(root, text="Client changes folder path")
    bullet_entry = Entry(root, width=80)
    bullet_browse = Button(root, text="Browse", command=lambda: bullet_get_path(root))
    output_lbl = Label(root, text="Output:")
    output_box = Text(root, height=20, width=100)
    execute_button = Button(root,text="Execute", command=lambda:execute(root, source_entry, bullet_entry, execute_button, output_box), width=20, height=3)

    source_entry.focus_set()

    # Placing elements on he screen
    source_lbl.grid(row=0, column=0, padx=30, pady=10, sticky='', columnspan=2)
    source_entry.grid(row=1, column=0, padx=30, pady=10)
    source_browse.grid(row=1, column=1, padx=30, pady=10)
    bullet_lbl.grid(row=2, column=0, padx=30, pady=10, sticky='', columnspan=2)
    bullet_entry.grid(row=3, column=0, padx=30, pady=10)
    bullet_browse.grid(row=3, column=1, padx=30, pady=10)
    execute_button.grid(row=4, column=0, padx=30, pady=10, sticky='', columnspan=2)
    output_lbl.grid(row=5, column=0, padx=30, pady=10, sticky='', columnspan=2)
    output_box.grid(row=6, column=0, padx=30, pady=10, sticky='', columnspan=2)

    paths = (source_entry, bullet_entry)

def pgbar(root):
    bar_window = Toplevel(root)
    bar_window.geometry("300x100")
    bar_window.title("Copying...")
    bar_window.attributes('-type', 'dialog')
    bar = ttk.Progressbar(
        bar_window,
        length = 200,
        orient = 'horizontal',
        # maximum = 100,
        # value = 50,
        mode = "indeterminate"
    )
    bar.pack()
    package = (bar, bar_window)
    return package
