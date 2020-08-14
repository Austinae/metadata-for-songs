from os import listdir, rename, path
from tkinter.filedialog import askdirectory, Tk
from sys import exit
import eyed3


try:
    Tk().withdraw() # Avoids showing tk window
    filename = askdirectory()
    listFiles = listdir(filename)
    #
    for file in listFiles:
        fileNameAndExtension = path.splitext(file)
        input(fileNameAndExtension)



except FileNotFoundError:
    exit(0)