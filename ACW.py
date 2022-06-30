import ctypes, os, random

defaultDir = os.environ["USERPROFILE"] + "\\"
inDefaultDir = True
subDir = [""]
allSubDir = False

if inDefaultDir == True:
    allFiles = [files for files in os.listdir(defaultDir) if os.path.isfile(defaultDir + files)]
elif inDefaultDir == False:
    allFiles = []
if allSubDir:
    subDir = [dir for dir in os.listdir(defaultDir) if os.path.isdir(defaultDir + dir)]

def fileTree(path):
    allFiles = []
    for entry in os.listdir(path):
        fullPath = os.path.join(path, entry)
        if os.path.isdir(fullPath):
            allFiles = allFiles + fileTree(fullPath)
        else:
            allFiles.append(fullPath)
    return allFiles

for i in range(len(subDir)):
    allFiles += fileTree(defaultDir + subDir[i])
blacklist = open(__file__.rstrip(os.path.basename(__file__)) + "blacklist.txt", "r")
blacklistFiles = blacklist.readlines()
for i in range(len(blacklistFiles)):
    blacklistFiles[i] = blacklistFiles[i].rstrip("\n")
    if os.path.isfile(blacklistFiles[i]):
        allFiles = [files for files in allFiles if files.lower() != blacklistFiles[i].lower()]
    elif os.path.isfile(defaultDir + blacklistFiles[i]):
        allFiles = [files for files in allFiles if files.lower() != (defaultDir + blacklistFiles[i]).lower()]
    else:
        allFiles = [files for files in allFiles if not files.lower().endswith(blacklistFiles[i].lower())]

ctypes.windll.user32.SystemParametersInfoW(20, 0, random.choice([images for images in allFiles if images.endswith(".jpg") or images.endswith(".png")]), 0)
