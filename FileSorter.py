import os
import shutil

#FUNCTIONS
def createdir(newDir):
    if not os.path.isdir(newDir):
        os.makedirs(newDir)
    return newDir;
def removeEmpty(directories):
    for dir in directories:
        if (len(os.listdir(dir)) == 0):
            shutil.rmtree(dir)
    return;
#MAIN
print("Sorting Files...")
currentDir = os.getcwd()
videoDir = createdir(currentDir + "/Videos")
pictureDir = createdir(currentDir + "/Pictures")
audioDir = createdir(currentDir + "/Audio")
programDir = createdir(currentDir + "/Programs")
documentDir = createdir(currentDir + "/Documents")
archiveDir = createdir(currentDir + "/Archived")
torrentDir = createdir(currentDir + "/Torrents")
directories = [videoDir, pictureDir, audioDir, programDir, documentDir, archiveDir, torrentDir]
files = os.listdir() #Get files in current folder
for i in files: #Sort files in specific folders
    if(i.lower().endswith(".png") or i.lower().endswith(".jpg") or i.lower().endswith(".gif")):     #PICTURES
        shutil.move(currentDir + "/" + i, pictureDir + "/" + i)
    elif (i.lower().endswith(".exe")):                                                                 #PROGRAMS
        shutil.move(currentDir + "/" + i, programDir + "/" + i)
    elif (i.lower().endswith(".mp3")  or i.lower().endswith(".waw")):                                    #AUDIO
        shutil.move(currentDir + "/" + i, audioDir + "/" + i)
    elif (i.lower().endswith(".pdf") or i.lower().endswith(".txt")  or i.lower().endswith(".html")
        or i.lower().endswith(".docx") or i.lower().endswith(".odt") or i.lower().endswith(".doc") ):    #DOCUMENTS
        shutil.move(currentDir + "/" + i, documentDir + "/" + i)
    elif (i.lower().endswith(".mp4") or i.lower().endswith(".wmw") or i.lower().endswith(".avi")):          # Video
        shutil.move(currentDir + "/" + i, programDir + "/" + i)
    elif (i.lower().endswith(".zip") or i.lower().endswith(".rar") or i.lower().endswith(".jar")
        or i.lower().endswith(".gz") or i.lower().endswith(".iso")):                                     # ARCHIVE
        shutil.move(currentDir + "/" + i, archiveDir + "/" + i)
    elif (i.lower().endswith(".torrent")):                                                               # torrents
        shutil.move(currentDir + "/" + i, torrentDir + "/" + i)
removeEmpty(directories) #Removes unused folders
print("Sorting Complete")