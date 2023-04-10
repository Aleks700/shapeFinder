import zipfile
import glob

import os
import shutil



pathToExtract = 'Turk_08032023_META'
targetPattern = r"Y:\\1.Turk.obl\\08.03.2023\\*.zip"
pathsToList=glob.glob(targetPattern)






print(targetPattern)


for file in pathsToList:
    file_zip = zipfile.ZipFile(file,'r')
    


    objectToListWrite = []
    for file_info in file_zip.infolist():
        if file_info.filename.endswith('.xml') and  (file_info.filename.find('meta')!=-1) and  (file_info.filename.find('PAN')!=-1) :
       
       
     
            objectToListWrite.append(file_info.filename)
            



    for i in objectToListWrite:
        file_zip.extract(i,pathToExtract)
       
    
        print(i)


file_zip.close()





pathToWalk =  os.path.join(os.getcwd(),pathToExtract) 


jpgDir = pathToExtract+'One'
os.mkdir(jpgDir)

data_to_copy=[]

for root, dirs, files in os.walk(pathToWalk):
    for file in files:
        if file.endswith('.xml'):
            data_to_copy.append(os.path.join(root, file))

for i in data_to_copy:
    shutil.copy2(i, jpgDir)
    # shutil.copy(i,'./data')
    print(i)
    
    
for root, dirs, files in os.walk(jpgDir):
    # print(root)
    print(dirs)
    # print(files)

    for i in files:
        p = os.path.join(os.getcwd(),root,i)
        print(p)
        readed = open(p,'r')


