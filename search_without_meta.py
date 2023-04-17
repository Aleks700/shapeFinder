import os
import glob
import shutil


jpgDir = 'Meta_Atyrau_17042023'




rowStart  = '<ImageRowGSD>'
rowEnd  = '</ImageRowGSD>'
columnStart  = '<ImageColumnGSD>'
columnEnd  = '</ImageColumnGSD>'

os.mkdir(jpgDir)
data_to_copy=[]

for root, dirs, files in os.walk(r"Y:\\3.Atyr.obl\\17.04.2023\\L1"):
    for file in files:
        if file.endswith('.xml')    and  (file.find('meta')!=-1)  and (file.find('PAN')!=-1):
            data_to_copy.append(os.path.join(root, file))
        # if file.endswith('.xml') or file.endswith('.shp') or file.endswith('.shx') or file.endswith('.dbf') or file.endswith('.txt') or file.endswith('.prj') :
        #     data_to_copy.append(os.path.join(root, file))
        

for i in data_to_copy:
  
    shutil.copy2(i, jpgDir)
    # shutil.copy(i,'./data')
    print(i)






dataToWrite = []

for root, dirs, files in os.walk(jpgDir):

    for i in files:
        p = os.path.join(os.getcwd(),root,i)
        readed = open(p,'r').readlines()
        joinedString = "".join(readed)
        # print("row"+'\t'+  joinedString[joinedString.find(rowStart)+len(rowStart):joinedString.find(rowEnd)]) 
        # print("column"+'\t'+joinedString[joinedString.find(columnStart)+len(columnStart) :joinedString.find(columnEnd)]) 
        dataToWrite.append([i,'\t',joinedString[joinedString.find(rowStart)+len(rowStart):joinedString.find(rowEnd)],'\t',joinedString[joinedString.find(columnStart)+len(columnStart) :joinedString.find(columnEnd)],'\n'])
      
print(dataToWrite)
f = open('meta_Atyrau_17042023.txt','w')
for i in dataToWrite:
    # toWriteLine = str(i)+"\t"
    # f.writelines([i,'\t'])
    f.writelines(i)




# print(data_to_copy)

# data = os.walk('\\10.20.1.246\mnt\kgs-data\\aerospace\\head\\1.Turk.obl\11.03.2023\\200080092\\*.shp')

# print(data)
# for i in data:
#     print(i)
