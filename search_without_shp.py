import os
import glob
import shutil


pathToFolder = r"Y:\\6.WstKaz.obl\\27.04.2023\\1\\"
toExtract = 'SHP_WestQaz_270423_1'




os.mkdir(toExtract)
data_to_copy=[]

for root, dirs, files in os.walk(pathToFolder):
    for file in files:
        if file.endswith('.xml') or file.endswith('.shp') or file.endswith('.shx') or file.endswith('.dbf') or file.endswith('.txt') or file.endswith('.prj') :
            data_to_copy.append(os.path.join(root, file))

for i in data_to_copy:
  
    shutil.copy2(i, toExtract)
    # shutil.copy(i,'./data')
    print(i)


# print(data_to_copy)

# data = os.walk('\\10.20.1.246\mnt\kgs-data\\aerospace\\head\\1.Turk.obl\11.03.2023\\200080092\\*.shp')

# print(data)
# for i in data:
#     print(i)
