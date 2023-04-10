import os
import glob
import shutil

os.mkdir('.Atyrau09042023')
data_to_copy=[]

for root, dirs, files in os.walk(r"Y:\\3.Atyr.obl\\09.04.2023"):
    for file in files:
        if file.endswith('.xml') or file.endswith('.shp') or file.endswith('.shx') or file.endswith('.dbf') or file.endswith('.txt') or file.endswith('.prj') :
            data_to_copy.append(os.path.join(root, file))

        

for i in data_to_copy:
  
    shutil.copy2(i, '.Atyrau09042023')
    # shutil.copy(i,'./data')
    print(i)


# print(data_to_copy)

# data = os.walk('\\10.20.1.246\mnt\kgs-data\\aerospace\\head\\1.Turk.obl\11.03.2023\\200080092\\*.shp')

# print(data)
# for i in data:
#     print(i)
