import zipfile
import glob

import os
import shutil



pathToExtract = 'Akt05042023'
targetPattern = r"Y:\\2.Akt.obl\\05.04.2023\\*.zip"
pathsToList=glob.glob(targetPattern)


rowStart  = '<ImageRowGSD>'
rowEnd  = '</ImageRowGSD>'
columnStart  = '<ImageColumnGSD>'
columnEnd  = '</ImageColumnGSD>'



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
    
    print(i)
    


dataToWrite = []

for root, dirs, files in os.walk(jpgDir):

    for i in files:
        p = os.path.join(os.getcwd(),root,i)
        readed = open(p,'r').readlines()
        joinedString = "".join(readed)
        # print("row"+'\t'+  joinedString[joinedString.find(rowStart)+len(rowStart):joinedString.find(rowEnd)]) 
        # print("column"+'\t'+joinedString[joinedString.find(columnStart)+len(columnStart) :joinedString.find(columnEnd)]) 
        dataToWrite.append([i,joinedString[joinedString.find(rowStart)+len(rowStart):joinedString.find(rowEnd)],joinedString[joinedString.find(columnStart)+len(columnStart) :joinedString.find(columnEnd)],'\n'])
      
print(dataToWrite)
f = open('meta_To_exist_05042023.txt','w')
for i in dataToWrite:
    f.writelines(i)