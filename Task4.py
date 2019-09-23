import shutil
import os
import zipfile
'''
Wayne O'Sullivan R00064536
I set loc equal to the location of my docs folder then used a for lop in os.walk(loc) to access the foldername, 
subfolder and filenames. I then used .endswith() to get .txt files. I used .strip(".txt") to seperate the filename, 
convereted the filename to uppercase with .upper() and added back the .txt. I then used 
shutil.copy(os.path.join(loc, filename), loc2) to copy all the files in my docs folder to the backup folder.
The below code ran fine on my windows machine Vincent. I was able to copy over the .txt files and create the zip 
folders no problem but i was getting a PermissionError for moving the subfolders. After the easter break i tried 
running it in the lab on the Vm but i was getting an error in shutil.copy() saying i can't pass an array??
'''
# make all files upper case then zip the docs folder * 3 and send it to backup
# then output the backup folder and the contents of one of the zipped folders
# os.listdir()

# Path directions for Linux
# loc = r'/home/cadmin/Desktop/wayneosullivan/Task4/working/docs'
# loc2 = r'/home/cadmin/Desktop/wayneosullivan/Task4/backup'
# loc3 = r'/home/cadmin/Desktop/wayneosullivan/Task4/backup/docs1_zip'

loc = r'C:\Users\Wayne\Desktop\wayneosullivan\Task4\working\docs'
loc2 = r'c:\users\wayne\desktop\wayneosullivan\Task4\backup'
loc3 = r'c:\users\wayne\desktop\wayneosullivan\Task4\backup\docs_1.zip'
#os.chdir(loc2)
for foldername, subfolder,filenames in os.walk(loc):
    for filename in filenames:
        if filename.endswith(".txt"):
            filename = filename.strip(".txt")
            filename = filename.upper()
            filename = filename + ".txt"
            #shutil.copy(os.path.join(loc, filename), loc2)
        shutil.copy(os.path.join(loc, filename), loc2)
       # print(filename)
    #for t in subfolder:
     #   print(t)
        #shutil.copy(os.path.join(loc, t), loc2) # Copying the folders (Wont allow me access on Windows)
        #shutil.move(os.path.join(loc, t), loc2) # Moving the folders


# The below function is from your code on Canvas Vincent for creating zipped folders
def zipBackup(folder):
    folder = os.path.abspath(folder)
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number = number + 1

    # Create the ZIP file
    backupZip = zipfile.ZipFile(zipFilename, 'w')
    # Walk the entire folder tree and compress the files in each folder.
    for foldername, subfolders, filenames in os.walk(folder):

        # Add the current folder to ZIP file
        backupZip.write(foldername)
        # Add all files in this folder to the ZIP file.
        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue  # Do not backup ZIP files
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()

    print('Done')

# This was to create 3 zip files
def tripleBackup():
    for i in range(3):
        zipBackup(r'''C:\Users\Wayne\Desktop\wayneosullivan\Task4\working\docs''')


tripleBackup() # calling the function


# This is for outputting the contents of the zipped folder using a for loop and the .namelist() method
def read_zip_file(filepath):
    zfile = zipfile.ZipFile(filepath)
    #zfile.extractall()
    for i in zfile.namelist():
        zfile.extract(i)
        print(i,"\n")
    #print(zfile.namelist())
    #for i in zfile.namelist():
     #   print(i,"\n")


read_zip_file(loc3)


# The below loop uses os.walk() to the backup folder and outputs the contents of the  backup folder
# showing that the data has been copied from working to backup.
for foldername, subfolder,filenames in os.walk(loc2):
    for s in subfolder:
        print(s)
    for filename in filenames:
        print(filename)