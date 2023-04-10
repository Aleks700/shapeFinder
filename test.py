import os


# print(os.path.join(os.getcwd(),'Hehehe'))



rowStart  = '<ImageRowGSD>'
rowEnd  = '<ImageRowGSD>'
columnStart  = '<ImageColumnGSD>'
columnEnd  = '<ImageColumnGSD>'
# print(len(rowStart))
# jpgDir = 'Meta'
# print(os.mkdir(jpgDir))
# print(os.path.join(os.getcwd(),jpgDir))
# print(os.path.exists(os.path.join(os.getcwd(),jpgDir)))




for root, dirs, files in os.walk('Turk_08032023_METAOne'):

    for i in files:
        p = os.path.join(os.getcwd(),root,i)
        # print(p)
        readed = open(p,'r').read()
        # type(readed.find(rowStart))
        # type(readed.find(rowStart))
        # type(readed.find(rowStart))
        # type(readed.find(rowStart))
       
        # print(readed.find(rowStart))
        # print(readed.find(rowEnd))
        # print(readed.find(columnStart))
        # print(readed.find(columnEnd))
        
        
        
        
        
        # print(readed[readed.find(rowStart):readed.find(rowEnd)]) 
        # print(readed[readed.find(columnStart) :readed.find(columnEnd)]) 
        print(readed[1:50])
        
        
        
        
        
        # print(readed.slice())
        # print(type(readed) )
        
        
   