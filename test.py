import os


# print(os.path.join(os.getcwd(),'Hehehe'))




# jpgDir = 'Meta'
# print(os.mkdir(jpgDir))
# print(os.path.join(os.getcwd(),jpgDir))
# print(os.path.exists(os.path.join(os.getcwd(),jpgDir)))




for root, dirs, files in os.walk('Turk_08032023_METAOne'):

    for i in files:
        p = os.path.join(os.getcwd(),root,i)
        print(p)
        readed = open(p,'r').read()
        print(readed)
        print(readed.find('<ImageRowGSD>'))
        print(readed.find('</ImageRowGSD>'))
        print(readed.find('<ImageColumnGSD>'))
        print(readed.find('</ImageColumnGSD>'))