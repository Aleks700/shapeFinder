import zipfile
import glob
import os

# listing = os.walk('\\10.20.1.246\\mnt\\kgs-data\\aerospace\\head\\2.Akt.obl\\08.03.2023')
# for paths in listing:
#     print(paths)


# targetPattern = r"\\10.20.1.246\\mnt\\kgs-data\\aerospace\\head\\2.Akt.obl\\08.03.2023*.zip"
targetPattern = r"\\10.20.1.246\mnt\kgs-data\\aerospace\\head\\2.Akt.obl\\08.03.2023\\*.zip"
pathsToList=glob.glob(targetPattern)
# print(pathsToList)


for file in pathsToList:
    file_zip = zipfile.ZipFile(file,'r')



    for file_info in file_zip.infolist():
        if file_info.filename.endswith('.shp'):
            print(file_info.filename)
            file_zip.extract(file_info.filename,'.NewShape')

file_zip.close()

