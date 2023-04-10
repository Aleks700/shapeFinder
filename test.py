import os


# print(os.path.join(os.getcwd(),'Hehehe'))



rowStart  = '<ImageRowGSD>'
rowEnd  = '</ImageRowGSD>'
columnStart  = '<ImageColumnGSD>'
columnEnd  = '</ImageColumnGSD>'
# print(len(rowStart))
# jpgDir = 'Meta'
# print(os.mkdir(jpgDir))
# print(os.path.join(os.getcwd(),jpgDir))
# print(os.path.exists(os.path.join(os.getcwd(),jpgDir)))


dataToWrite = []


for root, dirs, files in os.walk('.JPG_optim_Turkestan11032023Meta'):

    for i in files:
        p = os.path.join(os.getcwd(),root,i)
        readed = open(p,'r').readlines()
        joinedString = "".join(readed)
        # print("row"+'\t'+  joinedString[joinedString.find(rowStart)+len(rowStart):joinedString.find(rowEnd)]) 
        # print("column"+'\t'+joinedString[joinedString.find(columnStart)+len(columnStart) :joinedString.find(columnEnd)]) 
        dataToWrite.append([i,joinedString[joinedString.find(rowStart)+len(rowStart):joinedString.find(rowEnd)],joinedString[joinedString.find(columnStart)+len(columnStart) :joinedString.find(columnEnd)],'\n'])
        
print(dataToWrite)
f = open('meta_To_exisTurkestan11032023Meta.txt','w')
for i in dataToWrite:
    print(i)
    toWrite = i
    f.writelines(toWrite)