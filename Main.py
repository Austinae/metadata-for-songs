from os import listdir, rename, path
from tkinter.filedialog import askdirectory, Tk
from sys import exit
from tinytag import TinyTag
import re
import eyed3

try:
    Tk().withdraw() # Avoids showing tk window
    dir = askdirectory()
    listFiles = listdir(dir)
    text_file = open("log.txt", "w")

    for file in listFiles:
        fileNameAndExtension = path.splitext(file)
        if fileNameAndExtension[1] == ".mp3":
            print(fileNameAndExtension[0])
            audiofile = eyed3.load(dir+"/"+file)
            try:
                audiofile.tag.play_count = 0
            except Exception as ex:
                try:
                    text_file.write(fileNameAndExtension[0] + type(ex).__name__ + "\n")
                except:
                    continue

            try:
                formatArtist = re.compile("^[a-zA-Z0-9+].* -")
                formatTitle = re.compile("- [a-zA-Z0-9+].*")
                formatFeat = re.compile("\(Feat. [a-zA-Z0-9+].*\)")
                formatRemix = re.compile("\(Remix. [a-zA-Z0-9+].*\)")

                artistSearch = formatArtist.search(fileNameAndExtension[0])
                titleSearch = formatTitle.search(fileNameAndExtension[0])
                featSearch = formatFeat.search(fileNameAndExtension[0])
                remixSearch = formatRemix.search(fileNameAndExtension[0])
            except Exception as ex:
                try:
                    text_file.write(fileNameAndExtension[0] + type(ex).__name__ + "\n")
                except:
                    continue

            try:
                artist = artistSearch.group().replace(" -", "").strip()
            except Exception as ex:
                try:
                    text_file.write(fileNameAndExtension[0] + type(ex).__name__ + "\n")
                except:
                    continue

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
                        try:
                            title = titleSearch.group().replace("- ", "").strip()
                        except Exception as ex:
                            try:
                                text_file.write(fileNameAndExtension[0] + type(ex).__name__ + "\n")
                            except:
                                continue

            try:
                feat = featSearch.group().replace("(Feat. ", "").replace(")", "").split(", ")
                feat = [item.strip() for item in feat]
            except AttributeError:
                continue

            try:
                remix = remixSearch.group().replace("(Remix. ", "").replace(")", "").split(", ")
                remix = [item.strip() for item in remix]
            except AttributeError:
                continue

            try:
                audiofile.tag.title = title
                audiofile.tag.artist = artist
                audiofile.tag.album_artist = ", ".join(feat)
                audiofile.tag.original_artist = ", ".join(remix)
            except:
                try:
                    audiofile.tag.title = title
                    audiofile.tag.artist = artist
                    audiofile.tag.album_artist = ", ".join(feat)
                    audiofile.tag.original_artist = ""
                except:
                    try:
                        audiofile.tag.title = title
                        audiofile.tag.artist = artist
                        audiofile.tag.album_artist = ""
                        audiofile.tag.original_artist = ", ".join(remix)
                    except:
                        try:
                            audiofile.tag.title = title
                            audiofile.tag.artist = artist
                            audiofile.tag.album_artist = ""
                            audiofile.tag.original_artist = ""
                        except Exception as ex:
                            try:
                                text_file.write(fileNameAndExtension[0] + type(ex).__name__ + "\n")
                            except:
                                continue

            audiofile.tag.save()
except FileNotFoundError:
    exit(0)