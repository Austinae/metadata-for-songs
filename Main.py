from os import listdir, rename, path
from tkinter.filedialog import askdirectory, Tk
from sys import exit
from tinytag import TinyTag
import re


# try:
#     Tk().withdraw() # Avoids showing tk window
#     dir = askdirectory()
#     listFiles = listdir(dir)
#
#     for file in listFiles:
#         fileNameAndExtension = path.splitext(file)
#         if fileNameAndExtension[1] == ".mp3":
#             audioFile = TinyTag.get(dir+"/"+file)
#             input(audioFile)
#
# except FileNotFoundError:
#     exit(0)

try:
    Tk().withdraw() # Avoids showing tk window
    dir = askdirectory()
    listFiles = listdir(dir)

    for file in listFiles:
        fileNameAndExtension = path.splitext(file)
        if fileNameAndExtension[1] == ".mp3":

            formatArtist = re.compile("^[a-zA-Z0-9+].* -")
            formatTitle = re.compile("- [a-zA-Z0-9+].*")
            formatFeat = re.compile("\(Feat. [a-zA-Z0-9+].*\)")
            formatRemix = re.compile("\(Remix. [a-zA-Z0-9+].*\)")

            artistSearch = formatArtist.search(fileNameAndExtension[0])
            titleSearch = formatTitle.search(fileNameAndExtension[0])
            featSearch = formatFeat.search(fileNameAndExtension[0])
            remixSearch = formatRemix.search(fileNameAndExtension[0])

            artist = artistSearch.group().replace(" -", "").strip()

            try:
                title = titleSearch.group().replace("- ", "").replace(featSearch.group(), "").replace(
                    remixSearch.group(), "").strip()
            except:
                try:
                    title = titleSearch.group().replace("- ", "").replace(remixSearch.group(), "").strip()
                except:
                    try:
                        title = titleSearch.group().replace("- ", "").replace(featSearch.group(), "").strip()
                    except:
                        title = titleSearch.group().replace("- ", "").strip()

            try:
                feat = featSearch.group().replace("(Feat. ", "").replace(")", "").split(", ")
                feat = [item.strip() for item in feat]
            except AttributeError:
                pass

            try:
                remix = remixSearch.group().replace("(Remix. ", "").replace(")", "").split(", ")
                remix = [item.strip() for item in remix]
            except AttributeError:
                pass

            try:
                print(f"Artist: '{artist}'\nTitle: '{title}'\nFeat: {feat}\nRemix: {remix}")
            except:
                try:
                    print(f"Artist: '{artist}'\nTitle: '{title}'\nFeat: {feat}")
                except:
                    try:
                        print(f"Artist: '{artist}'\nTitle: '{title}'\nRemix: {remix}")
                    except:
                        print(f"Artist: '{artist}'\nTitle: '{title}'")

        input("\n")

except FileNotFoundError:
    exit(0)



